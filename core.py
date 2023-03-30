import json


class Task:
    def __init__(self, title, content, priority):
        self.title = title
        self.content = content
        self.priority = priority


class TaskManager:
    def __init__(self):
        self.file = 'tasks.json'
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load a task list"""
        with open(self.file, 'r') as file:
            tasks = json.load(file)
            return tasks

    def save_tasks(self):
        """Save task list"""
        with open(self.file, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def create_task(self, title, content, priority):
        """Create a new task."""
        task = Task(title, content, priority)
        self.tasks.append(task.__dict__)
        self.save_tasks()

    def read_task(self, title):
        """Read a task by title."""
        for task in self.tasks:
            if task['title'] == title:
                return task
        raise ValueError(f"No task with title '{title}' found.")

    def update_task(self, title, new_title=None, new_content=None,
                    new_priority=None):
        """Update a task by title."""
        for task in self.tasks:
            if task['title'] == title:
                if new_title:
                    task['title'] = new_title
                if new_content:
                    task['content'] = new_content
                if new_priority:
                    task['priority'] = new_priority
                self.save_tasks()
                return
        raise ValueError(f"No task with title '{title}' found.")

    def delete_task(self, title):
        """Delete a task by title."""
        for task in self.tasks:
            if task['title'] == title:
                self.tasks.remove(task)
                self.save_tasks()
                return
        raise ValueError(f"No task with title '{title}' found.")

    def list_tasks(self):
        """List all tasks, sorted by priority."""
        return self.tasks
