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


def test(env_dir: PathLike[str] | str | None = None) -> None:
    from pathlib import Path
    from subprocess import run
    from u_env import Env

    env = Env(env_dir)
    pip = env.data.installer
    python = env.data.executable

    run([pip, "install"] + list(Path("target/wheels").glob("*.*")), check=True)
    run(
        [
            python,
            "-m",
            "pytest",
            "--capture",
            "no",
            "--import-mode",
            "append",
        ]
        + list(Path("python/tests").glob("*.py")),
        check=True,
    )


if __name__ == "__main__":
    from sys import argv

    env_dir = argv[1] if len(argv) > 1 else None
    test(env_dir)
