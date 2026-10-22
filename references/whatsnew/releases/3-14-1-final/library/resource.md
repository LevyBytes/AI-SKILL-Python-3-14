# Python 3.14.1 final / library / resource

[gh-137044](https://github.com/python/cpython/issues/137044): In [`resource.getrlimit()`](https://docs.python.org/3.14/library/resource.html#resource.getrlimit), large limit values come back as positive integers in place of negative ones. For [`resource.setrlimit()`](https://docs.python.org/3.14/library/resource.html#resource.setrlimit), large values are accepted while negative ones are turned away (with [`RLIM_INFINITY`](https://docs.python.org/3.14/library/resource.html#resource.RLIM_INFINITY) as the exception).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
