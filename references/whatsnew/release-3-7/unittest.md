# What's New In Python 3.7 / unittest

### unittest

A freshly added `-k` command-line option lets you restrict the tests to those whose names contain a substring or match a Unix shell-like pattern. As an illustration, `python -m unittest -k foo` would run `foo_tests.SomeTest.test_something`, `bar_tests.SomeTest.test_foo`, yet skip `bar_tests.FooTest.test_something`. (Contributed by Jonas Haag in [bpo-32071](https://bugs.python.org/issue?@action=redirect&bpo=32071).)

[Subject index](INDEX.md) · [Previous source section](unicodedata.md) · [Next source section](unittest-mock.md) · [Release/subject declaration](summary-release-highlights.md)
