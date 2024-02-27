# import requests
# import sys
# from csv import writer

# def get_employee(sizeofReq):
#   """ Use API from jsonplaceholder to get employee's TODO list progress and export to CSV """

#   # Variables
#   taskList = []
#   count = 0

#   link = "https://jsonplaceholder.typicode.com"

#   # GET requests to fetch user details and TODO list
#   usersRes = requests.get(
#       "{}/users/{}".format(link, sizeofReq))
#   todosRes = requests.get(
#       "{}/users/{}/todos".format(link, sizeofReq))

#   # Get the JSON data from responses
#   name = usersRes.json().get('name')
#   todosJson = todosRes.json()

#   # Save the employee name and loop through the tasks
#   for task in todosJson:
#     taskList.append([
#         sizeofReq,  # User ID
#         name,       # Username
#         task.get('completed'),  # Completed Status
#         task.get('title')      # Task Title
#     ])

#   # Open CSV file for writing with user ID as filename
#   with open(f"{sizeofReq}.csv", "w", newline='') as csvfile:
#     csv_writer = writer(csvfile)
#     csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])  # Header row
#     csv_writer.writerows(taskList)  # Write task data

#   # Print confirmation message
#   print(f"Employee data exported to {sizeofReq}.csv")

#   return 0

# if __name__ == '__main__':
#   get_employee(argv[1])
import requests
import csv
import sys
from sys import argv

def get_employee(sizeofReq):
    """ Use API from jsonplaceholder to get employee's TODO list progress """

    # Variables
    taskList = []  # Initialize an empty list to store completed task titles
    count = 0  # Initialize a counter for completed tasks

    link = "https://jsonplaceholder.typicode.com"  # Base URL for the API

    # GET requests to fetch user details and TODO list
    usersRes = requests.get(
        "{}/users/{}".format(link, sizeofReq))
    todosRes = requests.get(
        "{}/users/{}/todos".
        format(link, sizeofReq))

    # Get the JSON data from responses
    user_id = sizeofReq
    username = usersRes.json().get('username')  # Extract employee username from user response
    todosJson = todosRes.json()  # Extract TODO list JSON data

    # Save the employee tasks
    for task in todosJson:
        taskList.append([user_id, username, str(task.get('completed')), task.get('title')])

    # Write data to CSV file
    filename = "{}.csv".format(user_id)
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write header
        csvwriter.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        # Write tasks
        csvwriter.writerows(taskList)

    print("Data exported to", filename)

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python3 script.py <user_id>")
        sys.exit(1)
    get_employee(argv[1])  # Fetch employee progress using command line argument
