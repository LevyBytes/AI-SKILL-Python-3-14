# Python 3.12.0 beta 1 / library / asyncio subprocess

[bpo-39744](https://bugs.python.org/issue?@action=redirect&bpo=39744): Arrange for [`asyncio.subprocess.Process.communicate()`](https://docs.python.org/3.14/library/asyncio-subprocess.html#asyncio.subprocess.Process.communicate) to shut the subprocess’s stdin even where the call passes `input=None`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
