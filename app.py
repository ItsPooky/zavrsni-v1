from flask import Flask, render_template, jsonify, url_for, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

connection = mysql.connector.connect(
    passwd="root", # password for the database
    user="root", # username
    database="cv", # database name     
    port=3306, # port on which the mysql server is running 
    auth_plugin='mysql_native_password' # if you are using mysql 8.x  
)

cursor = connection.cursor(dictionary=True)

app = Flask(__name__) 

app.secret_key = 'stefan'

@app.route('/', methods=['GET','POST'])
def render_home_page():
    return render_template('index.html')

def insert_data():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        address = request.form['address']
        zip_code = request.form['zip_code']
        phone_number = request.form['phone_number']
        city = request.form['city']
        
app.run(debug = True)
connection.close() 