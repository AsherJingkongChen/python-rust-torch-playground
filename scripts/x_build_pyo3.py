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
    from subprocess import check_call
    from u_env import Env
    from x_clear import remove_paths

    env = Env(env_dir)
    python = env.data.executable

    remove_paths(get_build_paths())
    check_call(
        [
            python,
            "-m",
            "maturin",
            "build",
            # "--compatibility",
            # "manylinux2014",
            "--out",
            "dist",
            "--release",
            # "--skip-auditwheel",
            "--strip",
        ]
        # + get_build_specfic_options(),
    )


def get_build_paths() -> list[Path]:
    return list(Path("dist").glob("*.whl"))


# def get_build_specfic_options() -> list[str]:
#     from platform import system

#     return ["--zig"] if system() == "Linux" else []


if __name__ == "__main__":
    from sys import argv

    env_dir = argv[1] if len(argv) > 1 else None
    build(env_dir)
