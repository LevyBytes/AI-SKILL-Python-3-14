# Python 3.8.0 alpha 1 / core and builtins / correct error handler used standard streams such sys stdout pythonioencoding

[bpo-34485](https://bugs.python.org/issue?@action=redirect&bpo=34485): Correct the error handler used by standard streams such as sys.stdout: PYTHONIOENCODING=?:? is now disregarded rather than forcing the error handler to ?strict?.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
