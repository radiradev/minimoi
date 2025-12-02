from models.tasks.task import Task
from datasets.dataset import Dataset

class Trainer:
    def __init__(self, task: Task, dataset: Dataset, epochs: int = 1):
        self.task = task
        self.dataset = dataset
        self.epochs = epochs
        print(f"Initialized MockTrainer(epochs={epochs})")

    def train(self):
        print(f"Starting training for {self.epochs} epochs...")
        self.task.run()
        print("Training complete.")
