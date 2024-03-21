#! /usr/bin/env python3

"""
Continuous Integration

## Usage

1.
```shell
./scripts/x_ci.py
```

2.
```shell
python3 scripts/x_ci.py
```

## Description
This script eases the process of continuous integration.
"""


def ci():
    from subprocess import run
    from sys import executable as python

    run([python, "scripts/x_clear.py"], check=True)
    run([python, "scripts/x_prepare.py"], check=True)
    run([python, "scripts/x_format.py"], check=True)
    run([python, "scripts/x_build.py"], check=True)
    run([python, "scripts/x_test.py"], check=True)

if __name__ == "__main__":
    ci()
