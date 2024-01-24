from flask import Flask
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
