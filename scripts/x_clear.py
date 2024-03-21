#! /usr/bin/env python3

"""
Clear artifacts

## Usage

1.
```shell
./scripts/x_clear.py
```

2.
```shell
python3 scripts/x_clear.py
```
"""


def clear():
    from itertools import chain
    from pathlib import Path
    from shutil import rmtree

    cwd = Path.cwd()
    tasks = chain(())
    tasks = chain(map(Path.unlink, cwd.glob("python/**/*.so")), tasks)
    tasks = chain(map(rmtree, cwd.glob("**/__pycache__")), tasks)
    tasks = chain(map(rmtree, cwd.glob("target")), tasks)
    tasks = chain(map(rmtree, cwd.glob(".venv")), tasks)

    list(tasks)


if __name__ == "__main__":
    clear()
