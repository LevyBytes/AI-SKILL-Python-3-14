# Python 3.11.0 alpha 6 / tests / zlib

[bpo-46623](https://bugs.python.org/issue?@action=redirect&bpo=46623): Bypass test_pair() and test_speech128() within test_zlib on s390x, given that they fail when zlib relies on the s390x hardware accelerator. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
