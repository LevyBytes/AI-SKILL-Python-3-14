# subprocess - Popen Constructor - Signature and initial contract

*class *subprocess.Popen(*args*, *bufsize=-1*, *executable=None*, *stdin=None*, *stdout=None*, *stderr=None*, *preexec_fn=None*, *close_fds=True*, *shell=False*, *cwd=None*, *env=None*, *universal_newlines=None*, *startupinfo=None*, *creationflags=0*, *restore_signals=True*, *start_new_session=False*, *pass_fds=()*, ***, *group=None*, *extra_groups=None*, *user=None*, *umask=-1*, *encoding=None*, *errors=None*, *text=None*, *pipesize=-1*, *process_group=None*)

Run a child program inside a new process. Under POSIX, the class relies on behavior resembling [`os.execvpe()`](https://docs.python.org/3.14/library/os.html#os.execvpe) to run the child program. Under Windows, it calls the Windows `CreateProcess()` function. Here are the arguments to `Popen`.

*args* should be either a sequence of program arguments, or else a lone string or [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object). When *args* is a sequence, the program that runs is by default its first item. When *args* is a string, how it is read depends on the platform and is covered below. Consult the *shell* and *executable* arguments for further departures from the default behavior. Barring a note to the contrary, passing *args* as a sequence is the recommended approach.

Warning

To be as reliable as possible, give the executable a fully qualified path. When you want an unqualified name looked up on `PATH`, use [`shutil.which()`](https://docs.python.org/3.14/library/shutil.html#shutil.which). Across every platform, handing in [`sys.executable`](https://docs.python.org/3.14/library/sys.html#sys.executable) is the recommended way to start the running Python interpreter over again, paired with the `-m` command-line form to start an installed module.

How the path of *executable* (or of the first item in *args*) gets resolved depends on the platform. Under POSIX, see [`os.execvpe()`](https://docs.python.org/3.14/library/os.html#os.execvpe), and keep in mind that, while the executable path is being resolved or searched for, *cwd* overrides the current working directory and *env* is able to override the `PATH` environment variable. Under Windows, see the documentation covering the `lpApplicationName` and `lpCommandLine` parameters of WinAPI `CreateProcess`, and keep in mind that, when the executable path is resolved or searched for using `shell=False`, neither does *cwd* take precedence over the current working directory nor can *env* supplant the `PATH` environment variable. Supplying a full path sidesteps all of these differences.

Here is how you might hand a few arguments to an outside program in sequence form:

```python
Popen(["/usr/bin/git", "commit", "-m", "Fixes a bug."])

```

Under POSIX, when *args* is a string, that string is read as the name or path of the program you want to run. This is only possible, however, when you aren't passing any arguments along to the program.

Note

Splitting a shell command into a sequence of arguments isn't always obvious, particularly in tricky cases. [`shlex.split()`](https://docs.python.org/3.14/library/shlex.html#shlex.split) can demonstrate how the proper tokenization of *args* is worked out:

```python
>>> import shlex, subprocess
>>> command_line = input()
/bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"
>>> args = shlex.split(command_line)
>>> print(args)
['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]
>>> p = subprocess.Popen(args) # Success!

```

Take special note that options (like *-input*) along with arguments (like *eggs.txt*) which the shell separates by whitespace become distinct list elements, whereas arguments that demand quoting or backslash escaping in the shell (like filenames carrying spaces, or the *echo* command above) form single list elements.

Under Windows, when *args* is a sequence, it gets turned into a string in the way laid out under Converting an argument sequence to a string on Windows. The reason is that the underlying `CreateProcess()` works on strings.

Changed in version 3.6: On POSIX, the *args* parameter takes a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) when *shell* is `False`, as well as a sequence holding path-like objects.

Changed in version 3.8: On Windows, the *args* parameter takes a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object) when *shell* is `False`, as well as a sequence holding bytes and path-like objects.

The *shell* argument (whose default is `False`) controls whether the shell itself serves as the program to run. With *shell* set to `True`, passing *args* as a string instead of a sequence is the recommended approach.

Under POSIX with `shell=True`, the shell falls back to `/bin/sh`. When *args* is a string, that string spells out the command to run through the shell. So the string has to be laid out precisely the way it would be if typed at the shell prompt. That covers, for example, quoting or backslash escaping filenames that contain spaces. When *args* is a sequence, its first item spells out the command string, while any further items get handled as extra arguments to the shell itself. Put another way, `Popen` carries out the equivalent of:

```python
Popen(['/bin/sh', '-c', args[0], args[1], ...])

```

Under Windows with `shell=True`, the default shell is named by the `COMSPEC` environment variable. The sole occasion you have to set `shell=True` on Windows is when the command you intend to run is built into the shell itself (for instance **dir** or **copy**). Running a batch file or a console-based executable does not require `shell=True`.

Note

Read the Security Considerations section before using `shell=True`.

*bufsize* is forwarded as the matching argument to the [`open()`](https://docs.python.org/3.14/library/functions.html#open) function while the stdin/stdout/stderr pipe file objects are being created:

- `0` selects unbuffered operation (a single read and a single write are each one system call, and short returns are possible)

- `1` selects line buffering (available only when `text=True` or `universal_newlines=True`)

- any other positive number selects a buffer roughly of that size

- a negative bufsize (the default) selects the system default, namely io.DEFAULT_BUFFER_SIZE.

Changed in version 3.3.1: *bufsize* defaults to -1 these days, turning on buffering by default so the behavior lines up with what the bulk of code anticipates. Before Python 3.2.4 and 3.3.1, the default was mistakenly `0`, which was unbuffered and permitted short reads. That outcome was accidental, and it failed to line up with how Python 2 behaved, which is what the bulk of code anticipated.

The *executable* argument names a substitute program to run. It is needed only on rare occasions. With `shell=False`, *executable* stands in for the program to run that *args* designates. Even so, the original *args* still reaches the program. Most programs read the program designated by *args* as the command name, and that can differ from the program actually run. Under POSIX, the *args* name turns into the display name for the executable in tools such as **ps**. With `shell=True`, under POSIX the *executable* argument names a substitute shell in place of the default `/bin/sh`.

Changed in version 3.6: On POSIX, the *executable* parameter takes a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Subject index](INDEX.md) · [Previous](popen-constructor.md) · [Continue](windows-executable-bytes-and-pathlike-support.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md) · [Owning module, declaration or section: Popen Constructor](popen-constructor.md)
