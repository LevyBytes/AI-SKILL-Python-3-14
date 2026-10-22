# Deprecation metadata and warning context managers

Whatever deprecation text you hand to the decorator gets stored under the `__deprecated__` attribute of the object it wraps. When the target is an overload, you have to place the decorator below the [`@~typing.overload`](https://docs.python.org/3.14/library/typing.html#typing.overload) marker so that the attribute shows up on the overload that [`typing.get_overloads()`](https://docs.python.org/3.14/library/typing.html#typing.get_overloads) hands back.

Added in version 3.13: See [**PEP 702**](https://peps.python.org/pep-0702/).

### Available Context Managers

`*class *warnings.catch_warnings(***, *record=False*, *module=None*, *action=None*, *category=Warning*, *lineno=0*, *append=False*)`

This context manager makes a copy of the warnings filter and the `showwarning()` function, then puts both back when it exits. Leaving *record* at its default of [`False`](https://docs.python.org/3.14/library/constants.html#False) means entry yields [`None`](https://docs.python.org/3.14/library/constants.html#None). Setting *record* to [`True`](https://docs.python.org/3.14/library/constants.html#True) instead gives you a list that fills up over time with the objects a custom `showwarning()` function observes (that function additionally keeps output from reaching `sys.stderr`). Every entry in that list is assured of carrying these attributes:

>
- `message`: the text of the warning, given as a [`Warning`](https://docs.python.org/3.14/library/exceptions.html#Warning) instance

- `category`: which class the warning belongs to, as a [`Warning`](https://docs.python.org/3.14/library/exceptions.html#Warning) subclass

- `filename`: the name of the file in which the warning was raised, a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str)

- `lineno`: which line within that file it came from, an [`int`](https://docs.python.org/3.14/library/functions.html#int)

- `file`: whichever file object handled the output, or `None` when there was none

- `line`: the relevant source-code line when it can be obtained, otherwise `None`

- `source`: the object that first triggered the warning when it is known, or else `None`

Changed in version 3.6: The `source` attribute was added.

Their exact type is left undefined and could be altered later; the only promise is that the attributes listed above will be present.

Supply a module through the *module* argument and its filter is the one shielded, in place of the module you would normally get from importing `warnings`. The main reason this argument is here is to allow the `warnings` module to be tested on its own.

Whenever *action* is something other than `None`, the rest of the arguments get forwarded to `simplefilter()`, just as though it had run the moment the context was entered.

Consult The Warnings Filter to learn what the *category* and *lineno* parameters signify.

Note

Refer to Concurrent safety of Context Managers for specifics on how concurrency-safe the `catch_warnings` context manager is inside programs that rely on several threads or on async functions.

Changed in version 3.11: The *action*, *category*, *lineno*, and *append* parameters were introduced here.

### Concurrent safety of Context Managers

How the `catch_warnings` context manager acts is governed by the [`sys.flags.context_aware_warnings`](https://docs.python.org/3.14/library/sys.html#sys.flags.context_aware_warnings) flag. A true value makes the context manager concurrent-safe; a false value does not. Here, concurrent-safe covers two things at once: being thread-safe and being usable inside [asyncio coroutines](https://docs.python.org/3.14/library/asyncio-task.html#coroutine) and tasks. Thread-safe, in turn, means the behavior stays predictable across a multi-threaded program. On free-threaded builds the flag starts out true, and on every other build it starts out false.

When the [`context_aware_warnings`](https://docs.python.org/3.14/library/sys.html#sys.flags.context_aware_warnings) flag is false, `catch_warnings` goes ahead and changes the global attributes belonging to the `warnings` module. Doing that is unsafe inside a concurrent program, whether it relies on several threads or on asyncio coroutines. Should two or more threads, say, reach for the `catch_warnings` class simultaneously, what happens is undefined.

With the flag set true, `catch_warnings` leaves the global attributes alone and keeps the freshly set warning-filtering state in a [`ContextVar`](https://docs.python.org/3.14/library/contextvars.html#contextvars.ContextVar) instead. Because a context variable gives you thread-local storage, this is what renders `catch_warnings` thread-safe.

The flag's value likewise shifts how the context handler's *record* parameter operates. Where *record* is true while the flag is false, the context manager does its job by swapping out the module's `showwarning()` function and reinstating it afterward, which is not concurrent-safe.

Where both *record* and the flag are true, no swap of the `showwarning()` function takes place at all. The recording state is signaled instead through an internal property held on the context variable, and so the `showwarning()` function does not get reinstated as the context handler is left.

You can turn the [`context_aware_warnings`](https://docs.python.org/3.14/library/sys.html#sys.flags.context_aware_warnings) flag on through the [`-X context_aware_warnings`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) command-line option or by way of the [`PYTHON_CONTEXT_AWARE_WARNINGS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_CONTEXT_AWARE_WARNINGS) environment variable.

>

Note

Odds are that any program after thread-safe behaviour from the warnings module will additionally want the [`thread_inherit_context`](https://docs.python.org/3.14/library/sys.html#sys.flags.thread_inherit_context) flag turned on. With it set, threads spun up by [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) begin life holding a copy of the context variables belonging to whichever thread launched them. So when it is true, the context that `catch_warnings` puts in place within one thread carries over to the fresh threads that thread spawns. When it is false, those new threads come up with an empty warnings context variable, so whatever filtering a `catch_warnings` context manager had arranged stops being in force.

Changed in version 3.14: Introduced the [`sys.flags.context_aware_warnings`](https://docs.python.org/3.14/library/sys.html#sys.flags.context_aware_warnings) flag along with the context-variable approach that `catch_warnings` takes whenever the flag is true. Earlier Python releases behaved as though the flag were permanently false.

[Subject index](INDEX.md)
