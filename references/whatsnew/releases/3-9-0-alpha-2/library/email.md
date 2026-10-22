# Python 3.9.0 alpha 2 / library / email

[bpo-38708](https://bugs.python.org/issue?@action=redirect&bpo=38708): Guard against a possible IndexError in the email parser while it parses an empty msg-id.

[bpo-38698](https://bugs.python.org/issue?@action=redirect&bpo=38698): Introduce a fresh `InvalidMessageID` token in the email parser to stand for malformed Message-ID headers. On top of that, record defects whenever value remains after the header has been parsed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
