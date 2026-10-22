# Python 3.9.0 alpha 1 / library / markup

[bpo-36564](https://bugs.python.org/issue?@action=redirect&bpo=36564): Cleared an infinite loop in the email header folding logic that fired whenever an email policy's max_line_length was too short to fit the mandatory markup together with any values present in the message. Paul Ganssle wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
