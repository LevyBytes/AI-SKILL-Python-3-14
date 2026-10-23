# What’s New in Python 2.4 / PEP 324: New subprocess Module - os, subprocess

### PEP 324: New subprocess Module

A variety of mechanisms for launching a subprocess come with the standard library, each offering its own features and its own degree of complexity. Though `os.system(command)` is simple to call, it’s slow (a shell process gets spun up to run the command) and risky (you must take care to escape the shell’s metacharacters). The `popen2` module supplies classes that grab a subprocess’s standard output and standard error, but the naming is muddled. By tidying all this up, the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module delivers one consistent interface carrying every feature you’re likely to want.

In place of the assortment of classes from `popen2`, the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module holds a lone class named [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen), whose constructor accepts a range of different keyword arguments.

```python
class Popen(args, bufsize=0, executable=None,
            stdin=None, stdout=None, stderr=None,
            preexec_fn=None, close_fds=False, shell=False,
            cwd=None, env=None, universal_newlines=False,
            startupinfo=None, creationflags=0):

```

Usually *args* is a sequence of strings serving as the arguments to the program that runs as the subprocess. (When the *shell* argument is true, *args* may be a single string, which then gets forwarded to the shell to interpret, much as [`os.system()`](https://docs.python.org/3.14/library/os.html#os.system) does.)

What the subprocess uses for its input, output, and error streams gets set by *stdin*, *stdout*, and *stderr*. You can hand over a file object or a file descriptor, or you can supply the constant `subprocess.PIPE` to open a pipe linking the subprocess and its parent.

A handful of convenient options come with the constructor:

- When *close_fds* is set, it asks that every file descriptor be shut before the subprocess runs.

- The *cwd* setting names the working directory the subprocess will run inside (falling back to whatever the parent’s working directory happens to be).

- A dictionary that lays out environment variables is what *env* holds.

- A function that runs right before the child launches is what *preexec_fn* provides.

- By setting *universal_newlines*, the child’s input and output are opened through Python’s [universal newlines](https://docs.python.org/3.14/glossary.html#term-universal-newlines) feature.

After the `Popen` instance exists, you can invoke its `wait()` method to block until the subprocess finishes, `poll()` to test whether it has finished without blocking, or `communicate(data)` to push the string *data* into the subprocess’s standard input. `communicate(data)` then collects whatever data the subprocess emitted on its standard output or standard error, handing back a tuple `(stdout_data, stderr_data)`.

As a shortcut, `call()` forwards its arguments to the `Popen` constructor, holds until the command finishes, and gives back the subprocess’s status code. You can treat it as a safer counterpart to [`os.system()`](https://docs.python.org/3.14/library/os.html#os.system):

```python
sts = subprocess.call(['dpkg', '-i', '/tmp/new-package.deb'])
if sts == 0:
    # Success
    ...
else:
    # dpkg returned an error
    ...

```

No shell takes part when the command runs. If using the shell really is what you want, you can tack on `shell=True` as a keyword argument and pass a string rather than a sequence:

```python
sts = subprocess.call('dpkg -i /tmp/new-package.deb', shell=True)

```

Through a range of shell and Python code samples, the PEP demonstrates how each would be rewritten into Python code built on [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess). Working through that part of the PEP comes highly recommended.

See also

[**PEP 324**](https://peps.python.org/pep-0324/) - subprocess - New process module

Authored and built by Peter Åstrand, with help from Fredrik Lundh among others.

[Subject index](INDEX.md) · [Previous source section](pep-322-reverse-iteration.md) · [Next source section](pep-327-decimal-data-type.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)
