#! /usr/bin/env python3

"""
# Preparation script

## Usage

```shell
./scripts/prepare.py
```
"""


def prepare():
    from subprocess import run
    from util_env import env

    env()
    run(["poetry", "install"], check=True)


if __name__ == "__main__":
    prepare()
