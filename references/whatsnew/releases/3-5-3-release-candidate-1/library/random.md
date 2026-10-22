# Python 3.5.3 release candidate 1 / library / random

[bpo-27706](https://bugs.python.org/issue?@action=redirect&bpo=27706): Brought back the deterministic behaviour of random.Random().seed() for string seeds when seeding version 1 is used. Call sequences to random() will then line up precisely with what Python 2 produced. Nofar Schnider contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
