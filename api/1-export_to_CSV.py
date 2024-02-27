import csv
import requests
import sys

def export_to_CSV(sizeofReq):
  """ Export employee's TODO list data to a CSV file """

  # Variables
  allTasks = []  # List to store all tasks data

  link = "https://jsonplaceholder.typicode.com"  # Base URL for the API

  # GET requests to fetch user details and TODO list
  usersRes = requests.get("{}/users/{}".format(link, sizeofReq))
  todosRes = requests.get("{}/users/{}/todos".format(link, sizeofReq))

  # Get the JSON data from responses
  employee_id = usersRes.json().get('id')  # Extract employee ID from user response
  name = usersRes.json().get('username')  # Extract employee username from user response
  todosJson = todosRes.json()  # Extract TODO list JSON data

  # Save the employee data and loop through the tasks to save task data
  for task in todosJson:
    taskRow = []  # List to store data for each task
    taskRow.append(employee_id)  # Add employee ID to task data
    taskRow.append(name)  # Add employee name to task data
    taskRow.append(task.get('completed'))  # Add task completion status to task data
    taskRow.append(task.get('title'))  # Add task title to task data
    allTasks.append(taskRow)  # Append task data to allTasks list

  # Write task data to a CSV file
  with open(f"{employee_id}.csv", "w") as csvFile:
    csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)  # Create a CSV writer object
    csvWriter.writerows(allTasks)  # Write allTasks data to the CSV file

  return 0

if __name__ == '__main__':
  export_to_CSV(int(sys.argv[1]))  # Fetch employee ID from command line argument and export data to CSV 
