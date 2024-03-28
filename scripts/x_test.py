#! /usr/bin/env python3

"""
Run tests

## Usage

1.
```shell
./scripts/x_test.py
```

2.
```shell
python3 scripts/x_test.py
```
"""

from os import PathLike
from pathlib import Path


def test(env_dir: PathLike[str] | str | None = None) -> None:
    from subprocess import check_call
    from u_env import Env

    env = Env(env_dir)
    python = env.data.executable

    check_call(
        f"{python} -m pytest --capture=no --ignore=*-packages --import-mode=append".split()
        + get_test_paths()
    )


def get_test_paths() -> list[Path]:
    return list(Path().glob("**/__tests__/**/*.py"))


if __name__ == "__main__":
    from sys import argv

    env_dir = argv[1] if len(argv) > 1 else None
    test(env_dir)
