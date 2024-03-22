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

## Note
This script eases the process of continuous integration.
"""


def ci():
    from x_build import build
    from x_clear import clear
    from x_format import format
    from x_prepare import prepare
    from x_test import test

    clear()
    prepare()
    format()
    build()
    test()

    # run([python, "scripts/x_clear.py"], check=True)
    # run([python, "scripts/x_prepare.py"], check=True)
    # run([python, "scripts/x_format.py"], check=True)
    # run([python, "scripts/x_build.py"], check=True)
    # run([python, "scripts/x_test.py"], check=True)


if __name__ == "__main__":
    ci()
