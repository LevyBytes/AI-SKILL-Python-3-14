# What's New In Python 3.7 / unittest.mock — copy, pickle, unittest.mock

### unittest.mock

When the [`sentinel`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.sentinel) attributes are [`copied`](https://docs.python.org/3.14/library/copy.html#module-copy) or [`pickled`](https://docs.python.org/3.14/library/pickle.html#module-pickle), they now keep their identity intact. (Contributed by Serhiy Storchaka in [bpo-20804](https://bugs.python.org/issue?@action=redirect&bpo=20804).)

A freshly added [`seal()`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.seal) function lets you seal [`Mock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock) instances, preventing any additional attribute mocks from being created afterward. Sealing propagates recursively into every attribute that is itself a mock. (Contributed by Mario Corchero in [bpo-30541](https://bugs.python.org/issue?@action=redirect&bpo=30541).)

[Subject index](INDEX.md) · [Previous source section](unittest.md) · [Next source section](urllib-parse.md) · [Release/subject declaration](summary-release-highlights.md)
