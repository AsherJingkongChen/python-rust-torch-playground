#! /usr/bin/env python3

"""
Prepare the project

## Usage

1.
```shell
./scripts/x_prepare.py
```

2.
```shell
python3 scripts/x_prepare.py
```
"""

from os import PathLike


def prepare(env_dir: PathLike[str] | str | None = None) -> None:
    from subprocess import run
    from u_env import Env

    env = Env(env_dir)
    python = env.data.executable

    run([python, "-m", "pip", "install", "-r", "requirements.txt"], check=True)


if __name__ == "__main__":
    from sys import argv

    env_dir = argv[1] if len(argv) > 1 else None
    prepare(env_dir)
