# Python 3.9.0 alpha 1 / library / email

[bpo-37491](https://bugs.python.org/issue?@action=redirect&bpo=37491): Cleared an `IndexError` that struck while email headers were parsed and a bare-quoted string value ended sooner than expected. Abhilash Raj authored the patch.

[bpo-33972](https://bugs.python.org/issue?@action=redirect&bpo=33972): A single-part email whose content-type is `multipart/*` no longer triggers an AttributeError.

[bpo-36520](https://bugs.python.org/issue?@action=redirect&bpo=36520): Long email headers carrying UTF-8 characters are now encoded correctly as they get folded. Jeffrey Kintscher wrote the patch.

[bpo-30835](https://bugs.python.org/issue?@action=redirect&bpo=30835): Cleared a defect in email parsing where a multipart message holding invalid bytes in its content-transfer-encoding could trigger an AttributeError. Andrew Donnellan authored the patch.

[bpo-32178](https://bugs.python.org/issue?@action=redirect&bpo=32178): Resolved an IndexError raised by the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package while it attempted to parse malformed address fields that begin with `:`.

[bpo-34002](https://bugs.python.org/issue?@action=redirect&bpo=34002): Boosted efficiency in portions of the email package by swapping while-pop for a for loop and relying on isdisjoint rather than set intersections.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
