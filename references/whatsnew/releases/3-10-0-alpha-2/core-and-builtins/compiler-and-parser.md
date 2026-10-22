# Python 3.10.0 alpha 2 / core and builtins / compiler and parser

[bpo-42214](https://bugs.python.org/issue?@action=redirect&bpo=42214): Resolved a potential crash within the PEG parser while testing for the ?!=? token inside the `barry_as_flufl` rule. Pablo Galindo supplied the patch.

[bpo-42206](https://bugs.python.org/issue?@action=redirect&bpo=42206): Forward and raise the errors that `PyAST_Validate()` produces within the parser.

[bpo-42123](https://bugs.python.org/issue?@action=redirect&bpo=42123): Execute the parser two separate times. The first pass switches off every rule that exists only to yield nicer error messages, gaining speed. Should a parse failure occur, a second pass runs the parser with those rules turned on.

[bpo-42093](https://bugs.python.org/issue?@action=redirect&bpo=42093): A new ?per opcode cache? mechanism backs the `LOAD_ATTR` instruction now, making it roughly 36% quicker. Pablo Galindo and Yury Selivanov supplied the patch.

[bpo-41979](https://bugs.python.org/issue?@action=redirect&bpo=41979): The PEG parser now permits star-unpacking for the targets of with items.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
