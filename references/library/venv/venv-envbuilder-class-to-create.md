# venv / API: `venv.EnvBuilder`, `create()`

### API

The high-level approach laid out above relies on a straightforward API offering hooks that let third-party virtual environment builders tailor environment creation to suit themselves, namely the `EnvBuilder` class.

 *class *`venv.EnvBuilder(system_site_packages=False, clear=False, symlinks=False, upgrade=False, with_pip=False, prompt=None, upgrade_deps=False, *, scm_ignore_files=frozenset())`

When you instantiate it, the `EnvBuilder` class takes the keyword arguments listed below:

- *system_site_packages* – a boolean signalling that the environment should have access to the system Python site-packages (the default is `False`).

- *clear* – a boolean that, when true, clears out anything in an existing target directory ahead of building the environment.

- *symlinks* – a boolean signalling whether an attempt should be made to symlink the Python binary in place of copying it.

- *upgrade* – a boolean that, when true, upgrades an existing environment using the running Python — handy once that Python has been upgraded where it sits (the default is `False`).

- *with_pip* – a boolean that, when true, guarantees pip ends up installed in the virtual environment. It relies on [`ensurepip`](https://docs.python.org/3.14/library/ensurepip.html#module-ensurepip) together with the `--default-pip` option.

- *prompt* – a string applied once the virtual environment is active (the default `None` causes the environment’s directory name to be used). Supplying the special string `"."` makes the basename of the current directory serve as the prompt.

- *upgrade_deps* – Bring the base venv modules up to their newest versions on PyPI

- *scm_ignore_files* – Produce ignore files for whichever source control managers (SCM) appear in the iterable. Support comes from having a method called `create_{scm}_ignore_file`. By default the lone supported value is `"git"`, handled through `create_git_ignore_file()`.

Changed in version 3.4: The `with_pip` parameter was introduced

Changed in version 3.6: The `prompt` parameter was introduced

Changed in version 3.9: The `upgrade_deps` parameter was introduced

Changed in version 3.13: The `scm_ignore_files` parameter was introduced

`EnvBuilder` may be used as a base class.

 create(*env_dir*)

Build a virtual environment by naming the target directory (whether absolute or relative to the current directory) that is to hold the virtual environment. The `create` method will either build the environment within the named directory or raise a fitting exception.

The hooks open to subclass customization are demonstrated by the `create` method of the `EnvBuilder` class:

```python
def create(self, env_dir):
    """
    Create a virtualized Python environment in a directory.
    env_dir is the target directory to create an environment in.
    """
    env_dir = os.path.abspath(env_dir)
    context = self.ensure_directories(env_dir)
    self.create_configuration(context)
    self.setup_python(context)
    self.setup_scripts(context)
    self.post_setup(context)

```

Every one of the methods `ensure_directories()`, `create_configuration()`, `setup_python()`, `setup_scripts()` and `post_setup()` is overridable.

[Subject index](INDEX.md) · [Previous](how-venvs-work.md) · [Continue](ensure-directories-to-post-setup.md) · [Owning module, declaration or section: venv](venv-creation-of-virtual-environments.md)
