# Python 3.8.0 alpha 3 / library / text and unicode

[bpo-36297](https://bugs.python.org/issue?@action=redirect&bpo=36297): The "unicode_internal" codec has been dropped. Its deprecation dated back to Python 3.3. Inada Naoki wrote the patch.

[bpo-36280](https://bugs.python.org/issue?@action=redirect&bpo=36280): Give ast.Constant a kind field. Its value is "u" should the literal bear a "u" prefix (that is, a Python 2 style unicode literal); otherwise it is None.

[bpo-36251](https://bugs.python.org/issue?@action=redirect&bpo=36251): Repair the format strings driving the stderrprinter and re.Match reprs. Stephan Hohe wrote the patch.

[bpo-35652](https://bugs.python.org/issue?@action=redirect&bpo=35652): `shutil.copytree(copy_function=...)` mistakenly handed a DirEntry over instead of a path string.

[bpo-35899](https://bugs.python.org/issue?@action=redirect&bpo=35899): Enum was repaired so it correctly copes with empty strings as well as strings containing non-Latin characters (for instance, `α`, `א`) without crashing. Maxwell contributed the original patch. Stéphane Wirtel helped out.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
