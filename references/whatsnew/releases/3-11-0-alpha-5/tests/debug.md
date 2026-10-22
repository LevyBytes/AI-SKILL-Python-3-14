# Python 3.11.0 alpha 5 / tests / debug

[bpo-46542](https://bugs.python.org/issue?@action=redirect&bpo=46542): Stop a Python crash in test_lib2to3 on a debug-mode Python build by capping the recursion limit. Victor Stinner authored the patch.

[bpo-46576](https://bugs.python.org/issue?@action=redirect&bpo=46576): test_peg_generator now turns off compiler optimization while testing compilation of its own C extensions, which markedly accelerates the testing on non-debug builds of CPython.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
