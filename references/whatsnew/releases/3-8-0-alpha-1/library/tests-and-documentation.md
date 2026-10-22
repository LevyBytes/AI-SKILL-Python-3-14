# Python 3.8.0 alpha 1 / library / tests and documentation

[bpo-14117](https://bugs.python.org/issue?@action=redirect&bpo=14117): Applied small adjustments to turtledemo. The 'wikipedia' example has been renamed 'rosette', naming what it renders. The 'penrose' print output is trimmed. The '1024' output of 'tree' has been removed.

[bpo-33078](https://bugs.python.org/issue?@action=redirect&bpo=33078): Repair the OSX failure that the tests relying on sem_getvalue produced

[bpo-32568](https://bugs.python.org/issue?@action=redirect&bpo=32568): Brought select.epoll() and its documentation into agreement regarding *sizehint* and *flags*.

[bpo-35585](https://bugs.python.org/issue?@action=redirect&bpo=35585): Made building enums by value quicker, for example http.HTTPStatus(200).

[bpo-32947](https://bugs.python.org/issue?@action=redirect&bpo=32947): Add OP_ENABLE_MIDDLEBOX_COMPAT plus a test workaround for TLSv1.3 toward later compatibility with OpenSSL 1.1.1.

[bpo-32146](https://bugs.python.org/issue?@action=redirect&bpo=32146): Document how frozen executables interact with the spawn and forkserver start methods inside multiprocessing.

[bpo-34897](https://bugs.python.org/issue?@action=redirect&bpo=34897): The test.support.missing_compiler_executable check was adjusted so that a nominal command name of `''` gets ignored. Michael Felt wrote the patch.

[bpo-35079](https://bugs.python.org/issue?@action=redirect&bpo=35079): Sharpen the difflib.SequenceManager.get_matching_blocks documentation by introducing "non-overlapping" and swapping "!=" for "<".

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
