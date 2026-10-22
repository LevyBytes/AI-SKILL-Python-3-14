# Python 3.6.5 release candidate 1 / library / files and paths

[bpo-21060](https://bugs.python.org/issue?@action=redirect&bpo=21060): The puzzling setup.py upload notice was reworded from “No dist file created in earlier command” into the clearer “Must create and upload files in one command”.

[bpo-32228](https://bugs.python.org/issue?@action=redirect&bpo=32228): Make `truncate()` keep the file position intact (the value `tell()` reports) following writes that exceed the buffer size.

[bpo-32255](https://bugs.python.org/issue?@action=redirect&bpo=32255): When a lone empty field gets written into a CSV file it is now always quoted. That makes it possible to tell an empty row apart from a row holding one empty field. Licht Takeuchi supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
