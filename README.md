# Don't get slain by the hydra
A mock package that explores an alternative way of configuration
## Design Philosophy

1. Business Logic (main codebase) is separated from configuration and usable without configs. 
2. Objects are decoupled as much as possible from each other. We stay as close as possible to base pytorch abstractions. 
3. Whenever possible objects allow for users to pass in their own objects.
4. Configuration is still serialisable and can be shared between users to facillitate reproducibility and collaboration between users.
5. Configuration is as Pythonic as possible, and can be de-serialized back to Python objects. 
