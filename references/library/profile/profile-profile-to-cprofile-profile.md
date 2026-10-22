# Using a custom timer

### Using a custom timer

Should you wish to override how the present moment gets measured — perhaps to insist on wall-clock readings or on process time consumed — supply your chosen timing callable to the `Profile` class constructor:

```python
pr = profile.Profile(your_time_func)

```

From that point on, the profiler invokes `your_time_func`. How the `your_time_func`’s output is read varies according to whether your code relies on `profile.Profile` versus `cProfile.Profile`:

`profile.Profile`

Here `your_time_func` ought to hand back either one number or a sequence of numbers that add up to the present time (much as [`os.times()`](https://docs.python.org/3.14/library/os.html#os.times) does). Supplying just one time value, or a returned sequence of length 2, earns you a notably quicker variant of the dispatch routine.

Keep in mind that the profiler class needs calibrating against whichever timer you settle on (consult Calibration). On the majority of hardware, a timer handing back a single integer keeps profiling overhead lowest and so performs best. ([`os.times()`](https://docs.python.org/3.14/library/os.html#os.times) does *pretty* poorly here, since it yields a tuple of floating-point values). To slot in a superior timer in the tidiest way, subclass the profiler and bake in a swapped-out dispatch method tuned to your particular timer call, paired with the matching calibration constant.

`cProfile.Profile`

In this case `your_time_func` ought to yield exactly one number. Where it produces integers, you may additionally pass the constructor a second argument that states how long, in reality, a single time unit lasts. So if `your_integer_time_func` reports times expressed in thousandths of a second, you would build the `Profile` instance like this:

```python
pr = cProfile.Profile(your_integer_time_func, 0.001)

```

Since the `cProfile.Profile` class admits no calibration, treat bespoke timer functions cautiously and keep them as quick as you can. Squeezing the most out of a custom timer may even require embedding it directly in the C source of the internal `_lsprof` module.

Python 3.3 brought a handful of fresh additions to [`time`](https://docs.python.org/3.14/library/time.html#module-time) suited to taking accurate readings of either process or wall-clock time — one such is [`time.perf_counter()`](https://docs.python.org/3.14/library/time.html#time.perf_counter).

[Subject index](INDEX.md)
