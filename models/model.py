from graphs.graph import Graph

class Model:
    """
    A mock model that operates on a graph structure.

    Args:
        graph (Graph): The graph structure used by the model.
        hidden_dim (int): The size of the hidden layers. Defaults to 64.
    """
    def __init__(self, graph: Graph, hidden_dim: int = 64):
        self.graph = graph
        self.hidden_dim = hidden_dim
        print(f"Initialized MockModel(hidden_dim={hidden_dim}) with graph linked to {graph.dataset.name}")

    def forward(self, x):
        """
        Performs a forward pass of the model.

        Args:
            x (Any): The input data.

        Returns:
            Any: The input data (identity function for mock purposes).
        """
        return x
