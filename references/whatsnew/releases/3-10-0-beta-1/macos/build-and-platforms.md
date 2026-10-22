# Python 3.10.0 beta 1 / macos / build and platforms

[bpo-44009](https://bugs.python.org/issue?@action=redirect&bpo=44009): A "python3.x-intel64" executable is now provided so that macOS universal2 framework builds can be forced reliably to run under Rosetta 2 Intel-64 emulation on Apple Silicon Macs. That comes in handy for testing or when universal2 wheels have not yet shipped.

[bpo-43851](https://bugs.python.org/issue?@action=redirect&bpo=43851): On macOS, SQLite is now compiled with `SQLITE_OMIT_AUTOINIT`. Erlend E. Aasland supplied the patch.

[bpo-43492](https://bugs.python.org/issue?@action=redirect&bpo=43492): The macOS installer was moved to SQLite 3.35.4.

[bpo-42235](https://bugs.python.org/issue?@action=redirect&bpo=42235): When building on macOS 10.15 or newer, `Mac/BuildScript/build-installer.py` will now apply `--enable-optimizations` together with `--with-lto`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
