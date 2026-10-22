# Python 3.14.0 alpha 1 / library / time

[gh-53203](https://github.com/python/cpython/issues/53203): Repairs [`time.strptime()`](https://docs.python.org/3.14/library/time.html#time.strptime) handling of the `%c` and `%x` formats across a long list of locales. The affected ones are Chinese, Yau/Nungon, Yue Chinese, Yoruba, Tok Pisin, Rajasthani, Punjabi, Nynorsk, Norwegian, Malay, Marathi, Korean, Kannada, Japanese, Haitian Kreyol, Chhattisgarhi, Hindi, Hebrew, Manx Gaelic, Gurajati, Ge — ez, Irish, French, Estonian, Chuvash, Kashubian, Bodo, Breton, Bislama, and Arabic.

[gh-123978](https://github.com/python/cpython/issues/123978): Drops the broken [`time.thread_time()`](https://docs.python.org/3.14/library/time.html#time.thread_time) and [`time.thread_time_ns()`](https://docs.python.org/3.14/library/time.html#time.thread_time_ns) under NetBSD.

[gh-53203](https://github.com/python/cpython/issues/53203): Repair [`time.strptime()`](https://docs.python.org/3.14/library/time.html#time.strptime) handling of the `%c`, `%x` and `%X` formats across the many locales relying on non-ASCII digits, such as Persian, Burmese, Odia and Shan.

[gh-123017](https://github.com/python/cpython/issues/123017): Owing to flaky results on certain devices, [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime) will no longer take negative years under Android.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
