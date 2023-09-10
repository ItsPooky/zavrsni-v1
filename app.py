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

@app.route('/', methods=['GET', 'POST'])
def render_home_page():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        address = request.form['address']
        zip_code = request.form['zip_code']
        phone_number = request.form['phone_number']
        city = request.form['city']

        # Insert data into the database (You should sanitize and validate data before inserting)
        cursor.execute(
            "INSERT INTO info (first_name, last_name, email, address, zip_code, phone_number, city) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (first_name, last_name, email, address, zip_code, phone_number, city)
        )
        connection.commit()

        # Redirect to the next page
        return redirect(url_for('render_history_page'))

    return render_template('index.html')
    
@app.route('/2', methods=['GET', 'POST'])
def render_history_page():
    if request.method == 'POST':
        return redirect(url_for('history_page'))
    return render_template('history.html')

@app.route('/history')
def history_page():
    return render_template('history.html')

app.run(debug = True)
connection.close() 