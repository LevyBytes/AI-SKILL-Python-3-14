# Python 3.8.0 alpha 1 / idle / tests and documentation

[bpo-35093](https://bugs.python.org/issue?@action=redirect&bpo=35093): Document the IDLE document viewer within the IDLE doc. Append a paragraph under “Help and preferences”, in the “Help sources” subsection.

[bpo-35088](https://bugs.python.org/issue?@action=redirect&bpo=35088): Refresh the idlelib.help.copy_string docstring. We henceforth rely on git plus backporting in place of hg and forward merging.

[bpo-33975](https://bugs.python.org/issue?@action=redirect&bpo=33975): Steer clear of tiny type while running htests. Because part of why human-viewed tests exist is to confirm that widgets look right, it matters that they appear identical during testing and when IDLE actually runs.

[bpo-33905](https://bugs.python.org/issue?@action=redirect&bpo=33905): Add a test covering idlelib.stackview.StackBrowser.

[bpo-33839](https://bugs.python.org/issue?@action=redirect&bpo=33839): IDLE: rework ToolTip together with CallTip, supplying both docs and test coverage

[bpo-33628](https://bugs.python.org/issue?@action=redirect&bpo=33628): IDLE: Tidy up codecontext.py alongside its test.

[bpo-32874](https://bugs.python.org/issue?@action=redirect&bpo=32874): Supply tests covering pyparse.

[bpo-32831](https://bugs.python.org/issue?@action=redirect&bpo=32831): Supply docstrings plus tests for codecontext.

[bpo-35641](https://bugs.python.org/issue?@action=redirect&bpo=35641): Format the `calltip` properly whenever the function carries no docstring.

[bpo-35598](https://bugs.python.org/issue?@action=redirect&bpo=35598): Refresh config_key: adopt PEP 8 names plus ttk widgets, promote certain objects to global scope, and append tests.

[bpo-35521](https://bugs.python.org/issue?@action=redirect&bpo=35521): Document IDLE’s editor code context feature. Append a few internal references within the IDLE doc.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
