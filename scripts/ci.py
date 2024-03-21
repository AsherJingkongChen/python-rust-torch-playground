#! /usr/bin/env python3

"""
Continuous Integration

## Usage

1.
```shell
./scripts/build.py
```

2.
```shell
python3 scripts/build.py
```
"""


def build():
    from subprocess import run
    from util_env import Env

    python = Env().data.executable
    run([python, "-m", "maturin", "build", "--strip", "--release"], check=True)


if __name__ == "__main__":
    build()
