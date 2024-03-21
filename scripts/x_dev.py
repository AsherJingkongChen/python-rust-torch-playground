#! /usr/bin/env python3

"""
Development

## Usage

1.
```shell
./scripts/x_dev.py
```

2.
```shell
python3 scripts/x_dev.py
```
"""


def dev():
    from subprocess import run
    from u_env import Env

    python = Env().data.executable

    run([python, "-m", "maturin", "develop", "--skip-install"], check=True)
    run([python], check=True)


if __name__ == "__main__":
    dev()
