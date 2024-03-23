#! /usr/bin/env python3

"""
Build the project (PyO3)

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

from os import PathLike
from pathlib import Path


def build(env_dir: PathLike[str] | str | None = None) -> None:
    from pathlib import Path
    from subprocess import run
    from u_env import Env

    env = Env(env_dir)
    python = env.data.executable

    list(map(Path.unlink, get_build_paths()))
    run(
        [
            python,
            "-m",
            "maturin",
            "build",
            "--compatibility",
            "linux",
            "--release",
            "--strip",
            "--out",
            "dist",
        ],
        check=True,
    )
    run(
        [python, "-m", "twine", "check", "--strict"] + get_build_paths(),
        check=True,
    )


def get_build_paths() -> list[Path]:
    return list(Path("dist").glob("*.whl"))


if __name__ == "__main__":
    from sys import argv

    env_dir = argv[1] if len(argv) > 1 else None
    build(env_dir)
