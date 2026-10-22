# shlex: `shlex.quote()`

`shlex.quote(*s*)`

Produce a shell-escaped rendering of the string *s*. What you get back is a string safe to drop in as a single token on a shell command line, handy whenever a list isn't an option.

Warning

The `shlex` module is **only designed for Unix shells**.

There is no promise that the `quote()` function behaves correctly under shells that aren't POSIX-compliant, nor under shells belonging to other platforms like Windows. Running commands escaped by this module on those shells could expose you to a command injection weakness.

A safer route is to use functions that hand off command arguments as lists, for instance [`subprocess.run()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.run) paired with `shell=False`.

The following idiom is unsafe:

```python
>>> filename = 'somefile; rm -rf ~'
>>> command = 'ls -l {}'.format(filename)
>>> print(command)  # executed by a shell: boom!
ls -l somefile; rm -rf ~

```

Calling `quote()` seals that security gap:

```python
>>> from shlex import quote
>>> command = 'ls -l {}'.format(quote(filename))
>>> print(command)
ls -l 'somefile; rm -rf ~'
>>> remote_command = 'ssh home {}'.format(quote(command))
>>> print(remote_command)
ssh home 'ls -l '"'"'somefile; rm -rf ~'"'"''

```

Such quoting works correctly with UNIX shells as well as with `split()`:

```python
>>> from shlex import split
>>> remote_command = split(remote_command)
>>> remote_command
['ssh', 'home', "ls -l 'somefile; rm -rf ~'"]
>>> command = split(remote_command[-1])
>>> command
['ls', '-l', 'somefile; rm -rf ~']

```

Added in version 3.3.

The `shlex` module defines the following class:

[Subject index](INDEX.md) · [Previous](shlex-split-to-shlex-join.md) · [Continue](shlex-shlex-class.md) · [Owning module, declaration or section: shlex](shlex-split-to-shlex-join.md)
