# bdb — `bdb` — Debugger framework

*class *bdb.Breakpoint(*self*, *file*, *line*, *temporary=False*, *cond=None*, *funcname=None*)

Temporary breakpoints, ignore counts, disabling and (re-)enabling, plus conditionals are all implemented by this class.

A list named `bpbynumber` indexes breakpoints by number, while `bplist` indexes them by `(file, line)` pairs. The former refers to a lone instance of class `Breakpoint`. The latter refers to a list of such instances, given that one line may carry more than one breakpoint.

As a breakpoint is created, its associated `file name` should be in canonical form. Where a `funcname` is defined, a breakpoint `hit` gets counted once the first line of that function runs. A `conditional` breakpoint always tallies a `hit`.

`Breakpoint` instances have the following methods:

 deleteMe()

Delete the breakpoint from the list tied to a file/line. Should it be the final breakpoint at that spot, it removes the file/line entry as well.

 enable()

Mark the breakpoint as enabled.

 disable()

Mark the breakpoint as disabled.

 bpformat()

Return a string carrying every piece of information about the breakpoint, neatly formatted:

- Breakpoint number.

- Temporary status (del or keep).

- File/line position.

- Break condition.

- Number of times to ignore.

- Number of times hit.

Added in version 3.2.

 bpprint(*out=None*)

Print the output of `bpformat()` to the file *out*, or, when that is `None`, to standard output.

`Breakpoint` instances have the following attributes:

 file

File name of the `Breakpoint`.

 line

Line number of the `Breakpoint` within `file`.

 temporary

`True` if a `Breakpoint` at (file, line) is temporary.

 cond

Condition for evaluating a `Breakpoint` at (file, line).

 funcname

Function name that defines whether a `Breakpoint` is hit upon entering the function.

 enabled

`True` if `Breakpoint` is enabled.

[Subject index](INDEX.md) · [Previous](bdb-bdbquit.md) · [Continue](bdb-debugger-framework.md) · [Owning module, declaration or section: bdb](bdb-bdbquit.md)
