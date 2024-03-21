"""
Construct an isolated environment

## Usage

```python
from util_env import Env
```
"""

from dataclasses import dataclass
from os import PathLike
from pathlib import Path


class Env:
    """
    Python environment builder

    ## Usage
    ```python
    # Construct an isolated environment in Python
    env = Env()

    # Access the environment data
    print(env.data)
    print(env.data.executable)
    ```

    ## Note
    It can only be used in a Python environment.

    To use it in a shell script for development,
    refer to the documentation here:
    https://docs.python.org/3/library/venv.html#how-venvs-work
    """

    def __init__(self, path: PathLike[str] | str | None = None) -> None:
        "Initialize an environment"

        import os
        from shutil import SameFileError
        import site
        import sys
        from venv import EnvBuilder

        # Initialize a virtual environment
        env = EnvBuilder(with_pip=True)
        paths = env.ensure_directories(str(Path(path or Env.DEFAULT_PATH()).absolute()))
        bin_path = str(paths.bin_path)
        env_path = str(paths.env_dir)
        exe_path = str(paths.env_exe)
        try:
            env.create(env_path)
        except SameFileError:
            pass

        # Set data
        self._data = EnvData(
            directory=Path(env_path),
            executable=Path(exe_path),
            installer=Path(bin_path) / "pip",
            path=Path(bin_path),
        )

        # Update environment variables
        # - [how-venv-works](https://docs.python.org/3/library/venv.html#how-venvs-work)
        path_var = bin_path + os.pathsep + os.environ.get("PATH", "")
        os.environ["PATH"] = os.pathsep.join(filter(bool, path_var.split(os.pathsep)))
        os.environ["VIRTUAL_ENV"] = env_path

        # Update site package paths
        # - [site.addsitedir](https://docs.python.org/3/library/site.html#site.addsitedir)
        for package_path in site.getsitepackages([env_path]):
            site.addsitedir(package_path)

        # Update system path prefixes
        # - [sys.*prefix](https://docs.python.org/3/library/sys.html#sys.prefix)
        sys.exec_prefix = sys.prefix = env_path

    def __repr__(self) -> str:
        return self._data.__repr__()

    @staticmethod
    def DEFAULT_PATH() -> Path:
        return Path(".venv")

    @property
    def data(self) -> "EnvData":
        return EnvData(**self._data.__dict__)


@dataclass
class EnvData:
    directory: Path
    """
    The directory of the virtual environment

    ## Example
    ```python
    assert Env().data.dir.name == ".venv"
    ```
    """

    executable: Path
    """
    The path to the Python interpreter

    ## Example
    ```python
    assert Env().data.executable.name.startswith("python")
    ```
    """

    installer: Path
    """
    The path to the installer

    ## Example
    ```python
    assert Env().data.installer.name == "pip"
    ```
    """

    path: Path
    """
    The directory of the executables

    ## Example
    1. On POSIX systems
    ```python
    assert Env().data.path.name == "bin"
    ```
    """
