#! /usr/bin/env python3

"""
Development (PyO3)

## Usage

1.
```shell
./scripts/x_dev_pyo3.py
```

2.
```shell
python3 scripts/x_dev_pyo3.py
```

## Note
This script will open a Python interpreter.
"""

from os import PathLike


def dev(env_dir: PathLike[str] | str | None = None) -> None:
    from subprocess import check_call
    from u_env import Env

    env = Env(env_dir)
    python = env.data.executable

    check_call([python, "-m", "maturin", "develop", "--skip-install"])
    check_call([python])


if __name__ == "__main__":
    from sys import argv

    env_dir = argv[1] if len(argv) > 1 else None
    dev(env_dir)
