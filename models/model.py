from graphs.graph import MockGraph

class Model:
    def __init__(self, graph: MockGraph, hidden_dim: int = 64):
        self.graph = graph
        self.hidden_dim = hidden_dim
        print(f"Initialized MockModel(hidden_dim={hidden_dim}) with graph linked to {graph.dataset.name}")

    def forward(self, x):
        return x
