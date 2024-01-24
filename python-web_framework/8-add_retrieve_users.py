from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 7-db_setup.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

# Constructing the SQLAlchemy URI
db_uri = f"mysql://{db_username}:{db_password}@{db_host}/{db_name}"

# Configuring Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating SQLAlchemy instance
db = SQLAlchemy(app)

# Your model class here
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()  # This calls the function to create tables

# Your routes and other Flask code here

@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        new_user = User(name=name, email=email)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash("User added successfully!", 'success')
        except IntegrityError:
            db.session.rollback()
            flash("Error: Email already exists!", 'error')

    return render_template('add_user.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
