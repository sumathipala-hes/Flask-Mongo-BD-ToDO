from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "262c7eccf4efd9296699a61f9fa13b198b3d952e"
app.config["MONGO_URI"] = "mongodb+srv://sudarshan:0000@cluster0.z2vlalu.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"

# setup MongoDB
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes
