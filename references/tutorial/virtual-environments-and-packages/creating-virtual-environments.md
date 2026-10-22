# 12.2. Creating Virtual Environments

### 12.2. Creating Virtual Environments

The tool that builds and administers virtual environments goes by the name [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv). Whatever Python version launched the command (the one the [`--version`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-version) option reports) is the version `venv` installs. So running it through `python3.12`, say, installs version 3.12.

Begin by picking the directory where the virtual environment should live, then run the [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv) module as a script and hand it that directory path:

```python
python -m venv tutorial-env

```

That creates the `tutorial-env` directory if it isn't already present, and populates it with subdirectories holding a copy of the Python interpreter plus assorted supporting files.

`.venv` is a popular choice of directory for a virtual environment. The name leaves the directory hidden in most shells and therefore out of sight, yet still hints at the directory's purpose. It also steers clear of colliding with `.env` environment-variable definition files that some tools recognize.

With the virtual environment built, your next step is to activate it.

On Windows, run:

```python
tutorial-env\Scripts\activate

```

On Unix or MacOS, run:

```python
source tutorial-env/bin/activate

```

(That script targets the bash shell. Users of the **csh** or **fish** shells have separate `activate.csh` and `activate.fish` scripts to run in its place.)

Activation rewrites your shell prompt to display which virtual environment is in effect, and reconfigures the environment so that invoking `python` lands on that specific Python version and installation. For instance:

```console
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>

```

Keep in mind that activating a virtual environment leaves the `PYTHONPATH` variable entirely untouched. That can produce surprises if the path points at code incompatible with the Python version the virtual environment runs. The recommended habit is to `unset PYTHONPATH` in bash, or the counterpart for whichever shell you run.

To deactivate a virtual environment, type:

```python
deactivate

```

into the terminal.

[Subject index](INDEX.md) · [Previous source section](introduction.md) · [Following source section](virtual-environment-package-lifecycle.md)
