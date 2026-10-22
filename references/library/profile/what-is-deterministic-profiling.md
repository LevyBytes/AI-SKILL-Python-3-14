# What Is Deterministic Profiling?

### What Is Deterministic Profiling?

*Deterministic profiling* is intended to capture the fact that every *function call*, *function return*, and *exception* event is monitored, with precise timings taken for the intervals between those events (during which the user's code runs). By contrast, *statistical profiling* (which this module does not do) samples the effective instruction pointer at random and infers where time is going. That latter approach has traditionally carried less overhead (since the code need not be instrumented), but it yields only relative hints about where time is spent.

In Python, because an interpreter is active throughout execution, no instrumented code is needed in order to do deterministic profiling. Python supplies a *hook* (an optional callback) for each event automatically. On top of that, Python's interpreted nature already loads so much overhead onto execution that deterministic profiling tends to add only a small amount of processing overhead in typical applications. The upshot is that deterministic profiling is not all that costly, yet it yields extensive run-time statistics about how a Python program executes.

Counts of calls can help you spot bugs in code (counts that surprise you) and pick out candidate inline-expansion points (counts that run high). Internal-time figures help you locate "hot loops" deserving careful optimization. Cumulative-time figures help you catch high-level mistakes in choosing algorithms. Note that, thanks to how this profiler handles cumulative times in its unusual way, statistics from recursive implementations of algorithms can be compared head-to-head against iterative ones.

[Subject index](INDEX.md) · [Previous](pstats-stats-print-callees-to-pstats-stats-get-stats-profile.md) · [Continue](limitations.md)
