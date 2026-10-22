# Python 3.11.0 alpha 3 / library / asyncio

[bpo-45711](https://bugs.python.org/issue?@action=redirect&bpo=45711): Have [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) normalize exceptions the moment they get captured through [`PyErr_Fetch()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Fetch), prior to storing them as an exc_info triplet. This aligns `asyncio` with the remainder of the codebase, where an exc_info triplet is consistently normalized.

[bpo-23819](https://bugs.python.org/issue?@action=redirect&bpo=23819): In asyncio, asserts were swapped for exceptions; Kumar Aditya provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
