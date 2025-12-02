from datasets.dataset import Dataset

class Graph:
    """
    A mock graph representation linking to a dataset.

    Args:
        dataset (Dataset): The dataset associated with this graph.
        nodes (int): The number of nodes in the graph. Defaults to 10.
    """
    def __init__(self, dataset: Dataset, nodes: int = 10):
        self.dataset = dataset
        self.nodes = nodes
        print(f"Initialized MockGraph(nodes={nodes}) with dataset={dataset.name}")
