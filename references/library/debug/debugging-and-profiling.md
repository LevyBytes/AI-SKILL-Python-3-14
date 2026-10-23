# dbm.dumb - Debugging and Profiling

## Debugging and Profiling

### Debugging and Profiling

These libraries support your Python work: the debugger lets you walk through code, examine stack frames, set breakpoints, and so on, while the profilers execute code and report a detailed timing breakdown so you can pinpoint the bottlenecks in your programs. Auditing events expose runtime behavior that you would otherwise only see through intrusive debugging or patching.

- [Audit events table](https://docs.python.org/3.14/library/audit_events.html)
- [`bdb` - Debugger framework](https://docs.python.org/3.14/library/bdb.html)
- [`faulthandler` - Dump the Python traceback](https://docs.python.org/3.14/library/faulthandler.html)
  - [Dumping the traceback](https://docs.python.org/3.14/library/faulthandler.html#dumping-the-traceback)
  - [Dumping the C stack](https://docs.python.org/3.14/library/faulthandler.html#dumping-the-c-stack)
    - [C Stack Compatibility](https://docs.python.org/3.14/library/faulthandler.html#c-stack-compatibility)

  - [Fault handler state](https://docs.python.org/3.14/library/faulthandler.html#fault-handler-state)
  - [Dumping the tracebacks after a timeout](https://docs.python.org/3.14/library/faulthandler.html#dumping-the-tracebacks-after-a-timeout)
  - [Dumping the traceback on a user signal](https://docs.python.org/3.14/library/faulthandler.html#dumping-the-traceback-on-a-user-signal)
  - [Issue with file descriptors](https://docs.python.org/3.14/library/faulthandler.html#issue-with-file-descriptors)
  - [Example](https://docs.python.org/3.14/library/faulthandler.html#example)

- [`pdb` - The Python Debugger](https://docs.python.org/3.14/library/pdb.html)
  - [Command-line interface](https://docs.python.org/3.14/library/pdb.html#command-line-interface)
  - [Debugger commands](https://docs.python.org/3.14/library/pdb.html#debugger-commands)

- [The Python Profilers](https://docs.python.org/3.14/library/profile.html)
  - [Introduction to the profilers](https://docs.python.org/3.14/library/profile.html#introduction-to-the-profilers)
  - [Instant User’s Manual](https://docs.python.org/3.14/library/profile.html#instant-user-s-manual)
  - [`profile` and `cProfile` Module Reference](https://docs.python.org/3.14/library/profile.html#module-cProfile)
  - [The `Stats` Class](https://docs.python.org/3.14/library/profile.html#the-stats-class)
  - [What Is Deterministic Profiling?](https://docs.python.org/3.14/library/profile.html#what-is-deterministic-profiling)
  - [Limitations](https://docs.python.org/3.14/library/profile.html#limitations)
  - [Calibration](https://docs.python.org/3.14/library/profile.html#calibration)
  - [Using a custom timer](https://docs.python.org/3.14/library/profile.html#using-a-custom-timer)

- [`timeit` - Measure execution time of small code snippets](https://docs.python.org/3.14/library/timeit.html)
  - [Basic Examples](https://docs.python.org/3.14/library/timeit.html#basic-examples)
  - [Python Interface](https://docs.python.org/3.14/library/timeit.html#python-interface)
  - [Command-Line Interface](https://docs.python.org/3.14/library/timeit.html#command-line-interface)
  - [Examples](https://docs.python.org/3.14/library/timeit.html#examples)

- [`trace` - Trace or track Python statement execution](https://docs.python.org/3.14/library/trace.html)
  - [Command-Line Usage](https://docs.python.org/3.14/library/trace.html#command-line-usage)
    - [Main options](https://docs.python.org/3.14/library/trace.html#main-options)
    - [Modifiers](https://docs.python.org/3.14/library/trace.html#modifiers)
    - [Filters](https://docs.python.org/3.14/library/trace.html#filters)

  - [Programmatic Interface](https://docs.python.org/3.14/library/trace.html#programmatic-interface)

- [`tracemalloc` - Trace memory allocations](https://docs.python.org/3.14/library/tracemalloc.html)
  - [Examples](https://docs.python.org/3.14/library/tracemalloc.html#examples)
    - [Display the top 10](https://docs.python.org/3.14/library/tracemalloc.html#display-the-top-10)
    - [Compute differences](https://docs.python.org/3.14/library/tracemalloc.html#compute-differences)
    - [Get the traceback of a memory block](https://docs.python.org/3.14/library/tracemalloc.html#get-the-traceback-of-a-memory-block)
    - [Pretty top](https://docs.python.org/3.14/library/tracemalloc.html#pretty-top)
      - [Record the current and peak size of all traced memory blocks](https://docs.python.org/3.14/library/tracemalloc.html#record-the-current-and-peak-size-of-all-traced-memory-blocks)

  - [API](https://docs.python.org/3.14/library/tracemalloc.html#api)
    - [Functions](https://docs.python.org/3.14/library/tracemalloc.html#functions)
    - [DomainFilter](https://docs.python.org/3.14/library/tracemalloc.html#domainfilter)
    - [Filter](https://docs.python.org/3.14/library/tracemalloc.html#filter)
    - [Frame](https://docs.python.org/3.14/library/tracemalloc.html#frame)
    - [Snapshot](https://docs.python.org/3.14/library/tracemalloc.html#snapshot)
    - [Statistic](https://docs.python.org/3.14/library/tracemalloc.html#statistic)
    - [StatisticDiff](https://docs.python.org/3.14/library/tracemalloc.html#statisticdiff)
    - [Trace](https://docs.python.org/3.14/library/tracemalloc.html#trace)
    - [Traceback](https://docs.python.org/3.14/library/tracemalloc.html#traceback)

[Subject index](INDEX.md)
