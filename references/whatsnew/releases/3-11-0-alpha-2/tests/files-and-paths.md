# Python 3.11.0 alpha 2 / tests / files and paths

[bpo-45403](https://bugs.python.org/issue?@action=redirect&bpo=45403): Repair test_sys.test_stdlib_dir() for builds outside the source tree by comparing normalized paths. Victor Stinner contributed the patch.

[bpo-45400](https://bugs.python.org/issue?@action=redirect&bpo=45400): Repair test_name_error_suggestions_do_not_trigger_for_too_many_locals() of test_exceptions whenever a directory name carries “a1” (such as “Python-3.11.0a1”): apply a tighter regular expression. Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
