# Amethyst Chatbot – Orbit 2024

Amethyst Chatbot is an intent-based chatbot designed to provide stress consultation and early stress detection for workers.  
This project was developed as part of the Orbit 2024 program using Natural Language Processing (NLP) techniques and a web-based interface.

## Project Overview
Amethyst Chatbot helps users express work-related stress conditions through conversational interaction.  
User inputs are processed using NLP techniques and classified into predefined stress-related intents, allowing the system to provide appropriate responses and basic guidance.

This application is intended as an **early-stage support and awareness tool**, not as a medical or psychological diagnosis system.

## Features
- Stress consultation chatbot for workers
- Early stress detection based on user input
- Intent-based NLP classification
- Custom stress-related training dataset
- Neural network model for intent classification
- Web-based interface using Flask
- Modular and maintainable project structure

## Technologies Used
- Python
- Flask (Web Framework)
- NLTK (Text Preprocessing)
- PyTorch (Neural Network Model)
- NumPy
- HTML & CSS

## Project Structure
app.py # Main Flask application
train.py # Model training script
chat.py # Chatbot logic
model.py # Neural network model
nltk_utils.py # NLP preprocessing utilities
intents.json # Stress-related training dataset
templates/ # HTML templates
static/ # CSS and static assets
requirements.txt # Project dependencies



## How to Run the Project
1. Install project dependencies:
```bash
pip install -r requirements.txt
```
2. Run the application:
```bash
python app.py
```
## Team Project & My Role
This project was developed as a team project during the Orbit 2024 program.

My contributions include:
- Developed backend logic for the chatbot using Python
- Implemented NLP-based intent classification and response handling
- Integrated the chatbot model with the Flask web application
- Organized and maintained the project repository


## Disclaimer
Amethyst Chatbot is designed for educational and early awareness purposes only.
It does not replace professional mental health consultation.

## Author
Danang Prayogi
Orbit 2024
