# What's New In Python 3.7 / Build Changes — ctypes, ssl, threading

### Build Changes

The ability to build `--without-threads` has been dropped. The [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module is now present at all times. (Contributed by Antoine Pitrou in [bpo-31370](https://bugs.python.org/issue?@action=redirect&bpo=31370).).

On non-OSX UNIX platforms, a complete copy of libffi is no longer shipped for use while building the [`_ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) module. Building `_ctypes` on those platforms now demands that a copy of libffi already be installed. (Contributed by Zachary Ware in [bpo-27979](https://bugs.python.org/issue?@action=redirect&bpo=27979).)

To fetch external sources, the Windows build process no longer leans on Subversion; instead a Python script downloads zipfiles from GitHub. When Python 3.6 cannot be located on the machine (through `py -3.6`), NuGet fetches a 32-bit Python copy for that role. (Contributed by Zachary Ware in [bpo-30450](https://bugs.python.org/issue?@action=redirect&bpo=30450).)

A libssl compatible with either OpenSSL 1.0.2 or 1.1 is required by the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module. Having reached end of lifetime on 2016-12-31, OpenSSL 1.0.1 is no longer supported. For the moment LibreSSL is also unsupported, as LibreSSL releases through version 2.6.4 lack the required OpenSSL 1.0.2 APIs.

[Subject index](INDEX.md) · [Previous source section](c-api-changes.md) · [Next source section](optimizations.md) · [Release/subject declaration](summary-release-highlights.md)
