# Python 3.9.0 alpha 1 / tests / test venv test multiprocessing calls pool terminate explicitly waits pool finish

[bpo-37153](https://bugs.python.org/issue?@action=redirect&bpo=37153): `test_venv.test_multiprocessing()` now calls `pool.terminate()` explicitly so it waits for the pool to finish.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
