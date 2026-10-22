# Python 3.9.0 alpha 2 / security / uu

[bpo-38945](https://bugs.python.org/issue?@action=redirect&bpo=38945): During uu encoding, newline characters are now escaped so they cannot spill over into the content portion of the encoded file. This blocks malicious or accidental tampering with the data while it is being decoded.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
