# What's New In Python 3.13 / Improved error messages

> (Contributed by Pablo Galindo Salgado, ?ukasz Langa, and Lysandros Nikolaou in [gh-111201](https://github.com/python/cpython/issues/111201) based on code from the PyPy project. Windows support contributed by Dino Viehland and Anthony Shaw.)

### Improved error messages

- When rendering tracebacks at the terminal, the interpreter now applies color by default. You [can control](https://docs.python.org/3.14/using/cmdline.html#using-on-controlling-color) this behavior through the new [`PYTHON_COLORS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_COLORS) environment variable along with the standard [`NO_COLOR`](https://no-color.org/) and [`FORCE_COLOR`](https://force-color.org/) environment variables. (Contributed by Pablo Galindo Salgado in [gh-112730](https://github.com/python/cpython/issues/112730).)

- People often write a script bearing the same name as a standard library module. Should that produce errors, a more useful message is now shown:

```pytb
$ python random.py
Traceback (most recent call last):
  File "/home/me/random.py", line 1, in <module>
    import random
  File "/home/me/random.py", line 3, in <module>
    print(random.randint(5))
          ^^^^^^^^^^^^^^
AttributeError: module 'random' has no attribute 'randint' (consider renaming '/home/me/random.py' since it has the same name as the standard library module named 'random' and prevents importing that standard library module)

```

In the same way, when a script carries the same name as a third-party module it tries to import and that yields errors, a more useful message is likewise shown:

```pytb
$ python numpy.py
Traceback (most recent call last):
  File "/home/me/numpy.py", line 1, in <module>
    import numpy as np
  File "/home/me/numpy.py", line 3, in <module>
    np.array([1, 2, 3])
    ^^^^^^^^
AttributeError: module 'numpy' has no attribute 'array' (consider renaming '/home/me/numpy.py' if it has the same name as a library you intended to import)

```

(Contributed by Shantanu Jain in [gh-95754](https://github.com/python/cpython/issues/95754).)

- When a wrong keyword argument reaches a function, the message now attempts to propose the right keyword argument.

```pycon
>>> "Better error messages!".split(max_split=1)
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    "Better error messages!".split(max_split=1)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
TypeError: split() got an unexpected keyword argument 'max_split'. Did you mean 'maxsplit'?

```

(Contributed by Pablo Galindo Salgado and Shantanu Jain in [gh-107944](https://github.com/python/cpython/issues/107944).)

[Subject index](INDEX.md) · [Previous source section](a-better-interactive-interpreter.md) · [Next source section](free-threaded-cpython.md) · [Release/subject declaration](summary-release-highlights.md)
