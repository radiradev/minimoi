from models.model import Model

class Task:
    def __init__(self, model: Model, task_type: str = "prediction"):
        self.model = model
        self.task_type = task_type
        print(f"Initialized MockTask(task_type={task_type})")

    def run(self):
        print("Running MockTask...")
