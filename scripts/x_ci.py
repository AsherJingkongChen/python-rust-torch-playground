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
"""


def ci():
    from x_build import build
    from x_clear import clear
    from x_prepare import prepare

    clear()
    prepare()
    build()


if __name__ == "__main__":
    ci()
