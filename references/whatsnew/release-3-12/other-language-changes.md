# What’s New In Python 3.12 / Other Language Changes — ast, shutil, sys, tarfile, types

An octal escape whose value exceeds `0o377` (for instance `"\477"`), already deprecated back in Python 3.11, now emits a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) rather than a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Some later Python release will eventually promote this to a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). (Contributed by Victor Stinner in [gh-98401](https://github.com/python/cpython/issues/98401).)

- Names appearing in the iteration target of a comprehension that are never bound there may now serve inside assignment expressions (`:=`). To illustrate, within `[(b := 1) for a, b.prop in some_iter]`, binding `b` is permitted from now on. Keep in mind that binding names that the comprehension target itself stores into (such as `a`) remains forbidden, following [**PEP 572**](https://peps.python.org/pep-0572/). (Contributed by Nikita Sobolev in [gh-100581](https://github.com/python/cpython/issues/100581).)

- Errors thrown from a class or type’s `__set_name__` hook are not wrapped inside a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) any longer. Surrounding detail gets attached to the error through a [**PEP 678**](https://peps.python.org/pep-0678/) note. (Contributed by Irit Katriel in [gh-77757](https://github.com/python/cpython/issues/77757).)

- Should a `try-except*` block deal with the whole [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup) and then throw a single additional error, that error is no longer enclosed within an `ExceptionGroup`. This was likewise adjusted back in release 3.11.4. (Contributed by Irit Katriel in [gh-103590](https://github.com/python/cpython/issues/103590).)

- Rather than triggering on object allocation, the Garbage Collector now fires solely via the eval breaker pathway of the Python bytecode evaluation loop. The GC may additionally fire whenever [`PyErr_CheckSignals()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_CheckSignals) is invoked, giving C extensions that stay busy for extended spans without running any Python code the opportunity to run the GC at intervals too. (Contributed by Pablo Galindo in [gh-97922](https://github.com/python/cpython/issues/97922).)

- Every builtin or extension callable that takes boolean parameters will now take values of whatever type rather than restricting itself to [`bool`](https://docs.python.org/3.14/library/functions.html#bool) and [`int`](https://docs.python.org/3.14/library/functions.html#int). (Contributed by Serhiy Storchaka in [gh-60203](https://github.com/python/cpython/issues/60203).)

- [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) gained handling for the half-float type, namely the “e” format code. (Contributed by Donghee Na and Antoine Pitrou in [gh-90751](https://github.com/python/cpython/issues/90751).)

- [`slice`](https://docs.python.org/3.14/library/functions.html#slice) objects can now be hashed, which lets them act as set items or as keys within a dict. (Contributed by Will Bradshaw, Furkan Onder, and Raymond Hettinger in [gh-101264](https://github.com/python/cpython/issues/101264).)

- [`sum()`](https://docs.python.org/3.14/library/functions.html#sum) has switched to Neumaier summation, raising accuracy and commutativity whenever floats, or a blend of ints and floats, are added together. (Contributed by Raymond Hettinger in [gh-100425](https://github.com/python/cpython/issues/100425).)

- [`ast.parse()`](https://docs.python.org/3.14/library/ast.html#ast.parse) will raise [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) rather than [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when the source it parses holds null bytes. (Contributed by Pablo Galindo in [gh-96670](https://github.com/python/cpython/issues/96670).)

- The extraction routines within [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile), along with [`shutil.unpack_archive()`](https://docs.python.org/3.14/library/shutil.html#shutil.unpack_archive), gained a fresh *filter* argument letting you restrict tar capabilities that could be unexpected or hazardous, like writing files beyond the destination directory. Consult [tarfile extraction filters](https://docs.python.org/3.14/library/tarfile.html#tarfile-extraction-filter) for the specifics. With Python 3.14, the default flips to `'data'`. (Contributed by Petr Viktorin in [**PEP 706**](https://peps.python.org/pep-0706/).)

- [`types.MappingProxyType`](https://docs.python.org/3.14/library/types.html#types.MappingProxyType) instances become hashable whenever the wrapped mapping is itself hashable. (Contributed by Serhiy Storchaka in [gh-87995](https://github.com/python/cpython/issues/87995).)

- Add [support for the perf profiler](https://docs.python.org/3.14/howto/perf_profiling.html#perf-profiling) by way of the fresh environment variable [`PYTHONPERFSUPPORT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONPERFSUPPORT) and the command-line flag [`-X perf`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X), together with the brand-new [`sys.activate_stack_trampoline()`](https://docs.python.org/3.14/library/sys.html#sys.activate_stack_trampoline), [`sys.deactivate_stack_trampoline()`](https://docs.python.org/3.14/library/sys.html#sys.deactivate_stack_trampoline), and [`sys.is_stack_trampoline_active()`](https://docs.python.org/3.14/library/sys.html#sys.is_stack_trampoline_active) functions. The design here came from Pablo Galindo. (Contributed by Pablo Galindo together with Christian Heimes, plus further work from Gregory P. Smith [Google] and Mark Shannon in [gh-96123](https://github.com/python/cpython/issues/96123).)

### Other Language Changes

- When source code holding null bytes is parsed, the parser now raises [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). (Contributed by Pablo Galindo in [gh-96670](https://github.com/python/cpython/issues/96670).)

- Whenever a backslash-character pair fails to form a valid escape sequence, the result is now a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) rather than a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). As an example, `re.compile("\d+\.\d+")` now raises a `SyntaxWarning` (`"\d"` is an invalid escape sequence, use raw strings for regular expression: `re.compile(r"\d+\.\d+")`). Down the road, a later Python release will at last raise [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) in place of `SyntaxWarning`. (Contributed by Victor Stinner in [gh-98401](https://github.com/python/cpython/issues/98401).)

-

[Subject index](INDEX.md) · [Next source section](new-modules.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](pep-698-override-decorator-for-static-typing.md)
