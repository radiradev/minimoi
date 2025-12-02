from models.tasks.task import Task
from datasets.dataset import Dataset

class Trainer:
    """
    A mock trainer responsible for training a task on a dataset.

    Args:
        task (Task): The task to be trained.
        dataset (Dataset): The dataset used for training.
        epochs (int): The number of training epochs. Defaults to 1.
    """
    def __init__(self, task: Task, dataset: Dataset, epochs: int = 1):
        self.task = task
        self.dataset = dataset
        self.epochs = epochs
        print(f"Initialized MockTrainer(epochs={epochs})")

    def train(self):
        """Starts the training loop for the specified number of epochs."""
        print(f"Starting training for {self.epochs} epochs...")
        self.task.run()
        print("Training complete.")
