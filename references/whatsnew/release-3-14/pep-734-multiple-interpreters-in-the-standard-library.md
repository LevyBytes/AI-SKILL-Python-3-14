# What's new in Python 3.14 / **PEP 734**: Multiple interpreters in the standard library — concurrent.interpreters, multiprocessing, threading

### [**PEP 734**](https://peps.python.org/pep-0734/): Multiple interpreters in the standard library

For more than two decades the CPython runtime has been able to host several concurrent copies of Python inside one process. The term for each independent copy is an "interpreter". Up to now, however, you could reach the capability solely via the [C-API](https://docs.python.org/3.14/c-api/subinterpreters.html#sub-interpreter-support).

Python 3.14 lifts that restriction by introducing the [`concurrent.interpreters`](https://docs.python.org/3.14/library/concurrent.interpreters.html#module-concurrent.interpreters) module.

Two especially noteworthy payoffs come from leaning on multiple interpreters:

- a concurrency model that is approachable for humans and novel within Python

- genuine parallelism spread across multiple cores

In certain situations, running software concurrently boosts throughput and, broadly speaking, can make a design cleaner. Yet building and sustaining anything beyond trivial concurrency tends to tax the human mind. The classic offender is bare threads (consider [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading)), in which every thread sees the very same shared memory.

Several isolated interpreters let you reach for a family of concurrency styles — for instance Communicating Sequential Processes (CSP) or the actor model — proven across other languages such as Smalltalk, Erlang, Haskell, and Go. Picture multiple interpreters as threads where sharing is opt-in rather than automatic.

On the topic of multi-core parallelism: since Python 3.12, interpreters have grown isolated enough from each other to run truly in parallel (refer to [**PEP 684**](https://peps.python.org/pep-0684/)). That opens up many CPU-bound Python workloads that the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) previously held back.

Reaching for multiple interpreters resembles [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) in numerous respects, since each gives you separate logical "processes" able to execute in parallel with nothing shared up front. The distinction is that an app built on multiple interpreters consumes fewer system resources and runs leaner, because everything stays inside one process. Picture multiple interpreters as combining process-grade isolation with thread-grade efficiency.

Even though this capability has existed for many years, few developers have leaned on multiple interpreters, owing to scant visibility and no standard-library entry point. As a result there remain a handful of notable constraints today, which should ease considerably now that the feature reaches a wider audience.

Current limitations:

- spinning up each interpreter still awaits optimization

- every interpreter consumes more memory than it strictly should (ongoing work targets broad internal sharing across interpreters)

- genuinely sharing objects or other data across interpreters offers few choices *yet* (apart from [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview))

- a great many third-party extension modules hosted on PyPI don't yet work with multiple interpreters (every standard library extension module *is* compatible, however)

- for the moment, crafting applications around several isolated interpreters is a style most Python developers haven't met

How much these constraints bite hinges on upcoming CPython work, the way interpreters get applied, and whatever the community ships through PyPI packages. For some workloads the constraints may barely register, so give it a spin!

Beyond that, later CPython releases will trim or remove overhead and ship helpers that wouldn't fit naturally on PyPI. For the time being, most constraints can equally be papered over via extension modules, so PyPI packages can close any gap as far back as 3.12 — the point where interpreters at last became properly isolated and quit sharing the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) — through 3.14. In the same vein, expect PyPI to grow libraries offering higher-level abstractions layered atop interpreters.

On the extension-module front, efforts are underway to bring several PyPI projects up to date, plus tooling like Cython, pybind11, nanobind, and PyO3. Instructions for isolating an extension module live at [Isolating Extension Modules](https://docs.python.org/3.14/howto/isolating-extensions.html#isolating-extensions-howto). Because isolating a module shares much ground with enabling free-threading, the community's active work there will speed along support for multiple interpreters too.

Also added in 3.14: concurrent.futures.InterpreterPoolExecutor.

(Contributed by Eric Snow in [gh-134939](https://github.com/python/cpython/issues/134939).)

See also

[**PEP 734**](https://peps.python.org/pep-0734/)

[Subject index](INDEX.md) · [Previous source section](pep-649-pep-749-deferred-evaluation-of-annotations.md) · [Next source section](pep-750-template-string-literals.md) · [Release/subject declaration](summary-release-highlights.md)
