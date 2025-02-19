from flask import Flask, render_template, request
from pymongo import MongoClient
import os

client = MongoClient("mongodb://localhost:27017/")
db = client["my_portfolio"]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contactus', methods = ['POST'])
def contactus():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    doc = {
        'name' : name,
        'email' : email,
        'message' : message
    }

    db.contactus.insert_one(doc)
    return "Thank you for contacting us. We will get back to you soon."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
