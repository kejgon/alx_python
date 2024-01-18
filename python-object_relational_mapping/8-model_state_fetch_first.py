import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine for database connection
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}"
    )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object only
    first_state = session.query(State).first()

    # Print the results appropriately
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
