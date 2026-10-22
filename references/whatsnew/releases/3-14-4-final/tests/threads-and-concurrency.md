# Python 3.14.4 final / tests / threads and concurrency

[gh-146202](https://github.com/python/cpython/issues/146202): A regrtest race condition is corrected by guaranteeing the temporary directory gets created inside the worker process. Earlier, temp_cwd() was able to fail on Windows whenever the "build" directory had not been created. Victor Stinner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
