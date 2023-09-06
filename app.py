from flask import Flask, render_template, request
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


@app.route('/', methods=['GET','POST'])
def render_history_page():
    return render_template('history.html')
        
app.run(debug = True)
