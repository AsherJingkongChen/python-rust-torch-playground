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
    from itertools import chain
    from pathlib import Path
    from subprocess import run
    from u_env import Env

    env = Env(env_dir)
    venv = env.data.directory
    pip = env.data.installer
    python = env.data.executable
    build_dir = Path("target/wheels")
    build_paths = list(chain(build_dir.glob("*.tar.gz"), build_dir.glob("*.whl")))
    test_paths = list(
        filter(lambda p: venv not in p.parents, Path.cwd().glob("**/tests/**/*.py"))
    )

    run([pip, "install"] + build_paths, check=True)
    run(
        [python, "-m", "pytest", "--capture", "no", "--import-mode", "append"]
        + test_paths,
        check=True,
    )


if __name__ == "__main__":
    from sys import argv

    env_dir = argv[1] if len(argv) > 1 else None
    test(env_dir)
