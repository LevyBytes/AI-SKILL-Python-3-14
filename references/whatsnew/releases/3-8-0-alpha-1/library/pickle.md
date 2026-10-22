# Python 3.8.0 alpha 1 / library / pickle

[bpo-33209](https://bugs.python.org/issue?@action=redirect&bpo=33209): Conclude framing at the close of the C implementation of [`pickle.Pickler.dump()`](https://docs.python.org/3.14/library/pickle.html#pickle.Pickler.dump).

[bpo-23403](https://bugs.python.org/issue?@action=redirect&bpo=23403): `DEFAULT_PROTOCOL` within [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) was raised to 4. Protocol 4 appears in [**PEP 3154**](https://peps.python.org/pep-3154/) and has been on hand since Python 3.4. It delivers stronger performance and a smaller footprint than protocol 3, which arrived in Python 3.0.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
