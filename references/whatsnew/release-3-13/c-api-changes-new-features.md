# Python 3.13 changes: Monitoring, mutex, clock and dictionary API additions

### C API Changes

### New Features

- Add the [PyMonitoring C API](https://docs.python.org/3.14/c-api/monitoring.html#c-api-monitoring) for emitting [**PEP 669**](https://peps.python.org/pep-0669/) monitoring events:

  - [`PyMonitoringState`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoringState)

  - [`PyMonitoring_FirePyStartEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FirePyStartEvent)

  - [`PyMonitoring_FirePyResumeEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FirePyResumeEvent)

  - [`PyMonitoring_FirePyReturnEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FirePyReturnEvent)

  - [`PyMonitoring_FirePyYieldEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FirePyYieldEvent)

  - [`PyMonitoring_FireCallEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FireCallEvent)

  - [`PyMonitoring_FireLineEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FireLineEvent)

  - [`PyMonitoring_FireJumpEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FireJumpEvent)

  - `PyMonitoring_FireBranchEvent`

  - [`PyMonitoring_FireCReturnEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FireCReturnEvent)

  - [`PyMonitoring_FirePyThrowEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FirePyThrowEvent)

  - [`PyMonitoring_FireRaiseEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FireRaiseEvent)

  - [`PyMonitoring_FireCRaiseEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FireCRaiseEvent)

  - [`PyMonitoring_FireReraiseEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FireReraiseEvent)

  - [`PyMonitoring_FireExceptionHandledEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FireExceptionHandledEvent)

  - [`PyMonitoring_FirePyUnwindEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FirePyUnwindEvent)

  - [`PyMonitoring_FireStopIterationEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FireStopIterationEvent)

  - [`PyMonitoring_EnterScope()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_EnterScope)

  - [`PyMonitoring_ExitScope()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_ExitScope)

(Contributed by Irit Katriel in [gh-111997](https://github.com/python/cpython/issues/111997)).

- Add [`PyMutex`](https://docs.python.org/3.14/c-api/synchronization.html#c.PyMutex), a compact mutex taking up only one byte, together with the new [`PyMutex_Lock()`](https://docs.python.org/3.14/c-api/synchronization.html#c.PyMutex_Lock) and [`PyMutex_Unlock()`](https://docs.python.org/3.14/c-api/synchronization.html#c.PyMutex_Unlock) functions. Should the operation have to block, `PyMutex_Lock()` releases the [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) when it is held at the time. (Contributed by Sam Gross in [gh-108724](https://github.com/python/cpython/issues/108724).)

- Add the [PyTime C API](https://docs.python.org/3.14/c-api/time.html#c-api-time) to expose the system clocks:

  - [`PyTime_t`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_t).

  - [`PyTime_MIN`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_MIN) and [`PyTime_MAX`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_MAX).

  - [`PyTime_AsSecondsDouble()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_AsSecondsDouble).

  - [`PyTime_Monotonic()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_Monotonic).

  - [`PyTime_MonotonicRaw()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_MonotonicRaw).

  - [`PyTime_PerfCounter()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_PerfCounter).

  - [`PyTime_PerfCounterRaw()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_PerfCounterRaw).

  - [`PyTime_Time()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_Time).

  - [`PyTime_TimeRaw()`](https://docs.python.org/3.14/c-api/time.html#c.PyTime_TimeRaw).

(Contributed by Victor Stinner and Petr Viktorin in [gh-110850](https://github.com/python/cpython/issues/110850).)

- Add the [`PyDict_ContainsString()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_ContainsString) function, which acts just like [`PyDict_Contains()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_Contains) except that *key* is given as a const char* UTF-8 encoded bytes string in place of a [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)*. (Contributed by Victor Stinner in [gh-108314](https://github.com/python/cpython/issues/108314).)

- Add the [`PyDict_GetItemRef()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_GetItemRef) and [`PyDict_GetItemStringRef()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_GetItemStringRef) functions, whose behavior resembles [`PyDict_GetItemWithError()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_GetItemWithError) but yields a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) rather than a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference). On top of that, they signal an error by returning `-1`, so checking `PyErr_Occurred()` becomes unnecessary. (Contributed by Victor Stinner in [gh-106004](https://github.com/python/cpython/issues/106004).)

- Add the [`PyDict_SetDefaultRef()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_SetDefaultRef) function, whose behavior resembles [`PyDict_SetDefault()`](https://docs.python.org/3.14/c-api/dict.html#c.PyDict_SetDefault) but yields a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) rather than a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference). It returns `-1` on error, `0` when an insertion happens, and `1` if the dictionary already held the key. (Contributed by Sam Gross in [gh-112066](https://github.com/python/cpython/issues/112066).)

-

[Subject index](INDEX.md) · [Previous source section](cpython-bytecode-changes.md) · [Release/subject declaration](summary-release-highlights.md) · [Following release/subject continuation](dictionary-removal-and-c-api-additions.md)
