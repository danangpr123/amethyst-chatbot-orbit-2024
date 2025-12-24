from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_mysqldb import MySQL
from MySQLdb.cursors import DictCursor
from werkzeug.security import check_password_hash, generate_password_hash
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import string
from chat import get_response


app = Flask(__name__)
# koneksi
app.secret_key = "secretkey"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'
app.config['MYSQL_CHARSET'] = 'utf8mb4'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

# Load the model
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/stress.csv")

def clean(text, stopword, stemmer):  
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    text = ' '.join([word for word in text.split(' ') if word not in stopword])
    text = ' '.join([stemmer.stem(word) for word in text.split(' ')])
    return text

# Clean the text data
stopword = set(stopwords.words('english'))  
stemmer = SnowballStemmer("english")  
data["text"] = data["text"].apply(lambda x: clean(x, stopword, stemmer))  

# Convert label to categorical
data["label"] = data["label"].map({0: "No Stress", 1: "Stress"})
data = data[["text", "label"]]

# Prepare data for training
x = np.array(data["text"])
y = np.array(data["label"])

cv = CountVectorizer()
X = cv.fit_transform(x)
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.33, random_state=42)

# Train the model
model = BernoulliNB()
model.fit(xtrain, ytrain)

# Deteksi route
@app.route('/deteksi')
def deteksi():
    return render_template('deteksi.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        user_input = request.form['text']
        data = cv.transform([user_input]).toarray()
        output = model.predict(data)[0]
        return render_template('result.html', prediction=output)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    message = data['message']
    response = get_response(message)
    return jsonify({'answer': response})

@app.route("/")
def home():
    if 'loggedin' in session:
        return render_template("index.html")
    flash ('Harap Login Terlebih Dahulu','danger')
    return redirect (url_for('login'))

@app.route("/journaling", methods=['GET', 'POST'])
def catatan():
    if 'loggedin' in session:
        if request.method == 'POST':
            date = request.form['date']
            note = request.form['note']
            username = session['username']
            
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO tb_journal (username, date, note) VALUES (%s, %s, %s)', (username, date, note))
            mysql.connection.commit()
            cursor.close()
            flash('Catatan Jurnal Berhasil Disimpan', 'success')
            return redirect(url_for('view_journal'))  # redirect ke halaman view_journal
        return render_template("journaling.html")
    else:
        flash('Harap Login Terlebih Dahulu', 'danger')
        return redirect(url_for('login'))


@app.route("/view_journal", methods=['GET', 'POST'])
def view_journal():
    if 'loggedin' in session:
        username = session['username']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_journal WHERE username=%s', (username,))
        journal_entries = cursor.fetchall()
        cursor.close()

        print("Journal Entries:", journal_entries)  # Check the result of the query

        if journal_entries:  # If journal entries are found
            return render_template("view_journal.html", journal_entries=journal_entries)
        else:
            flash('Tidak ada entri jurnal yang ditemukan', 'warning')
            return render_template("view_journal.html", journal_entries=[])
    else:   
        flash('Harap Login Terlebih Dahulu', 'danger')
        return redirect(url_for('login'))




@app.route("/about")    
def about():
    return render_template("about.html")

@app.route("/mind_body")
def mind_body():
    return render_template("mind_body.html")

@app.route("/recharge_explore")
def recharge_explore():
    return render_template("recharge_explore.html")


@app.route('/cal', methods=['GET', 'POST'])
def cal():
    if request.method == 'POST':
        if 'id' in session:
            user_id = session['id']
            mood = request.form.get('mood')  
            date = request.form.get('date')

            if mood and date:  
                try:
                 
                    cur = mysql.connection.cursor()
                    cur.execute("INSERT INTO moods (user_id, mood, date) VALUES (%s, %s, %s)", (user_id, mood, date))
                    mysql.connection.commit()
                    cur.close()

                    flash('Mood added successfully!', 'success')
                    return redirect(url_for('calendar'))
                except Exception as e:
                    flash(f'An error occurred: {str(e)}', 'error')
                    return redirect(url_for('calendar'))
            else:
                flash('Please fill in all required fields.', 'error')
                return redirect(url_for('calendar'))

   
    return redirect(url_for('home')) 


@app.route("/mood", methods=['GET', 'POST'])
def mood():
    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(DictCursor)
    cur.execute("SELECT * FROM moods ORDER BY id")
    calendar = cur.fetchall()
    return render_template('calendar.html', calendar = calendar)


@app.route("/suggestion")
def suggestion():
    return render_template("suggestion.html")

@app.route("/login", methods=('GET','POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_user WHERE email=%s', (email,))
        akun = cursor.fetchone()

        if akun is None:
            flash('Login Gagal, Cek Username Anda ', 'danger')
        elif not check_password_hash(akun['password'], password):
            flash('Login Gagal, Cek Password Anda', 'danger')
        else:
            session['loggedin'] = True
            session['username'] = akun['username']
            return redirect(url_for('home'))
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('loggedin',None)
    session.pop('username',None)
    return redirect (url_for('login'))

@app.route("/register", methods=('GET','POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        #cek username atau email
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_user WHERE username=%s OR email=%s',(username, email, ))
        akun = cursor.fetchone()
        if akun is None:
            cursor.execute('INSERT INTO tb_user VALUES (NULL, %s, %s, %s)',(username,email,generate_password_hash(password)))
            mysql.connection.commit()
            flash('Registrasi Berhasil',' Sukses')
        else :
            flash ('Username atau email sudah ada', 'danger')       
    return render_template("register.html")

@app.route("/journaling")
def journaling():
    return render_template("journaling.html")

@app.route("/meditation")
def meditation():
    return render_template("meditation.html")

@app.route("/sport")
def sport():
    return render_template("sport.html")

@app.route("/article")
def article():
    return render_template("article.html")

@app.route("/place")
def place():
    return render_template("place.html")

@app.route("/activities")
def activities():
    return render_template("activities.html")


@app.route("/delete/<int:entry_id>", methods=['POST'])
def delete_entry(entry_id):
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM tb_journal WHERE id=%s', (entry_id,))
        mysql.connection.commit()
        cursor.close()
        flash('Catatan Jurnal Berhasil Dihapus', 'success')
        return redirect(url_for('view_journal'))
    else:
        flash('Harap Login Terlebih Dahulu', 'danger')
        return redirect(url_for('login'))

@app.route("/edit/<int:entry_id>", methods=['GET', 'POST'])
def edit_entry(entry_id):
    if 'loggedin' in session:
        if request.method == 'POST':
            new_note = request.form['note']
            cursor = mysql.connection.cursor()
            cursor.execute('UPDATE tb_journal SET note=%s WHERE id=%s', (new_note, entry_id))
            mysql.connection.commit()
            cursor.close()
            flash('Catatan Jurnal Berhasil Diedit', 'success')
            return redirect(url_for('view_journal'))
        else:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM tb_journal WHERE id=%s', (entry_id,))
            entry = cursor.fetchone()
            cursor.close()
            return render_template("edit_entry.html", entry=entry)
    else:
        flash('Harap Login Terlebih Dahulu', 'danger')
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)