import requests
import sys
from sys import argv  # Importing argv from sys module

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
    name = usersRes.json().get('name')  # Extract employee name from user response
    todosJson = todosRes.json()  # Extract TODO list JSON data

    # Save the employee Name and Loop through the tasks
    for task in todosJson:
        if task.get('completed') is True:
            count += 1  # Increment count for completed tasks
            taskList.append(task.get('title'))  # Save completed task title to taskList

    # Print the first line with employee's progress
    print('Employee {} is done with tasks({}/{}):'.format(
        name, count, len(todosJson)))

    # Loop through taskList and print completed tasks
    for title in taskList:
        print('\t {}'.format(title))  # Print each completed task title with indentation

    return 0

if __name__ == '__main__':
    get_employee(argv[1])  # Fetch employee progress using command line argument
