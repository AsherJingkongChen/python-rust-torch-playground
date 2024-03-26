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

from os import PathLike


def ci(env_dir: PathLike[str] | str | None = None) -> None:
    from x_build_pyo3 import build
    from x_clear import clear
    from x_format import format
    from x_prepare import prepare
    from x_test import test

    clear(env_dir)
    prepare(env_dir)
    # format(env_dir)
    build(env_dir)
    test(env_dir)


if __name__ == "__main__":
    from sys import argv

    env_dir = argv[1] if len(argv) > 1 else None
    ci(env_dir)
