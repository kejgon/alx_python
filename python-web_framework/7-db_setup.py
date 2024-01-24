from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 7-db_setup.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqldb://{db_username}:{db_password}@{db_host}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Creating a Base object
Base = declarative_base()

# Creating the State class
class State(Base):
    __tablename__ = 'states'

    # Columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

# Main section
if __name__ == "__main__":
    # Connecting to the MySQL server
    engine = create_engine(f"mysql+mysqldb://{db_username}:{db_password}@{db_host}/{db_name}")

    # Creating tables in the database
    Base.metadata.create_all(engine)

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
