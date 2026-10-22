# Python 3.14.0 alpha 3 / core and builtins / threads and concurrency

[gh-124470](https://github.com/python/cpython/issues/124470): On free-threaded builds, stop the crash that happened when one thread swapped out an object dictionary while another was reading an attribute

[gh-109746](https://github.com/python/cpython/issues/109746): Should `_thread.start_new_thread()` be unable to launch a fresh thread, it now removes its own state from the interpreter, sidestepping the repeated cleanup that finalization would otherwise perform.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
