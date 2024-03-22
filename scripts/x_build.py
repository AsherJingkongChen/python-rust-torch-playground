#! /usr/bin/env python3

"""
Build the project

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


def build(env_dir: PathLike[str] | str | None = None) -> None:
    from subprocess import run
    from u_env import Env

    env = Env(env_dir)
    python = env.data.executable

    run([python, "-m", "maturin", "build", "--strip", "--release"], check=True)
    run(
        [python, "-m", "twine", "check", "--strict", "target/wheels/*.*"],
        check=True,
    )


if __name__ == "__main__":
    from sys import argv

    env_dir = argv[1] if len(argv) > 1 else None
    build(env_dir)
