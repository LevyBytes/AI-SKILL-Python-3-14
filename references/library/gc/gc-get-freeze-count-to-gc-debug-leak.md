# gc: `gc.get_freeze_count()`, `gc.garbage`, `gc.callbacks`, `gc.DEBUG_STATS`, `gc.DEBUG_COLLECTABLE`, `gc.DEBUG_UNCOLLECTABLE`, `gc.DEBUG_SAVEALL`, `gc.DEBUG_LEAK`

gc.get_freeze_count()

Return the number of objects in the permanent generation.

Added in version 3.7.

These variables are exposed for read-only access (mutating their values is fine, but you shouldn't rebind them):

 gc.garbage

A list holding objects that the collector judged unreachable yet was unable to free (uncollectable objects). As of Python 3.4, this list ought to stay empty almost always, the exception being when instances of C extension types carrying a non-`NULL` `tp_del` slot are in play.

When `DEBUG_SAVEALL` is set, every unreachable object lands on this list in place of being freed.

Changed in version 3.2: Should this list still hold entries at [interpreter shutdown](https://docs.python.org/3.14/glossary.html#term-interpreter-shutdown), a [`ResourceWarning`](https://docs.python.org/3.14/library/exceptions.html#ResourceWarning) — silent by default — is emitted. Setting `DEBUG_UNCOLLECTABLE` additionally causes every uncollectable object to be printed.

Changed in version 3.4: In line with [**PEP 442**](https://peps.python.org/pep-0442/), objects carrying a [`__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__) method no longer wind up in `gc.garbage`.

 gc.callbacks

A list of callbacks the garbage collector runs both before and after a collection. Each callback receives two arguments, *phase* and *info*.

*phase* can be one of two values:

>

“start”: The garbage collection is about to start.

“stop”: The garbage collection has finished.

*info* is a dict supplying the callback with extra detail. At present these keys are defined:

>

“generation”: The oldest generation being collected.

“collected”: When *phase* is “stop”, the number of objects successfully collected.

“uncollectable”: With *phase* being “stop”, the tally of objects that resisted collection and ended up in `garbage`.

Programs may append callbacks of their own to this list. The chief use cases are:

>

Collecting metrics on garbage collection: for example, how frequently the various generations get collected and how much time a collection consumes.

Letting programs spot and dispose of their own uncollectable types once those surface in `garbage`.

Added in version 3.3.

The following constants are provided for use with `set_debug()`:

 gc.DEBUG_STATS

Emit statistics as collection runs. Such data can help when you tune the collection frequency.

 gc.DEBUG_COLLECTABLE

Print information on collectable objects found.

 gc.DEBUG_UNCOLLECTABLE

Report on the uncollectable objects discovered (those the collector cannot reach yet cannot free). Such objects get appended to the `garbage` list.

Changed in version 3.2: At [interpreter shutdown](https://docs.python.org/3.14/glossary.html#term-interpreter-shutdown), also dump whatever the `garbage` list holds, provided it isn’t empty.

 gc.DEBUG_SAVEALL

With this set, every unreachable object that turns up is appended to *garbage* instead of being released. That can help when you are debugging a program that leaks.

 gc.DEBUG_LEAK

The set of debugging flags the collector needs to report on a program that leaks (equivalent to `DEBUG_COLLECTABLE | DEBUG_UNCOLLECTABLE | DEBUG_SAVEALL`).

[Subject index](INDEX.md) · [Previous](gc-get-count-to-gc-unfreeze.md) · [Continue](../getopt/getopt-getopt-to-getopt-getopterror.md) · [Owning module, declaration or section: gc](gc-enable-to-gc-set-threshold.md)
