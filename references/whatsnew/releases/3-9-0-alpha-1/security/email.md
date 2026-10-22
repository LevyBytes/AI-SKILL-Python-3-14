# Python 3.9.0 alpha 1 / security / email

[bpo-37764](https://bugs.python.org/issue?@action=redirect&bpo=37764): Correct email._header_value_parser.get_unstructured, which entered an infinite loop both for a particular case where the email header lacks trailing whitespace and for the case where it carries an invalid encoded word. Ashwin Ramaswami supplied the patch.

[bpo-37461](https://bugs.python.org/issue?@action=redirect&bpo=37461): Resolve an infinite loop that occurred while parsing specially crafted email headers. Abhilash Raj wrote the patch.

[bpo-34155](https://bugs.python.org/issue?@action=redirect&bpo=34155): Correct the parsing of invalid email addresses carrying more than one `@` (for example a@b@c.com.) so the portion ahead of the 2nd `@` is not returned as a valid email address. The patch came from maxking & jpic.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
