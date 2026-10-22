# Python 3.10.0 alpha 1 / core and builtins / memory and lifetimes

[bpo-40958](https://bugs.python.org/issue?@action=redirect&bpo=40958): Closes a possible buffer overflow in the PEG parser while it collects details to report syntax errors. Pablo Galindo contributed the patch.

[bpo-40880](https://bugs.python.org/issue?@action=redirect&bpo=40880): An invalid memory read was fixed in the new parser as it inspects newlines inside string literals. Pablo Galindo authored this.

[bpo-40883](https://bugs.python.org/issue?@action=redirect&bpo=40883): A memory leak that occurred during f-string parsing in the new parser was resolved. Pablo Galindo wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
