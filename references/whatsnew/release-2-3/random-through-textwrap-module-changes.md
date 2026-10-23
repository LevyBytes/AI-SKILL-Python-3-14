# What’s New in Python 2.3 / New, Improved, and Deprecated Modules - random, readline, shutil, signal, socket, tarfile, textwrap

```python
>>> days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'St', 'Sn']
>>> random.sample(days, 3)      # Choose 3 elements
['St', 'Sn', 'Th']
>>> random.sample(days, 7)      # Choose 7 elements
['Tu', 'Th', 'Mo', 'We', 'St', 'Fr', 'Sn']
>>> random.sample(days, 7)      # Choose 7 again
['We', 'Mo', 'Sn', 'Fr', 'Tu', 'St', 'Th']
>>> random.sample(days, 8)      # Can't choose eight
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
  File "random.py", line 414, in sample
      raise ValueError, "sample larger than population"
ValueError: sample larger than population
>>> random.sample(xrange(1,10000,2), 10)   # Choose ten odd nos. under 10000
[3407, 3805, 1505, 7023, 2401, 2267, 9733, 3151, 8083, 9195]

```

The [`random`](https://docs.python.org/3.14/library/random.html#module-random) module now relies on a new algorithm, the Mersenne Twister, written in C. It is quicker and has been studied more thoroughly than the earlier algorithm.

(All changes contributed by Raymond Hettinger.)

- The [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) module similarly picked up several new functions: [`get_history_item()`](https://docs.python.org/3.14/library/readline.html#readline.get_history_item), [`get_current_history_length()`](https://docs.python.org/3.14/library/readline.html#readline.get_current_history_length), and [`redisplay()`](https://docs.python.org/3.14/library/readline.html#readline.redisplay).

- The `rexec` and `Bastion` modules have been pronounced dead, and any attempt to import them now fails with a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError). New-style classes open up fresh avenues to escape the restricted execution environment that `rexec` supplies, and nobody is interested in fixing them or has the time to. If your applications depend on `rexec`, rewrite them to rely on something else.

(Remaining on Python 2.2 or 2.1 grants your applications no extra safety, since the `rexec` module in those releases has known bugs. To say it again: if you are using `rexec`, stop using it right away.)

- The `rotor` module has been deprecated because its encryption algorithm is not thought to be secure. If you require encryption, turn to one of the several AES Python modules available separately.

- The [`shutil`](https://docs.python.org/3.14/library/shutil.html#module-shutil) module acquired a `move(src, dest)` function that recursively relocates a file or directory to a new spot.

- Support for more sophisticated POSIX signal handling was added to the [`signal`](https://docs.python.org/3.14/library/signal.html#module-signal) but then taken back out again, as it turned out to be impossible to make it work dependably across platforms.

- The [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module now supports timeouts. Calling the `settimeout(t)` method on a socket object establishes a timeout lasting *t* seconds. Any later socket operations that run past *t* seconds before finishing will abort and raise a [`socket.timeout`](https://docs.python.org/3.14/library/socket.html#socket.timeout) exception.

The first timeout implementation came from Tim O'Malley. Michael Gilfix folded it into the Python [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module and guided it through an extended review. Once the code was checked in, Guido van Rossum rewrote portions of it. (This serves as a fine illustration of a collaborative development process at work.)

- On Windows, the [`socket`](https://docs.python.org/3.14/library/socket.html#module-socket) module now comes with Secure Sockets Layer (SSL) support.

- At the Python level, the value held by the C `PYTHON_API_VERSION` macro is now exposed as `sys.api_version`. Calling the new `sys.exc_clear()` function clears the current exception.

- The new [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) module lets you both read and write archive files in **tar** format. (Contributed by Lars Gustäbel.)

- The new [`textwrap`](https://docs.python.org/3.14/library/textwrap.html#module-textwrap) module holds functions for wrapping strings that contain paragraphs of text. The `wrap(text, width)` function accepts a string and returns a list with the text broken into lines no wider than the chosen width. The `fill(text, width)` function returns one single string, reflowed to fit lines no longer than the chosen width. (As you might expect, [`fill()`](https://docs.python.org/3.14/library/textwrap.html#textwrap.fill) is layered on top of [`wrap()`](https://docs.python.org/3.14/library/textwrap.html#textwrap.wrap). For instance:

[Subject index](INDEX.md) · [Previous source section](idle-iterators-networking-and-system-module-changes.md) · [Next source section](text-threading-and-timing-updates.md) · [Release/subject declaration](standard-set-type.md) · [Release/subject declaration](standard-library-module-changes.md)
