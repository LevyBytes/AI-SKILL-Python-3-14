# Python 3.7.0 alpha 4 / core and builtins / compiler and parser

[bpo-32390](https://bugs.python.org/issue?@action=redirect&bpo=32390): Repair the compilation failure on AIX that arose once the f_fsid field joined the object os.statvfs() returns ([bpo-32143](https://bugs.python.org/issue?@action=redirect&bpo=32143)). Michael Felt wrote the original patch.

[bpo-31650](https://bugs.python.org/issue?@action=redirect&bpo=31650): Carry out [**PEP 552**](https://peps.python.org/pep-0552/) (Deterministic pycs). Bytecode cache files can now be invalidated by Python based on a hash of the source content instead of the source last-modified time.

[bpo-29469](https://bugs.python.org/issue?@action=redirect&bpo=29469): Relocate constant folding off the bytecode layer onto the AST layer. Eugene Toder wrote the original patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
