import fiddle as fdl

from datasets.dataset import Dataset
from graphs.graph import Graph
from models.model import Model
from models.tasks.task import Task
from training.trainer import Trainer

def base_config():
    """Defines the base configuration for the training pipeline."""
    
    # 1. Dataset
    dataset = fdl.Config(Dataset, name="my_dataset", size=500)
    
    # 2. Graph
    graph = fdl.Config(Graph, dataset=dataset, nodes=20)
    
    # 3. Model
    model = fdl.Config(Model, graph=graph, hidden_dim=128)
    
    # 4. Task
    task = fdl.Config(Task, model=model, task_type="forecasting")
    
    # 5. Trainer (Top-level object)
    trainer_cfg = fdl.Config(Trainer, task=task, dataset=dataset, epochs=10)
    
    return trainer_cfg
