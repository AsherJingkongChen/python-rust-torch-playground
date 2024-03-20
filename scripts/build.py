#! /usr/bin/env python3

"""
# Build script

## Usage

```shell
./scripts/build.py
```
"""


def build():
    from subprocess import run
    from util_env import env

    env()
    run(["python3", "-m", "maturin", "build"], check=True)


if __name__ == "__main__":
    build()
