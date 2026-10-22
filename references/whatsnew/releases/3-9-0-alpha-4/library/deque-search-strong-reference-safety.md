# Python 3.9.0 alpha 4 / library / collections deque keeps strong references throughout deque contains deque count prevents crashes

[bpo-39590](https://bugs.python.org/issue?@action=redirect&bpo=39590): Collections.deque now keeps strong references throughout deque.__contains__ and deque.count, which prevents crashes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
