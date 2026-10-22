# Python 3.8.0 alpha 1 / library / base64

[bpo-33770](https://bugs.python.org/issue?@action=redirect&bpo=33770): made the base64 exception message clearer for encoded inputs whose length is invalid

[bpo-27397](https://bugs.python.org/issue?@action=redirect&bpo=27397): Got the email module to deal correctly with invalid-length base64 strings.

[bpo-34164](https://bugs.python.org/issue?@action=redirect&bpo=34164): For bad padding, [`base64.b32decode()`](https://docs.python.org/3.14/library/base64.html#base64.b32decode) used to raise UnboundLocalError or OverflowError. It now consistently raises `base64.Error` in such situations.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
