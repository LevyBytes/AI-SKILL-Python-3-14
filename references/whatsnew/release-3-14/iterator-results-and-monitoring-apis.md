# What's new in Python 3.14 / C API changes / New features in the C API — sys.monitoring

Introduce [`PyIter_NextItem()`](https://docs.python.org/3.14/c-api/iter.html#c.PyIter_NextItem) as a stand-in for [`PyIter_Next()`](https://docs.python.org/3.14/c-api/iter.html#c.PyIter_Next), whose return value is ambiguous. (Contributed by Irit Katriel and Erlend Aasland in [gh-105201](https://github.com/python/cpython/issues/105201).)

- Introduce the [`PyLong_GetSign()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_GetSign) function for fetching the sign of [`int`](https://docs.python.org/3.14/library/functions.html#int) objects. (Contributed by Sergey B Kirpichev in [gh-116560](https://github.com/python/cpython/issues/116560).)

- Introduce [`PyLong_IsPositive()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_IsPositive), [`PyLong_IsNegative()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_IsNegative) and [`PyLong_IsZero()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_IsZero); these report, respectively, whether a [`PyLongObject`](https://docs.python.org/3.14/c-api/long.html#c.PyLongObject) holds a positive, negative, or zero value. (Contributed by James Roy and Sergey B Kirpichev in [gh-126061](https://github.com/python/cpython/issues/126061).)

- Introduce fresh functions that move C `<stdint.h>` numbers to and from Python [`int`](https://docs.python.org/3.14/library/functions.html#int) objects:

  - [`PyLong_AsInt32()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsInt32)

  - [`PyLong_AsInt64()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsInt64)

  - [`PyLong_AsUInt32()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsUInt32)

  - [`PyLong_AsUInt64()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_AsUInt64)

  - [`PyLong_FromInt32()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromInt32)

  - [`PyLong_FromInt64()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromInt64)

  - [`PyLong_FromUInt32()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromUInt32)

  - [`PyLong_FromUInt64()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FromUInt64)

(Contributed by Victor Stinner in [gh-120389](https://github.com/python/cpython/issues/120389).)

- Introduce a fresh import-and-export API covering Python [`int`](https://docs.python.org/3.14/library/functions.html#int) objects ([**PEP 757**](https://peps.python.org/pep-0757/)):

  - [`PyLong_GetNativeLayout()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_GetNativeLayout)

  - [`PyLong_Export()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_Export)

  - [`PyLong_FreeExport()`](https://docs.python.org/3.14/c-api/long.html#c.PyLong_FreeExport)

  - [`PyLongWriter_Create()`](https://docs.python.org/3.14/c-api/long.html#c.PyLongWriter_Create)

  - [`PyLongWriter_Finish()`](https://docs.python.org/3.14/c-api/long.html#c.PyLongWriter_Finish)

  - [`PyLongWriter_Discard()`](https://docs.python.org/3.14/c-api/long.html#c.PyLongWriter_Discard)

(Contributed by Sergey B Kirpichev and Victor Stinner in [gh-102471](https://github.com/python/cpython/issues/102471).)

- Introduce [`PyMonitoring_FireBranchLeftEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FireBranchLeftEvent) and [`PyMonitoring_FireBranchRightEvent()`](https://docs.python.org/3.14/c-api/monitoring.html#c.PyMonitoring_FireBranchRightEvent), which raise [`BRANCH_LEFT`](https://docs.python.org/3.14/library/sys.monitoring.html#monitoring-event-BRANCH_LEFT) and [`BRANCH_RIGHT`](https://docs.python.org/3.14/library/sys.monitoring.html#monitoring-event-BRANCH_RIGHT) events respectively. (Contributed by Mark Shannon in [gh-122548](https://github.com/python/cpython/issues/122548).)

-

[Subject index](INDEX.md) · [Previous source section](c-api-startup-configuration-functions.md) · [Next source section](c-api-type-freezing-and-unicode-writer.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-python-configuration-c-api.md) · [Release/subject declaration](c-api-additions.md) · [Preceding release/subject continuation](c-api-additions.md)
