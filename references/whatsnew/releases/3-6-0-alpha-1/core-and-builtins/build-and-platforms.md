# Python 3.6.0 alpha 1 / core and builtins / build and platforms

[bpo-25003](https://bugs.python.org/issue?@action=redirect&bpo=25003): Starting with Solaris 11.3, os.urandom() now reaches for the getrandom() function in place of getentropy(). getentropy() blocks while it produces very high quality entropy, and os.urandom() has no need for entropy of that caliber.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
