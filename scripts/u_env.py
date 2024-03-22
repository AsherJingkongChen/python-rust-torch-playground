"""
Construct an isolated environment

## Usage

```python
from u_env import Env
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

    _ENVIRONMENTS = {}

    def __init__(self, env_dir: PathLike[str] | str | None = None) -> None:
        """
        Initialize an environment

        ## Parameters
        - `env_dir` (`PathLike[str] | str | None` = `None`):
            - Path to the environment directory

        ## Note
        The created environment will be cached for reuse.
        """

        from os import environ, pathsep
        from shutil import SameFileError
        from site import addsitepackages
        import sys
        from venv import EnvBuilder

        # Convert parameters
        env_dir = Env.resolve_dir(env_dir)

        # Check if the environment already exists
        old_env = Env._ENVIRONMENTS.get(env_dir)
        if old_env:
            self._data = old_env._data
            return

        # Initialize a virtual environment
        env = EnvBuilder(with_pip=True)
        paths = env.ensure_directories(str(env_dir))
        bin_path = str(paths.bin_path)
        env_path = str(paths.env_dir)
        exe_path = str(paths.env_exe)
        try:
            env.create(env_path)
        except SameFileError:
            # The error may occur if the environment already exists,
            # just ignore it.
            pass

        # Update environment variables
        # - [how-venv-works](https://docs.python.org/3/library/venv.html#how-venvs-work)
        path_var = bin_path + pathsep + environ.get("PATH", "")
        environ["PATH"] = pathsep.join(filter(bool, path_var.split(pathsep)))
        environ["VIRTUAL_ENV"] = env_path

        # Update site package paths
        # - [site.addsitedir](https://docs.python.org/3/library/site.html#site.addsitedir)
        # - [site.getsitepackages](https://docs.python.org/3/library/site.html#site.getsitepackages)
        addsitepackages(known_paths=None, prefixes=[env_path])

        # Update system path prefixes
        # - [sys.*prefix](https://docs.python.org/3/library/sys.html#sys.prefix)
        sys.exec_prefix = sys.prefix = env_path

        # Set data
        self._data = EnvData(
            directory=Path(env_path),
            executable=Path(exe_path),
            path=Path(bin_path),
        )

        # Record the environment
        Env._ENVIRONMENTS[self._data.directory] = self

        # Show post-init message
        print(
            f'A Python environment has initialized at "{self._data.directory}"',
            file=sys.stderr,
        )

    def __repr__(self) -> str:
        return self._data.__repr__()

    @staticmethod
    def resolve_dir(env_dir: PathLike[str] | str | None) -> Path:
        "Resolve the environment directory"
        return Path(env_dir or Env.DEFAULT_PATH()).resolve()

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

    path: Path
    """
    The directory of the executables

    ## Example
    1. On POSIX systems
    ```python
    assert Env().data.path.name == "bin"
    ```
    
    2. On NT systems
    ```python
    assert Env().data.path.name == "Scripts"
    ```
    """
