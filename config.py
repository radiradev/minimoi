import fiddle as fdl
from fiddle.experimental import auto_config
from fiddle.codegen import codegen
from fiddle import printing

from datasets.dataset import Dataset
from graphs.graph import Graph
from models.model import Model
from models.tasks.task import Task
from training.trainer import Trainer

@auto_config.auto_config
def make_trainer():
    """Creates a trainer.
    """
    dataset = Dataset(name="era", size=1000)
    # change the dataset to wrong type on purpose to trigger type checking error
    #dataset = 'ooops'
    graph = Graph(dataset=dataset, nodes=15)

    model = Model(graph=graph, hidden_dim=64)
    task = Task(model=model, task_type="classifier")
    trainer = Trainer(task=task, dataset=dataset, epochs=5)
    return trainer


cfg = make_trainer.as_buildable()
print(printing.as_str_flattened(cfg))


generated = codegen.codegen_dot_syntax(cfg)
print("\n".join(generated.lines()))