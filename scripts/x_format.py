#! /usr/bin/env python3

"""
Format source codes

## Usage

1.
```shell
./scripts/x_format.py
```

2.
```shell
python3 scripts/x_format.py
```
"""


def format():
    from subprocess import run
    from u_env import Env

    python = Env().data.executable

    run([python, "-m", "black", "--line-length", "80", "."], check=True)


if __name__ == "__main__":
    format()
