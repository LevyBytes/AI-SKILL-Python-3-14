# Python 3.10.0 beta 1 / windows / build and platforms

[bpo-40432](https://bugs.python.org/issue?@action=redirect&bpo=40432): The pegen regeneration script on Windows was updated so it locates and runs Python 3.8 or above. Regeneration already needed 3.8 or newer beforehand, yet the script could end up invoking older Python releases.

[bpo-43745](https://bugs.python.org/issue?@action=redirect&bpo=43745): The Windows release is now genuinely bumped to OpenSSL 1.1.1k. Prior builds carried the wrong label and in fact shipped 1.1.1i once more.

[bpo-43652](https://bugs.python.org/issue?@action=redirect&bpo=43652): Within the Windows installer, Tcl and Tk were updated to 8.6.11.

[bpo-43492](https://bugs.python.org/issue?@action=redirect&bpo=43492): The Windows installer was moved up to SQLite 3.35.5.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
