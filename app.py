from flask import Flask, flash, render_template, request, redirect, session, send_from_directory, url_for
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import os
from werkzeug.utils import secure_filename

connection = mysql.connector.connect(
    passwd="",  # password for the database
    user="root",  # username
    database="cv",  # database name
    port=3307,  # port on which the MySQL server is running
    auth_plugin='mysql_native_password'  # if you are using MySQL 8.x
)

cursor = connection.cursor(dictionary=True)

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app.secret_key = 'stefan'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    upit = "SELECT * FROM korisnici WHERE id = %s"
    cursor.execute(upit, (user_id,))
    return cursor.fetchone()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('logout'))


def ulogovan():
    if "ulogovani_korisnik" in session:
        return True
    else:
        return False


@app.route('/', methods=["GET", "POST"])
def render_korisnik_novi():
    if request.method == "GET":
        upit2 = "select * from users"
        cursor.execute(upit2)
        users = cursor.fetchall()
        return render_template('register.html', users=users)

    if request.method == "POST":
        forma = request.form
        hesovana_lozinka = generate_password_hash(forma["lozinka"])
        vrednosti = (
            forma["username"],
            hesovana_lozinka
        )

        upit = """insert into
                    users(username,  password)
                    values (%s, %s)
        """
        cursor.execute(upit, vrednosti)
        connection.commit()
        return redirect(url_for("login"))


# Deo za login

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        forma = request.form
        upit = "SELECT * FROM users WHERE username=%s"
        vrednost = (forma["username"],)
        cursor.execute(upit, vrednost)
        korisnik = cursor.fetchone()
        if korisnik and check_password_hash(korisnik["password"], forma["password"]):
            session["ulogovani_korisnik"] = korisnik
            return redirect(url_for("render_create_page"))
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")


@app.route('/create', methods=['GET', 'POST'])
def render_create_page():
    if request.method == 'POST':
        user_id = session["ulogovani_korisnik"]["id"]
        profilepicture = request.files['profilepicture']  # Get the uploaded file

        if profilepicture and allowed_file(profilepicture.filename):
            filename = secure_filename(profilepicture.filename)
            profilepicture.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Save the file to the UPLOAD_FOLDER
            profilepicture_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # Continue with the rest of your data processing
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            email = request.form['email']
            address = request.form['address']
            zip_code = request.form['zip_code']
            phone_number = request.form['phone_number']
            city = request.form['city']

            # Insert basic data into the database
            cursor.execute(
                "INSERT INTO info (user_id, profilepicture, first_name, last_name, email, address, zip_code, phone_number, city) "
                "VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)",
                (user_id, profilepicture_path, first_name, last_name, email, address, zip_code, phone_number, city)
            )
            connection.commit()

            # Redirect to the next page for adding additional info
            return redirect(url_for('render_history_page'))
        else:
            flash('Allowed image types are - png, jpg, jpeg, gif')
            return redirect(request.url)

    return render_template('index.html')  # Render a form for basic info


@app.route('/history', methods=['GET', 'POST'])
def render_history_page():
    if request.method == 'POST':
        user_id = session["ulogovani_korisnik"]["id"]
        resume_description = request.form['resume_description']
        job_title = request.form['job_title']
        work_citytown = request.form['work_citytown']
        employer = request.form['employer']
        work_startdate = request.form['work_startdate']
        work_enddate = request.form['work_enddate']
        work_description = request.form['work_description']
        degree = request.form['degree']
        education_citytown = request.form['education_citytown']
        school = request.form['school']
        education_startdate = request.form['education_startdate']
        education_enddate = request.form['education_enddate']
        education_description = request.form['education_description']
        hobby = request.form['hobby']
        skills = request.form['skills']

        # Insert additional data into the database
        cursor.execute(
            "UPDATE info SET resume_description=%s, job_title=%s, work_citytown=%s, employer=%s, "
            "work_startdate=%s, work_enddate=%s, work_description=%s, degree=%s, education_citytown=%s, "
            "school=%s, education_startdate=%s, education_enddate=%s, education_description=%s, hobby=%s, skills=%s "
            "WHERE user_id = %s",
            (resume_description, job_title, work_citytown, employer, work_startdate, work_enddate, work_description,
             degree, education_citytown, school, education_startdate, education_enddate, education_description,
             hobby, skills, user_id)
        )

        connection.commit()

        return redirect(url_for('render_template_page'))  # Redirect to the 'history_page' route

    return render_template('history.html')  # Render a form for additional info


@app.route('/template', methods=['GET', 'POST'])
def render_template_page():
    return render_template('template.html')


@app.route('/modern_template', methods=['GET'])
def render_modern_template():
    if "ulogovani_korisnik" not in session:
        return redirect(url_for('login'))  # Redirect to login if the user is not logged in

    user_id = session["ulogovani_korisnik"]["id"]

    # Execute a query to fetch information from the "info" table for the current user
    cursor.execute("SELECT * FROM info WHERE user_id = %s", (user_id,))
    info = cursor.fetchone()

    return render_template('modern.html', info=info)


if __name__ == "__main__":
    app.run(debug=True)