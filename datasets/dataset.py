
class Dataset:
    """
    A mock dataset class for demonstration purposes.

    Args:
        name (str): The name of the dataset.
        size (int): The number of samples in the dataset.
    """
    def __init__(self, name: str, size: int = 100):
        self.name = name
        self.size = size
        print(f"Initialized MockDataset(name={name}, size={size})")

    def __len__(self):
        return self.size
