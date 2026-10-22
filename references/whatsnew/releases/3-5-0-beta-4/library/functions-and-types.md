# Python 3.5.0 beta 4 / library / functions and types

[bpo-24683](https://bugs.python.org/issue?@action=redirect&bpo=24683): Repaired crashes in _json functions invoked with arguments whose type was inappropriate.

[bpo-22485](https://bugs.python.org/issue?@action=redirect&bpo=22485): Corrected a defect that made `inspect.getsource` produce wrong output on nested functions.

[bpo-18622](https://bugs.python.org/issue?@action=redirect&bpo=18622): A call to unittest.mock.mock_open().reset_mock would recurse without end. Nicola Palumbo and Laurent De Buyst submitted the patch.

[bpo-15014](https://bugs.python.org/issue?@action=redirect&bpo=15014): The optional initial-response argument from RFC 4954 for the SMTP AUTH command is now honored by SMTP.auth() and SMTP.login().

[bpo-24669](https://bugs.python.org/issue?@action=redirect&bpo=24669): Repair inspect.getsource() so it handles "async def" functions. Kai Groner supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
