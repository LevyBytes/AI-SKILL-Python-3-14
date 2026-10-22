# Python 3.7.0 alpha 3 / c api / exceptions and tracebacks

[bpo-25612](https://bugs.python.org/issue?@action=redirect&bpo=25612): Relocate the active exception state out of the frame object and into the co-routine. Doing so simplifies the interpreter and clears up a couple of obscure bugs that arose from swapping exception state on entry to or exit from a generator.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
