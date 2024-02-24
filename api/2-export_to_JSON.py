import requests
import sys
from sys import argv  # Importing argv from sys module
import json

def export_to_JSON(employee_id):
    """ Export employee's TODO list data to a JSON file """

    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # GET requests to fetch user details and TODO list
    users_response = requests.get(f"{base_url}/users/{employee_id}")
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")

    # Extract JSON data from responses
    user_data = users_response.json()
    todos_data = todos_response.json()

    # Extract user information
    user_id = user_data['id']
    username = user_data['username']

    # Prepare dictionary to store task data
    tasks_dict = {"USER_ID": [], "username": username}

    # Iterate over todo items and extract relevant information
    for todo in todos_data:
        task_title = todo['title']
        task_completed_status = todo['completed']
        task_dict = {"task": task_title, "completed": task_completed_status, "username": username}
        tasks_dict["USER_ID"].append(task_dict)

    # Write task data to a JSON file
    filename = f"{user_id}.json"
    with open(filename, "w") as json_file:
        json.dump(tasks_dict, json_file, indent=4)

    print(f"JSON file '{filename}' created successfully.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_JSON(employee_id)
