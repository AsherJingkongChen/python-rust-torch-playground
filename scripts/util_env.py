"""
# Environment setup script

## Usage

```python
from env import env

# Set up the environment
env()
```
"""


def env():
    from pathlib import Path
    from subprocess import run
    from sys import executable

    run(["poetry", "env", "use", executable], check=True)

    virtual_env_path = run(
        ["poetry", "env", "info", "--path"],
        capture_output=True,
        check=True,
        text=True,
    ).stdout.strip()
    activator_path = Path(virtual_env_path) / "bin" / "activate_this.py"

    with open(activator_path, "r") as file:
        exec(file.read(), {"__file__": activator_path})
