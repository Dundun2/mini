from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import requests
import certifi

app = Flask(__name__)

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.4kiuj.mongodb.net/cluster0?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def main():

    return render_template("index.html")

@app.route('/index2')
def index2():

    return render_template("index2.html")

@app.route('/index3')
def index3():

    return render_template("index3.html")

@app.route('/index4')
def index4():

    return render_template("index4.html")

@app.route('/index5')
def index5():

    return render_template("index5.html")



if __name__ == '__main__':
    app.run('0.0.0.0', port=5500, debug=True)