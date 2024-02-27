import csv
import requests
import sys

def export_to_CSV(employee_id):
    """ Export employee's TODO list data to a CSV file """

    # Variables
    allTasks = []  # List to store all tasks data

    link = "https://jsonplaceholder.typicode.com"  # Base URL for the API

    # GET requests to fetch user details and TODO list
    usersRes = requests.get("{}/users/{}".format(link, employee_id))
    todosRes = requests.get("{}/users/{}/todos".format(link, employee_id))

    # Get the JSON data from responses
    employee_data = usersRes.json()  # Extract employee data
    todosJson = todosRes.json()  # Extract TODO list JSON data

    # Save the employee data and loop through the tasks to save task data
    for task in todosJson:
        taskRow = [employee_data['id'], employee_data['username'], task.get('completed'), task.get('title')]
        allTasks.append(taskRow)  # Append task data to allTasks list

    # Write task data to a CSV file
    filename = f"{employee_id}.csv"
    with open(filename, "w", newline='') as csvFile:
        csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)  # Create a CSV writer object
        csvWriter.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])  # Write header
        csvWriter.writerows(allTasks)  # Write allTasks data to the CSV file

    return filename, len(allTasks)  # Return filename and number of tasks

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    csv_filename, num_tasks = export_to_CSV(employee_id)
    print(f"CSV file '{csv_filename}' created with {num_tasks} tasks.")
