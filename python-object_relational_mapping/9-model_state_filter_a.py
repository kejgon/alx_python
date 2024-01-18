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

    # Query states containing the letter 'a' in their name, ordered by id
    states_with_a = session.query(State).filter(State.name.like("%a%")).order_by(State.id).all()

    # Print the results in the specified format
    for state in states_with_a:
        print(f"{state.id}: {state.name}")
