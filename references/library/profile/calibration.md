# Calibration

### Calibration

The profiler in the `profile` module subtracts a fixed constant from each event-handling time to make up for the overhead of calling the time function and stashing away the results. By default that constant is 0. You can use the procedure below to obtain a better constant for a given platform (see Limitations).

```python
import profile
pr = profile.Profile()
for i in range(5):
    print(pr.calibrate(10000))

```

The method performs as many Python calls as the argument asks for, once on its own and once more under the profiler, clocking each. From that it derives the concealed per-event profiler overhead and hands it back as a float. For instance, on a 1.8Ghz Intel Core i5 running macOS, with Python's time.process_time() serving as the timer, the magical number comes to roughly 4.04e-6.

The point of this exercise is to arrive at a fairly steady result. When your computer is *very* fast, or your timer function resolves poorly, you may need to pass 100000, or even 1000000, to get steady results.

Once you have a steady answer, there are three ways you can put it to use:

```python
import profile

# 1. Apply computed bias to all Profile instances created hereafter.
profile.Profile.bias = your_computed_bias

# 2. Apply computed bias to a specific Profile instance.
pr = profile.Profile()
pr.bias = your_computed_bias

# 3. Specify computed bias in instance constructor.
pr = profile.Profile(bias=your_computed_bias)

```

Given the choice, you are better off going with a smaller constant, since then your results will "less often" surface as negative in the profile statistics.

[Subject index](INDEX.md) · [Previous](limitations.md) · [Continue](profile-profile-to-cprofile-profile.md)
