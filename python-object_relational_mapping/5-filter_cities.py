import MySQLdb
import sys

def list_cities_by_state(username, password, database, state_name):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute parameterized query to list cities of the specified state
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id
    """
    cursor.execute(query, (state_name,))

    # Fetch all rows
    cities = cursor.fetchall()

    # Format the output
    city_names = ', '.join(city[0] for city in cities)

    # Print the results
    print(city_names)

    # Close the database connection
    db.close()

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    # Get username, password, database, and state_name from command line arguments
    username, password, database, state_name = sys.argv[1:]

    # Call the function to list cities of the specified state
    list_cities_by_state(username, password, database, state_name)
