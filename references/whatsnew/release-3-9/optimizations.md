# What's New In Python 3.9 / Optimizations — subprocess

### Optimizations

- The idiom that assigns a temporary variable within comprehensions was optimized. Writing `for y in [expr]` inside a comprehension now runs as quickly as the plain assignment `y = expr`. As an illustration:

```python
sums = [s for s in [0] for x in data for s in [s + x]]
```

In contrast to the `:=` operator, this idiom keeps the variable from escaping into the enclosing scope.

(Contributed by Serhiy Storchaka in [bpo-32856](https://bugs.python.org/issue?@action=redirect&bpo=32856).)

- Signal handling within multithreaded programs was optimized. When a signal lands on a thread other than the main one, the bytecode evaluation loop is no longer paused at every bytecode instruction to look for pending signals that it cannot handle. Signals can only be handled by the main thread belonging to the main interpreter.

Formerly, the bytecode evaluation loop was paused at every instruction until the signals were handled by the main thread. (Contributed by Victor Stinner in [bpo-40010](https://bugs.python.org/issue?@action=redirect&bpo=40010).)

- On FreeBSD, the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module was optimized through use of `closefrom()`. (Work credited, under [bpo-38061](https://bugs.python.org/issue?@action=redirect&bpo=38061), to Ed Maste, Conrad Meyer, Kyle Evans, Kubilay Kocak and Victor Stinner.)

- For values that fit inside a long, [`PyLong_FromDouble()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromDouble) now runs up to 1.87x faster. (Contributed by Sergey Fedoseev in [bpo-37986](https://bugs.python.org/issue?@action=redirect&bpo=37986).)

- Several Python builtins ([`range`](https://docs.python.org/3.14/library/stdtypes.html#range), [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple), [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset), [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict)) were accelerated by adopting the vectorcall protocol from [**PEP 590**](https://peps.python.org/pep-0590/). (Work credited, under [bpo-37207](https://bugs.python.org/issue?@action=redirect&bpo=37207), to Donghee Na, Mark Shannon, Jeroen Demeyer and Petr Viktorin.)

- `set.difference_update()` was optimized for situations where the other set far outsizes the base one. (Suggestion under [bpo-8425](https://bugs.python.org/issue?@action=redirect&bpo=8425) came from Evgeny Kapun, with the implementing code provided by Michele Orr?.)

- The small object allocator in Python (`obmalloc.c`) now permits at most a single empty arena to stay around for instant reuse instead of handing it back to the OS. That keeps tight loops from thrashing, where otherwise an arena would be built and torn down fresh on every pass. (Contributed by Tim Peters in [bpo-37257](https://bugs.python.org/issue?@action=redirect&bpo=37257).)

- The [floor division](https://docs.python.org/3.14/glossary.html#term-floor-division) of a float operation now performs better. The [`ZeroDivisionError`](https://docs.python.org/3.14/library/exceptions.html#ZeroDivisionError) message for that operation was also revised. (Contributed by Donghee Na in [bpo-39434](https://bugs.python.org/issue?@action=redirect&bpo=39434).)

- Decoding brief ASCII strings via the UTF-8 and ascii codecs is now roughly 15% quicker. (Contributed by Inada Naoki in [bpo-37348](https://bugs.python.org/issue?@action=redirect&bpo=37348).)

A roundup of the performance gains spanning Python 3.4 up through Python 3.9 follows:

```none
Python version                       3.4     3.5     3.6     3.7     3.8    3.9
--------------                       ---     ---     ---     ---     ---    ---

Variable and attribute read access:
    read_local                       7.1     7.1     5.4     5.1     3.9    3.9
    read_nonlocal                    7.1     8.1     5.8     5.4     4.4    4.5
    read_global                     15.5    19.0    14.3    13.6     7.6    7.8
    read_builtin                    21.1    21.6    18.5    19.0     7.5    7.8
    read_classvar_from_class        25.6    26.5    20.7    19.5    18.4   17.9
    read_classvar_from_instance     22.8    23.5    18.8    17.1    16.4   16.9
    read_instancevar                32.4    33.1    28.0    26.3    25.4   25.3
    read_instancevar_slots          27.8    31.3    20.8    20.8    20.2   20.5
    read_namedtuple                 73.8    57.5    45.0    46.8    18.4   18.7
    read_boundmethod                37.6    37.9    29.6    26.9    27.7   41.1

Variable and attribute write access:
    write_local                      8.7     9.3     5.5     5.3     4.3    4.3
    write_nonlocal                  10.5    11.1     5.6     5.5     4.7    4.8
    write_global                    19.7    21.2    18.0    18.0    15.8   16.7
    write_classvar                  92.9    96.0   104.6   102.1    39.2   39.8
    write_instancevar               44.6    45.8    40.0    38.9    35.5   37.4
    write_instancevar_slots         35.6    36.1    27.3    26.6    25.7   25.8

Data structure read access:
    read_list                       24.2    24.5    20.8    20.8    19.0   19.5
    read_deque                      24.7    25.5    20.2    20.6    19.8   20.2
    read_dict                       24.3    25.7    22.3    23.0    21.0   22.4
    read_strdict                    22.6    24.3    19.5    21.2    18.9   21.5

Data structure write access:
    write_list                      27.1    28.5    22.5    21.6    20.0   20.0
    write_deque                     28.7    30.1    22.7    21.8    23.5   21.7
    write_dict                      31.4    33.3    29.3    29.2    24.7   25.4
    write_strdict                   28.4    29.9    27.5    25.2    23.1   24.5

Stack (or queue) operations:
    list_append_pop                 93.4   112.7    75.4    74.2    50.8   50.6
    deque_append_pop                43.5    57.0    49.4    49.2    42.5   44.2
    deque_append_popleft            43.7    57.3    49.7    49.7    42.8   46.4

Timing loop:
    loop_overhead                    0.5     0.6     0.4     0.3     0.3    0.3

```

The figures above came from the variable access benchmark script located at `Tools/scripts/var_access_benchmark.py`. Timings reported by that benchmark script are given in nanoseconds. Measurements were taken on an [Intel? Core? i7-4960HQ processor](https://ark.intel.com/content/www/us/en/ark/products/76088/intel-core-i7-4960hq-processor-6m-cache-up-to-3-80-ghz.html) using the 64-bit macOS builds available from [python.org](https://www.python.org/downloads/macos/).

[Subject index](INDEX.md) · [Previous source section](xml.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](deprecated.md)
