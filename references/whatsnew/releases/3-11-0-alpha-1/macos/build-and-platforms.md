# Python 3.11.0 alpha 1 / macos / build and platforms

[bpo-45007](https://bugs.python.org/issue?@action=redirect&bpo=45007): Move the macOS installer builds up to OpenSSL 1.1.1l.

[bpo-34602](https://bugs.python.org/issue?@action=redirect&bpo=34602): While compiling CPython on macOS via `./configure --with-undefined-behavior-sanitizer --with-pydebug`, the stack size now grows fourfold so the whole test suite is able to pass.

[bpo-44848](https://bugs.python.org/issue?@action=redirect&bpo=44848): Move the macOS installer up to SQLite 3.36.0.

[bpo-43109](https://bugs.python.org/issue?@action=redirect&bpo=43109): Let the --with-lto configure option operate alongside Apple-supplied Xcode or Command Line Tools.

[bpo-34932](https://bugs.python.org/issue?@action=redirect&bpo=34932): Provide socket.TCP_KEEPALIVE on macOS. Shane Harvey wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
