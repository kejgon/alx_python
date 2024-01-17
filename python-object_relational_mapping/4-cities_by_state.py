import MySQLdb
import sys

def list_cities(username, password, database):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute query to list all cities
    query = "SELECT id, state_id, name FROM cities ORDER BY id"
    cursor.execute(query)

    # Fetch all rows
    cities = cursor.fetchall()

    # Print the results
    for city in cities:
        print(city)

    # Close the database connection
    db.close()

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    # Get username, password, and database from command line arguments
    username, password, database = sys.argv[1:]

    # Call the function to list all cities
    list_cities(username, password, database)
