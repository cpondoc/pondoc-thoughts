from flask import Flask
from tinydb import TinyDB, Query

# Set up flask app and database
app = Flask(__name__)
db = TinyDB('data/db.json')

@app.route("/")
def hello_world():
    posts = db.all()
    sample_text = posts[0]['content']
    return "<p>" + str(sample_text) + "</p>"