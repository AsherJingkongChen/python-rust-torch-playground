#! /usr/bin/env python3

"""
Build the project

## Usage

1.
```shell
./scripts/x_build.py
```

2.
```shell
python3 scripts/x_build.py
```
"""


def build():
    from subprocess import run
    from util_env import Env

    python = Env().data.executable

    run([python, "-m", "maturin", "build", "--strip", "--release"], check=True)
    run(
        [python, "-m", "twine", "check", "--strict", "target/wheels/*"],
        check=True,
    )


if __name__ == "__main__":
    build()
