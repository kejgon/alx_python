import MySQLdb
import sys

def search_states(username, password, database, state_name):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute query to search for states based on state_name
    query = "SELECT id, name FROM states WHERE name = '{}' ORDER BY id".format(state_name)
    cursor.execute(query)

    # Fetch all rows
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the database connection
    db.close()

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    # Get username, password, database, and state_name from command line arguments
    username, password, database, state_name = sys.argv[1:]

    # Call the function to search for states based on state_name
    search_states(username, password, database, state_name)
