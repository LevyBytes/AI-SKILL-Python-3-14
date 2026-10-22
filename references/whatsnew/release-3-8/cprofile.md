# What’s New In Python 3.8 / cProfile — profile

> (Contributed by Raymond Hettinger in [bpo-35864](https://bugs.python.org/issue?@action=redirect&bpo=35864).)

### cProfile

You may now drive the [`cProfile.Profile`](https://docs.python.org/3.14/library/profile.html#profile.Profile) class as a context manager. Wrap a region of code to profile it like so:

```python
import cProfile

with cProfile.Profile() as profiler:
      # code to be profiled
      ...

```

[Subject index](INDEX.md) · [Previous source section](collections.md) · [Next source section](csv.md) · [Release/subject declaration](assignment-expressions.md)
