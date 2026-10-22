# Python 3.6.0 beta 1 / library / random

[bpo-27706](https://bugs.python.org/issue?@action=redirect&bpo=27706): Bring back deterministic random.Random().seed() behavior for string seeds under seeding version 1. This lets a series of random() calls line up exactly with what Python 2 yielded. Nofar Schnider wrote the patch.

[bpo-22233](https://bugs.python.org/issue?@action=redirect&bpo=22233): Email header lines are split *only* at the CR and LF characters mandated by the RFC, never at any random unicode line break. A bug in HTTP header parsing gets corrected by the same change.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
