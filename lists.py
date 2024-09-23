import json
import os

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description, deadline=None):
        task = {"description": description, "deadline": deadline, "completed": False}
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        for idx, task in enumerate(self.tasks):
            print(f"{idx+1}. {task['description']} - {'Done' if task['completed'] else 'Pending'}")

    def update_task(self, index, description=None, deadline=None, completed=None):
        if 0 <= index < len(self.tasks):
            if description:
                self.tasks[index]["description"] = description
            if deadline:
                self.tasks[index]["deadline"] = deadline
            if completed is not None:
                self.tasks[index]["completed"] = completed
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

