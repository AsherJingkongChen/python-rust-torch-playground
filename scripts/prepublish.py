#! /usr/bin/env python3

"""
# Pre-publish script

## Usage

```shell
./scripts/prepublish.py
```
"""


def prepublish():
    from subprocess import run

    run(["poetry", "lock"], check=True)
    run(["poetry", "export", "--output", "requirements.txt"], check=True)


if __name__ == "__main__":
    prepublish()
