# Python 3.7.0 alpha 4 / library / files and paths

[bpo-32255](https://bugs.python.org/issue?@action=redirect&bpo=32255): When a lone empty field is written into a CSV file it is now always quoted. That lets an empty row be told apart from a row holding one single empty field. Licht Takeuchi supplied the patch.

[bpo-32441](https://bugs.python.org/issue?@action=redirect&bpo=32441): Hand back the new file descriptor (that is, the second argument) out of `os.dup2`. Formerly `None` came back every time.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
