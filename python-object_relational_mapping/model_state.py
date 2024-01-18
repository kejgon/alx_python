from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Assuming MySQL server is running on localhost with default port 3306
    engine = create_engine('mysql+mysqldb://user:password@localhost:3306/hbtn_0e_6_usa')
    Base.metadata.create_all(engine)
