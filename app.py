from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bonjour depuis Render : Votre app Flask est bien en ligne"

if __name__ == '__main__':
    app.run(debug=True)
