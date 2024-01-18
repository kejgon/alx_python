"""Importing SQLAlchemy"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

"""Creating a Base object"""
Base = declarative_base()

"""Creating the State class"""
class State(Base):
    """Class representing the 'states' table in the database."""
    __tablename__ = 'states'
    
    # Columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

"""Main section"""
if __name__ == "__main__":
    # Connecting to the MySQL server
    # Replace 'kejgon', 'Password', 'localhost:3306', and 'hbtn_test_db_5' with your actual credentials and database information
    engine = create_engine('mysql+mysqldb://kejgon:Password@localhost:3306/hbtn_test_db_5')
    
    # Creating tables in the database
    Base.metadata.create_all(engine)
