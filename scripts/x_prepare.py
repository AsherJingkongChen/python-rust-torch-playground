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


def prepare():
    from subprocess import run
    from util_env import Env

    pip = Env().data.installer

    run([pip, "install", "-r", "requirements.txt"], check=True)


if __name__ == "__main__":
    prepare()
