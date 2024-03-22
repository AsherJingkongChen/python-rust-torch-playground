#! /usr/bin/env python3

"""
Development (PyO3)

## Usage

1.
```shell
./scripts/x_dev.py
```

2.
```shell
python3 scripts/x_dev.py
```

## Note
This script will open a Python interpreter.
"""

from os import PathLike


def dev(env_dir: PathLike[str] | str | None = None) -> None:
    from subprocess import run
    from u_env import Env

    env = Env(env_dir)
    python = env.data.executable

    run([python, "-m", "maturin", "develop", "--skip-install"], check=True)
    run([python], check=True)


if __name__ == "__main__":
    from sys import argv

    env_dir = argv[1] if len(argv) > 1 else None
    dev(env_dir)
