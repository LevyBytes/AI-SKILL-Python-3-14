# Python 3.5.1 release candidate 1 / core and builtins / build and platforms

[bpo-25003](https://bugs.python.org/issue?@action=redirect&bpo=25003): Running on Solaris 11.3 or later, os.urandom() now calls the getrandom() function rather than the getentropy() function. Because getentropy() blocks while producing very high quality entropy, and os.urandom() does not require entropy of that grade.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
