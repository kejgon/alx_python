import MySQLdb
import sys

def list_states_starting_with_N(username, password, database):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute query to get states starting with 'N' (case-sensitive)
    cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' COLLATE utf8mb4_bin ORDER BY id")

    # Fetch all rows
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the database connection
    db.close()

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    # Get username, password, and database from command line arguments
    username, password, database = sys.argv[1:]

    # Call the function to list states starting with 'N' (case-insensitive)
    list_states_starting_with_N(username, password, database)
