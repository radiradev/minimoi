import fiddle as fdl

from datasets.dataset import MockDataset
from graphs.graph import MockGraph
from models.model import MockModel
from models.tasks.task import MockTask
from training.trainer import MockTrainer

def base_config():
    """Defines the base configuration for the training pipeline."""
    
    # 1. Dataset
    dataset = fdl.Config(MockDataset, name="my_dataset", size=500)
    
    # 2. Graph
    graph = fdl.Config(MockGraph, dataset=dataset, nodes=20)
    
    # 3. Model
    model = fdl.Config(MockModel, graph=graph, hidden_dim=128)
    
    # 4. Task
    task = fdl.Config(MockTask, model=model, task_type="forecasting")
    
    # 5. Trainer (Top-level object)
    trainer_cfg = fdl.Config(MockTrainer, task=task, dataset=dataset, epochs=10)
    
    return trainer_cfg
