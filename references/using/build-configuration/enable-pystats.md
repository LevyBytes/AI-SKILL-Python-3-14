# --enable-pystats

--enable-pystats

Switch on collection of Python's internal performance statistics.

Statistics collection is off by default. To begin collecting at Python startup, run the `python3 -X pystats` command or assign the `PYTHONSTATS=1` environment variable.

When Python exits, the statistics get written out if collection was active and had not been cleared.

Effects:

- Adds the [`-X pystats`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command line option.

- Adds the `PYTHONSTATS` environment variable.

- Defines the `Py_STATS` macro.

- Adds these functions onto the [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys) module:

  - `sys._stats_on()`: Begins collecting statistics.

  - `sys._stats_off()`: Stops collecting statistics.

  - `sys._stats_clear()`: Wipes the statistics.

  - `sys._stats_dump()`: Writes the statistics to a file, then wipes them.

Output of the statistics lands in some arbitrary (most likely unique) file under `/tmp/py_stats/` (Unix) or `C:\temp\py_stats\` (Windows). Should that directory be absent, the results go to stderr instead.

Run `Tools/scripts/summarize_stats.py` to interpret the stats.

[Subject index](INDEX.md) · [Previous source section](with-pkg-config-check-yes-no.md) · [Following source section](enable-pystats-opcode-and-call-statistics.md) · [Opcode and call statistics](enable-pystats-opcode-and-call-statistics.md) · [Object and GC statistics](enable-pystats-object-and-garbage-collector-statistics.md)
