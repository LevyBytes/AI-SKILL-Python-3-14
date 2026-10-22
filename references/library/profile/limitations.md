# Limitations

### Limitations

One limitation concerns the accuracy of the timing information. Deterministic profilers face a fundamental problem with accuracy. The most obvious restriction is that the underlying "clock" ticks only at a rate of (typically) around .001 seconds. So no measurement can be more accurate than that underlying clock. Take enough measurements and the "error" will tend to average out. Removing that first error, unfortunately, brings on a second source of error.

The second problem is that "it takes a while" between the moment an event is dispatched and the moment the profiler's call to read the time actually *gets* the clock's state. There is likewise a certain lag, from when the clock's value was read (and then tucked away) on leaving the profiler's event handler, until the user's code is running once more. The result is that functions called many times, or that call many functions, will typically pile up this error. The error accumulating in this manner is normally below the clock's accuracy (under a single clock tick), but it *can* add up and grow quite significant.

The problem matters more with `profile` than with the lower-overhead `cProfile`. For that reason, `profile` offers a way to calibrate itself for a given platform so this error can be removed probabilistically (on the average). Once the profiler is calibrated it will be more accurate (in a least-squares sense), though now and then it yields negative numbers (when call counts run unusually low and the gods of probability conspire against you :-). ) Do *not* let negative numbers in the profile alarm you. Such numbers ought to *only* appear once you have calibrated your profiler, and the figures are in truth better than what you would get with no calibration.

[Subject index](INDEX.md) · [Previous](what-is-deterministic-profiling.md) · [Continue](calibration.md)
