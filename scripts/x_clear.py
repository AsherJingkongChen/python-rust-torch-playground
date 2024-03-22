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

from os import PathLike


def clear(env_dir: PathLike[str] | str | None = None) -> None:
    from itertools import chain
    from pathlib import Path
    from shutil import rmtree
    from typing import Iterable
    from u_env import Env

    def remove_paths(*paths: Iterable[Path]) -> None:
        for path in chain(*paths):
            if not path.exists():
                continue
            if path.is_dir():
                rmtree(path)
            else:
                path.unlink()

    cwd = Path.cwd()
    env_dir = Env.resolve_dir(env_dir).relative_to(cwd)
    remove_paths(
        cwd.glob("dist/"),
        cwd.glob("target/"),
        cwd.glob(".pytest_cache/"),
        cwd.glob("python/**/*.so"),
        cwd.glob("**/__pycache__"),
        cwd.glob("{}".format(env_dir)),
    )


if __name__ == "__main__":
    from sys import argv

    clear(argv[1] if len(argv) > 1 else None)
