from Flask import flask 
app = flask(__name__)
def home():
  return "Bonjour depuis Render: Votre app from flask est bien en ligne "
if __name__ == '__main__':
  app.run()
