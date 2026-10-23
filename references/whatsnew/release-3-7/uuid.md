# What's New In Python 3.7 / uuid - uuid

### uuid

Whether produced UUIDs come from a multiprocessing-safe method is now reported by the freshly added [`UUID.is_safe`](https://docs.python.org/3.14/library/uuid.html#uuid.UUID.is_safe) attribute, which relays that fact from the platform. (Contributed by Barry Warsaw in [bpo-22807](https://bugs.python.org/issue?@action=redirect&bpo=22807).)

Universally administered MAC addresses are now preferred over locally administered ones by [`uuid.getnode()`](https://docs.python.org/3.14/library/uuid.html#uuid.getnode). This more strongly assures global uniqueness for the UUIDs that [`uuid.uuid1()`](https://docs.python.org/3.14/library/uuid.html#uuid.uuid1) yields. Should only locally administered MAC addresses exist, the first one encountered is returned. (Contributed by Barry Warsaw in [bpo-32107](https://bugs.python.org/issue?@action=redirect&bpo=32107).)

[Subject index](INDEX.md) · [Previous source section](uu.md) · [Next source section](warnings.md) · [Release/subject declaration](summary-release-highlights.md)
