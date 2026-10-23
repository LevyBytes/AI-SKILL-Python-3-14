# What’s New in Python 2.2 / Other Changes and Fixes - sys, weakref

### Other Changes and Fixes

As ever, plenty of additional improvements and bug fixes were sprinkled across the source tree. Combing the CVS change logs turns up 527 patches applied and 683 bugs fixed across the Python 2.1 to 2.2 span; 2.2.1 brought 139 patches and 143 bug fixes; 2.2.2 brought 106 patches and 82 bug fixes. In all likelihood those tallies run low.

A few of the changes worth singling out:

- Jack Jansen's MacOS port of Python now resides in the main Python CVS tree, and a great many changes have gone in to back MacOS X.

The standout change is being able to build Python as a framework, switched on by passing the `--enable-framework` option to the configure script as you compile Python. Jack Jansen explains that doing so drops a self-contained Python install, together with the OS X framework “glue”, into `/Library/Frameworks/Python.framework` — or wherever else you point it. He notes that the immediate payoff is slim today, and indeed there's a downside: you must adjust your PATH before Python can be located. Even so, he describes it as the groundwork for a number of things — assembling a fully fledged Python application, bringing over the MacPython IDE, perhaps treating Python as a standard OSA scripting language, and a good deal besides.

Nearly all of the MacPython toolbox modules — the ones that bridge to MacOS APIs like windowing, QuickTime, scripting, and so on — have made it over to OS X, though they sit commented out in `setup.py`. Anyone wanting to play with these modules can uncomment them by hand.

- Hand keyword arguments to a built-in function that accepts none and you'll now trigger a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception carrying the message “*function* takes no keyword arguments”.

- Weak references, which arrived in Python 2.1 as an extension module, now belong to the core, since new-style classes rely on them under the hood. As a result, the [`ReferenceError`](https://docs.python.org/3.14/library/exceptions.html#ReferenceError) exception has shifted out of the [`weakref`](https://docs.python.org/3.14/library/weakref.html#module-weakref) module and become a built-in exception.

- Tim Peters contributed a new script, `Tools/scripts/cleanfuture.py`, that strips outdated `__future__` statements out of Python source automatically.

- The built-in function [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) has picked up an extra *flags* argument, letting the effect of `__future__` statements be observed properly inside simulated shells — the kind that IDLE and other development environments provide. [**PEP 264**](https://peps.python.org/pep-0264/) lays this out. (Contributed by Michael Hudson.)

- The license that came with Python 1.6 turned out not to be GPL-compatible. A few small wording tweaks to the 2.2 license put that right, so embedding Python within a GPLed program is once again permitted. Keep in mind that Python is not itself GPLed; it carries a license that boils down to roughly the BSD license, just as it always has. Those same license tweaks were applied as well to the Python 2.0.1 and 2.1.1 releases.

- Given a Unicode filename on Windows, Python now turns it into an MBCS-encoded string of the sort the Microsoft file APIs expect. Because those file APIs deliberately work in MBCS, Python's default of ASCII encoding becomes a nuisance. Over on Unix, the locale's character set gets used whenever `locale.nl_langinfo(CODESET)` is on hand. (On the Windows side the work came from Mark Hammond, helped by Marc-André Lemburg; the Unix side was the doing of Martin von Löwis.)

- Large file support is now enabled on Windows. (Contributed by Tim Peters.)

- Should you have a `.netrc` file, the `Tools/scripts/ftpmirror.py` script now reads it. (Contributed by Mike Romberg.)

- Certain features of the object that the `xrange()` function hands back are now deprecated and raise warnings on access; they're slated to vanish in Python 2.3. By supporting slicing, sequence multiplication, and the [`in`](https://docs.python.org/3.14/reference/expressions.html#in) operator, `xrange` objects had tried to masquerade as full sequence types, yet those features saw little use and were consequently buggy. Likewise headed for deprecation are the `tolist()` method along with the `start`, `stop`, and `step` attributes. Down at the C level, the `PyRange_New()` function's fourth argument, `repeat`, has been deprecated too.

- The dictionary implementation took a number of patches, largely aimed at heading off possible core dumps when a dictionary holds objects that quietly altered their hash value or mutated the very dictionary they sat inside. For a stretch, python-dev settled into an easy cadence: Michael Hudson would turn up a core-dumping case, Tim Peters would patch the bug, Michael would surface another, and so it went on and on.

- Owing to several patches from Stephen Hansen, Python can now be built with Borland C on Windows, even if the outcome isn't fully working just yet. (Still, this *is* progress…)

- One more Windows improvement: Wise Solutions kindly let PythonLabs make use of their InstallerMaster 8.1 system. The previous PythonLabs Windows installers ran on Wise 5.0a, which had started to look dated. (Packaged up by Tim Peters.)

- On Windows, files whose names end in `.pyw` can now be imported. The `.pyw` suffix is a Windows-only convention, signalling that a script must run under PYTHONW.EXE rather than PYTHON.EXE so that no DOS console pops open to show the output. This patch lets such scripts be imported, for the cases where they double as modules. (Implemented by David Bolen.)

- On platforms where Python loads extension modules through the C `dlopen()` function, you can now adjust the flags that `dlopen()` passes by way of the [`sys.getdlopenflags()`](https://docs.python.org/3.14/library/sys.html#sys.getdlopenflags) and [`sys.setdlopenflags()`](https://docs.python.org/3.14/library/sys.html#sys.setdlopenflags) functions. (Contributed by Bram Stolk.)

- When given floating-point numbers, the [`pow()`](https://docs.python.org/3.14/library/functions.html#pow) built-in function no longer accepts 3 arguments. Although `pow(x, y, z)` computes `(x**y) % z`, that is of no value for floating-point numbers and the end result swings unpredictably from one platform to the next. From now on a call like `pow(2.0, 8.0, 7.0)` raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception.

[Subject index](INDEX.md) · [Previous source section](interpreter-changes-and-fixes.md) · [Release/subject declaration](introduction.md)
