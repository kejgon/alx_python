from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Replace 'kejgon', 'Password', 'localhost:3306', and 'alx_flask_db' with your actual credentials and database information
db_username = 'kejgon'
db_password = 'Password'
db_host = 'localhost:3306'
db_name = 'alx_flask_db'

# Constructing the SQLAlchemy URI
db_uri = f"mysql+mysqldb://{db_username}:{db_password}@{db_host}/{db_name}"

# Configuring Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Creating SQLAlchemy instance
db = SQLAlchemy(app)

# Your USER Model class here
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

@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
