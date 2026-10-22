# Python 3.11.0 alpha 4 / library / text and unicode

[bpo-45874](https://bugs.python.org/issue?@action=redirect&bpo=45874): The empty query string, one that holds no query arguments, is now processed properly by `urllib.parse.parse_qsl`. Previously this triggered problems whenever strict parsing was turned on.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
