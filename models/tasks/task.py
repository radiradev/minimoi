from models.model import Model

class Task:
    """
    A mock task that utilizes a model for a specific objective.

    Args:
        model (Model): The model to be used for the task.
        task_type (str): The type of task (e.g., "interpolator", "forecaster"). Defaults to "forecaster".
    """
    def __init__(self, model: Model, task_type: str = "forecaster"):
        self.model = model
        self.task_type = task_type
        print(f"Initialized MockTask(task_type={task_type})")

    def run(self):
        """Executes the defined task."""
        print("Running MockTask...")
