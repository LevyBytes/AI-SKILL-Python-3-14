# Python 3.10.0 alpha 3 / library / os

[bpo-42236](https://bugs.python.org/issue?@action=redirect&bpo=42236): Under Unix the [`os.device_encoding()`](https://docs.python.org/3.14/library/os.html#os.device_encoding) function now yields `'UTF-8'` in place of the device encoding whenever the [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode) is on.

[bpo-41625](https://bugs.python.org/issue?@action=redirect&bpo=41625): Surface `splice()` as [`os.splice()`](https://docs.python.org/3.14/library/os.html#os.splice) inside the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module. Pablo Galindo wrote the patch

[bpo-41001](https://bugs.python.org/issue?@action=redirect&bpo=41001): Add [`os.eventfd()`](https://docs.python.org/3.14/library/os.html#os.eventfd) as a low level interface onto Linux’s event notification file descriptor.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
