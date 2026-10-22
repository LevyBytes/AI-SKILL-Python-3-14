# Python 3.9.0 alpha 2 / library / compiler and parser

[bpo-38698](https://bugs.python.org/issue?@action=redirect&bpo=38698): Stop UnboundLocalError from surfacing inside parse_message_id.

Because parse_message_id() mistakenly referenced a token declared within an exception handler, parsing an invalid value raised `UnboundLocalError`. Claudiu Popa wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
