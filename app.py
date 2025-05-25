from flask import Flask

app = Flask(__name__)

def home():
    return "Bonjour depuis Render : Votre app Flask est bien en ligne"

if __name__ == '__main__':
    app.run()
