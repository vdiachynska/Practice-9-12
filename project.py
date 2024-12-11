class Task:

    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self. status = status

    def __repr__(self):
        return f"Task title: {self.title}, Description: {self.description}, Status: {self.status}"

class Project:
    tasks = []

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def add_task(self, task, description, status):
        Project.tasks.append(Task(task, description, status))

    def remove_task(self, task):
        for i in Project.tasks:
            if i.title == task:
                obj = i
        Project.tasks.remove(obj)

    def get_task_status(self, task):
        for i in Project.tasks:
            if i.title == task:
                obj = i
        return obj.status

    def update_task_status(self, task, new_status):
        for i in Project.tasks:
            if i.title == task:
                i.status = new_status

    def get_tasks_by_status(self, status):
        list_by_status= []
        for i in Project.tasks:
            if i.status == status:
                list_by_status.append(i.title)
        return list_by_status

    def print_tasks(self):
        for i in Project.tasks:
            print(i)

project = Project("Website Redesign", "A project for redesigning the company website")
project.add_task("Design Layout", "Create a layout for the new website", "Planned")
project.add_task("Develop Homepage", "Develop the homepage of the website", "In progress")
project.update_task_status("Design Layout", "Completed")
project.add_task("Design AI asistant", "Create a wrapper for the assistant", "Completed")
project.add_task("Design intro", "Create a welcome page", "In progress")
project.print_tasks()

print(project.get_tasks_by_status('In progress'))
print(project.get_task_status('Design Layout'))
project.remove_task("Design intro")
project.print_tasks()
