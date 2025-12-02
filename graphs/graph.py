from datasets.dataset import Dataset

class Graph:
    def __init__(self, dataset: Dataset, nodes: int = 10):
        self.dataset = dataset
        self.nodes = nodes
        print(f"Initialized MockGraph(nodes={nodes}) with dataset={dataset.name}")
