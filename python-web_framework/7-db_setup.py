from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)

# Check for command-line arguments
if len(sys.argv) != 5:
    print("Usage: python app.py <db_username> <db_password> <db_host> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_host = sys.argv[3]
db_name = sys.argv[4]

# Constructing the SQLAlchemy URI
db_uri = f"mysql+mysqldb://{db_username}:{db_password}@{db_host}/{db_name}"

# Configuring Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating SQLAlchemy instance
db = SQLAlchemy(app)

# Your model class here
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()  # This calls the function to create tables

# Your routes and other Flask code here

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
