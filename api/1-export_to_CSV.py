import csv
import requests
import sys
from sys import argv


def export_to_CSV(sizeofReq):
    """ Export employee's TODO list data to a CSV file """

    # Variables
    allTasks = []  # List to store all tasks data

    link = "https://jsonplaceholder.typicode.com"  # Base URL for the API

    # GET requests to fetch user details and TODO list
    usersRes = requests.get("{}/users/{}".format(link, sizeofReq))
    todosRes = requests.get("{}/users/{}/todos".format(link, sizeofReq))

    # Get the JSON data from responses
    name = usersRes.json().get('username')  # Extract employee username from user response
    todosJson = todosRes.json()  # Extract TODO list JSON data

    # Save the employee data and loop through the tasks to save task data
    for task in todosJson:
        taskRow = []  # List to store data for each task
        taskRow.append(sizeofReq)  # Add employee ID to task data
        taskRow.append(name)  # Add employee name to task data
        taskRow.append(task.get('completed'))  # Add task completion status to task data
        taskRow.append(task.get('title'))  # Add task title to task data
        allTasks.append(taskRow)  # Append task data to allTasks list

    # Write task data to a CSV file
    filename = "{}.csv".format(sizeofReq)
    with open(filename, "w", newline='') as csvFile:
        csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)  # Create a CSV writer object
        csvWriter.writerows(allTasks)  # Write allTasks data to the CSV file

    print(f"CSV file '{filename}' created successfully.")

    return 0


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    export_to_CSV(int(argv[1]))  # Fetch employee ID from command line argument and export data to CSV
