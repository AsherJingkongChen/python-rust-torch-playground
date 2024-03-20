#! /usr/bin/env python3

"""
# Clear artifacts script

## Usage

```shell
./scripts/clear.py
```
"""


def clear():
    from itertools import chain
    from pathlib import Path
    from shutil import rmtree
    from subprocess import run

    cwd = Path.cwd()
    tasks = chain(())
    tasks = chain(map(rmtree, cwd.glob("**/__pycache__")), tasks)
    tasks = chain(map(Path.unlink, cwd.glob("python/**/*.so")), tasks)
    tasks = chain(map(rmtree, cwd.glob("dist")), tasks)
    tasks = chain(map(rmtree, cwd.glob("target")), tasks)
    tasks = chain(map(run, [("poetry", "env", "remove", "--all")]), tasks)
    list(tasks)


if __name__ == "__main__":
    clear()
