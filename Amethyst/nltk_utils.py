import numpy as np #numpy: Library untuk operasi numerik dan array.
import nltk # nltk.download('punkt')
from nltk.stem.porter import PorterStemmer #PorterStemmer: Algoritma stemming yang mengubah kata ke bentuk dasarnya (stem).
stemmer = PorterStemmer()

#tokenisasi 
def tokenize(sentence):
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    return nltk.word_tokenize(sentence)

#stemming
def stem(word):
    """
    stemming = find the root form of the word
    examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())

#bag_of_words
def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ['aktivitas_relaksasi', 'bahagia', 'bertanya', 'dukungan_keluarga', 'dukungan_online', 'dukungan_sosial', 'goal_setting', 'istirahat_sebentar', 'komunikasi_terbuka', 'lawakan_ringan', 'manajemen_emosi', 'manajemen_waktu', 'masa depan', 'masa lalu', 'motivasi', 'motivasi_diri', 'motivasi_kerja', 'pemahaman_diri', 'pemulihan', 'pencegahan_burnout', 'penerimaan_diri', 'pengelolaan_kecemasan', 'pengembangan_diri', 'perawatan_diri', 'perawatan_krisis', 'percaya diri']
    words = ["hi", "hello", "saya", "kamu", "selamat tinggal", "terimakasih", "baik"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag
