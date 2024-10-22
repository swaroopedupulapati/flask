from flask import Flask, request,render_template
from pymongo import MongoClient

my_client = MongoClient("localhost",27017)
my_db=my_client["cse4"]
my_collection = my_db["login"]

app = Flask(__name__)
@app.route('/', methods=['GET',"POST"])
def login():
    if request.method == 'POST':
        name=request.form["username"]
        phone_no = request.form["phone_number"]
        email = request.form["email"]
        my_collection.insert_one({"name":name,"phone_no":phone_no,"email":email})
        return "<h2>submit successfully</h2>"
    else:
        return render_template("index.html")