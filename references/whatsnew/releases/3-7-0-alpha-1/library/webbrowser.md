# Python 3.7.0 alpha 1 / library / webbrowser

[bpo-24452](https://bugs.python.org/issue?@action=redirect&bpo=24452): Gave webbrowser the ability to drive Chrome under Mac OS X. Ned Batchelder provided the patch.

[bpo-29645](https://bugs.python.org/issue?@action=redirect&bpo=29645): Importing the webbrowser module was made faster, and webbrowser.register() is now thread-safe.

[bpo-23262](https://bugs.python.org/issue?@action=redirect&bpo=23262): Firefox 36+ along with derived browsers are now handled by the webbrowser module. The change derives from a patch by Oleg Broytman.

[bpo-24241](https://bugs.python.org/issue?@action=redirect&bpo=24241): Under an X environment, the webbrowser module now favors launching the default browser directly. On top of that, the webbrowser register() function carries a documented ‘preferred’ argument for naming the browsers that get() should hand back when called without arguments. David Steele wrote the patch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
