import requests
import json



response = requests.get('https://jsonplaceholder.typicode.com/todos')

obj =response.json()

selected_todos=[]

for todo in obj:
    if todo["completed"] == False:
        selected_todos.append(todo)

with open("todos.json",'w') as f:
    pass

for todo in selected_todos:        
    with open('todos.json.','a') as f:
        json.dump(todo,f,indent=4)
