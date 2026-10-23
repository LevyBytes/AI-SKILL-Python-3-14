# What’s New in Python 2.3 / Other Changes and Fixes - pdb

### Other Changes and Fixes

As is customary, numerous other improvements and bugfixes were spread across the source tree. Scanning the CVS change logs reveals that 523 patches were applied and 514 bugs were fixed between Python 2.2 and 2.3. Both numbers are probably on the low side.

Among the more noteworthy changes are these:

- When the [`PYTHONINSPECT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONINSPECT) environment variable is set, the Python interpreter drops into the interactive prompt once a Python program finishes, exactly as though Python had been started with the [`-i`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-i) option. You can set the environment variable before launching the Python interpreter, or the Python program itself can set it during execution.

- The `regrtest.py` script now offers a means to permit "all resources except *foo*." A resource name given to the `-u` option may now carry a leading hyphen (`'-'`) signifying "remove this resource." For instance, the option '`-uall,-bsddb`' would let you use all resources apart from `bsddb`.

- The tooling used to build the documentation now functions under Cygwin in addition to Unix.

- The `SET_LINENO` opcode has been removed. Long ago, this opcode was required to generate line numbers in tracebacks and to support trace functions (for instance, [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb)). Since Python 1.5, traceback line numbers have been derived through a different mechanism that also works with "python -O". For Python 2.3, Michael Hudson built a comparable scheme to decide when to invoke the trace function, doing away with the need for `SET_LINENO` altogether.

Detecting any consequent difference from Python code would be tough, aside from a minor speed-up when Python runs without [`-O`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-O).

C extensions that read the [`f_lineno`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_lineno) field of frame objects ought to call `PyCode_Addr2Line(f->f_code, f->f_lasti)` in its place. This carries the bonus of making the code behave correctly under "python -O" in older Python versions too.

One handy new capability lets a trace function assign a value to the [`f_lineno`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_lineno) attribute on frame objects, thereby changing which line executes next. A `jump` command exploiting this new capability has been added to the [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) debugger. (Implemented by Richie Hindle.)

[Subject index](INDEX.md) · [Previous source section](port-specific-changes.md) · [Next source section](porting-to-python-2-3.md) · [Release/subject declaration](standard-set-type.md)
