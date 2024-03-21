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


def test():
    from pathlib import Path
    from subprocess import run
    from util_env import Env

    env = Env().data
    pip = env.installer
    python = env.executable

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
    test()
