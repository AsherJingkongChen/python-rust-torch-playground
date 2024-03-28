#! /usr/bin/env python3

"""
Build the project (PyO3)

## Usage

1.
```shell
./scripts/x_build_pyo3.py
```

2.
```shell
python3 scripts/x_build_pyo3.py
```
"""

from os import PathLike
from pathlib import Path


def build(env_dir: PathLike[str] | str | None = None) -> None:
    from subprocess import check_call
    from u_env import Env
    from x_clear import remove_paths

    env = Env(env_dir)
    python = env.data.executable

    remove_paths(get_build_paths())
    check_call(
        f"{python} -m maturin build --compatibility=manylinux2014 --future-incompat-report --out=dist --release --skip-auditwheel --strip".split()
    )
    remove_paths(get_build_temp_paths())
    check_call(f"{python} -m twine check --strict".split() + get_build_paths())
    check_call(
        f"{python} -m pip install --force-reinstall --no-deps".split()
        + get_build_paths()
    )


def get_build_paths() -> list[Path]:
    return list(Path("dist").glob("*"))


def get_build_temp_paths() -> list[Path]:
    return list(Path().glob("build"))


if __name__ == "__main__":
    from sys import argv

    env_dir = argv[1] if len(argv) > 1 else None
    build(env_dir)
