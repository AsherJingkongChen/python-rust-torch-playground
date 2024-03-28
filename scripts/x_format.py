#! /usr/bin/env python3

"""
Format source codes

## Usage

1.
```shell
./scripts/x_format.py
```

2.
```shell
python3 scripts/x_format.py
```
"""


from os import PathLike


def format(env_dir: PathLike[str] | str | None = None) -> None:
    from subprocess import check_call
    from u_env import Env

    env = Env(env_dir)
    python = env.data.executable

    check_call(f"{python} -m black --line-length=80 .".split())


if __name__ == "__main__":
    from sys import argv

    env_dir = argv[1] if len(argv) > 1 else None
    format(env_dir)
