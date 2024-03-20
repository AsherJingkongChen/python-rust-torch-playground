#! /usr/bin/env python3

"""
# Development script

## Usage

```shell
./scripts/dev.py
```
"""


def dev():
    from subprocess import run
    from util_env import env

    env()
    run(["python3", "-m", "maturin", "develop"], check=True)
    run(["python3"], check=True)


if __name__ == "__main__":
    dev()
