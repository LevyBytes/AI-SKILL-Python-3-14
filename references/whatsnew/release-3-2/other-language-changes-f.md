# What's New In Python 3.2 / Other Language Changes - collections.abc, gc, os, sys, time, warnings

This is permitted now. Bear in mind that the [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) clause's target gets cleared, so the snippet below, functional under Python 2.6, threw a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) under Python 3.1 and once again runs:

```python
def f():
    def print_error():
        print(e)
    try:
        something
    except Exception as e:
        print_error()
        # implicit "del e" here

```

(See [bpo-4617](https://bugs.python.org/issue?@action=redirect&bpo=4617).)

- [Struct sequence types](https://docs.python.org/3.14/c-api/tuple.html#struct-sequence-objects) now derive from tuple. So the C structures returned from calls like [`os.stat()`](https://docs.python.org/3.14/library/os.html#os.stat), [`time.gmtime()`](https://docs.python.org/3.14/library/time.html#time.gmtime), and [`sys.version_info`](https://docs.python.org/3.14/library/sys.html#sys.version_info) behave like a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) and accept being passed to functions and methods that take a tuple argument. That marks major progress toward giving the C structures the same flexibility their pure Python equivalents enjoy:

```python
>>> import sys
>>> isinstance(sys.version_info, tuple)
True
>>> 'Version %d.%d.%d %s(%d)' % sys.version_info
'Version 3.2.0 final(0)'

```

(Suggested by Arfrever Frehtes Taifersar Arahesis and implemented by Benjamin Peterson in [bpo-8413](https://bugs.python.org/issue?@action=redirect&bpo=8413).)

- Controlling warnings is now simpler via the [`PYTHONWARNINGS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONWARNINGS) environment variable, which serves as a substitute for passing `-W` on the command line:

```shell
$ export PYTHONWARNINGS='ignore::RuntimeWarning::,once::UnicodeWarning::'

```

(Suggested by Barry Warsaw and implemented by Philip Jenvey in [bpo-7301](https://bugs.python.org/issue?@action=redirect&bpo=7301).)

- There is a fresh warning category, [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning). The interpreter raises it upon detecting likely trouble with resource usage or cleanup. Normal release builds keep it muted by default, yet you may turn it on through the facilities offered by the [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module, or from the command line.

At interpreter shutdown, a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) fires whenever the [`gc.garbage`](https://docs.python.org/3.14/library/gc.html#gc.garbage) list still holds entries, and when [`gc.DEBUG_UNCOLLECTABLE`](https://docs.python.org/3.14/library/gc.html#gc.DEBUG_UNCOLLECTABLE) has been set, every uncollectable object gets printed. The point is to alert the programmer that their code has object finalization problems.

Destroying a [file object](https://docs.python.org/3.14/glossary.html#term-file-object) without an explicit close also triggers a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning). Although the deallocator for that object does make sure the underlying operating system resource (typically a file descriptor) gets released, the lag before the object is deallocated may bring on assorted problems, particularly on Windows. Below is a demonstration of switching the warning on from the command line:

```shell
$ python -q -Wdefault
>>> f = open("foo", "wb")
>>> del f
__main__:1: ResourceWarning: unclosed file <_io.BufferedWriter name='foo'>

```

(Added by Antoine Pitrou and Georg Brandl in [bpo-10093](https://bugs.python.org/issue?@action=redirect&bpo=10093) and [bpo-477863](https://bugs.python.org/issue?@action=redirect&bpo=477863).)

- [`range`](https://docs.python.org/3.14/library/stdtypes.html#range) objects have gained *index* and *count* methods. That belongs to a wider drive to get more objects to fully realize the [`collections.Sequence`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Sequence) [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class). Consequently the language gains a more consistent API. On top of that, `range` objects now handle slicing plus negative indices, even at values exceeding [`sys.maxsize`](https://docs.python.org/3.14/library/sys.html#sys.maxsize). That lets *range* mesh better with lists:

```python
>>> range(0, 100, 2).count(10)
1
>>> range(0, 100, 2).index(10)
5
>>> range(0, 100, 2)[5]
10
>>> range(0, 100, 2)[0:5]
range(0, 10, 2)

```

(Work by Daniel Stutzbach landed in [bpo-9213](https://bugs.python.org/issue?@action=redirect&bpo=9213); Alexander Belopolsky's in [bpo-2690](https://bugs.python.org/issue?@action=redirect&bpo=2690); and Nick Coghlan's in [bpo-10889](https://bugs.python.org/issue?@action=redirect&bpo=10889).)

-

[Subject index](INDEX.md) · [Next source section](callable-builtin-and-language-changes.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md) · [Release/subject declaration](core-language-changes.md) · [Preceding release/subject continuation](other-language-changes-outer.md)
