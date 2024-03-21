#! /usr/bin/env python3

"""
Clear artifacts

## Usage

1.
```shell
./scripts/x_clear.py
```

2.
```shell
python3 scripts/x_clear.py
```
"""


def clear():
    from itertools import chain
    from pathlib import Path
    from shutil import rmtree
    from typing import Iterable

    def remove_paths(*paths: Iterable[Path]) -> None:
        for path in chain(*paths):
            if not path.exists():
                continue
            if path.is_dir():
                rmtree(path)
            else:
                path.unlink()

    cwd = Path.cwd()
    remove_paths(
        cwd.glob("python/**/*.so"),
        cwd.glob("**/__pycache__"),
        cwd.glob("target/"),
        cwd.glob(".venv/"),
    )


if __name__ == "__main__":
    clear()
