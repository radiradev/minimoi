import fiddle as fdl
from config import base_config

def main():
    print("--- Building and running Base Config ---")
    cfg = base_config()
    
    # Fiddle allows printing the configuration structure
    print("\n[Configuration Structure]")
    print(cfg) 
    
    # Build the actual Python objects
    trainer = fdl.build(cfg)
    
    # Run the application
    trainer.train()

    print("\n--- Overriding Config (e.g. for experimentation) ---")
    # Example of modifying the config: Change model hidden dimension and epochs
    cfg_experiment = base_config()
    cfg_experiment.task.model.hidden_dim = 256
    cfg_experiment.epochs = 5
    
    # Example: Swap out the dataset config entirely if we had another class
    # cfg_experiment.dataset.name = "experiment_dataset"
    
    trainer_exp = fdl.build(cfg_experiment)
    trainer_exp.train()

if __name__ == "__main__":
    main()