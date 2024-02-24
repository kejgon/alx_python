import requests
import sys

def check_tasks(id):
    """ Fetch user name, number of tasks """
    
    # Fetch user name
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    user_data = user_response.json()
    username = user_data['name']
    
    # Fetch tasks
    tasks_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}/todos')
    tasks_data = tasks_response.json()
    total_tasks = len(tasks_data)
    completed_tasks = sum(1 for task in tasks_data if task['completed'])

    print(f"Employee {username} is done with tasks({completed_tasks}/{total_tasks}):")

    # Print titles of completed tasks and check formatting
    for count, task in enumerate(tasks_data, start=1):
        if task['completed']:
            if task['title'].startswith('\t ') and task['title'].endswith('\n'):
                print(f"\t{task['title']}")
                print(f"Task {count} Formatting: OK")
            else:
                print(f"Task {count} Formatting: Incorrect")
        else:
            print(f"Task {count} Formatting: OK")

if __name__ == "__main__":
    check_tasks(int(sys.argv[1]))
