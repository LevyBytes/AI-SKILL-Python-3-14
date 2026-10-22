# Python 3.10.0 alpha 1 / library / site

[bpo-33689](https://bugs.python.org/issue?@action=redirect&bpo=33689): Skip blank or whitespace-only lines within .pth files, which lines up with the documented behavior. Previously, blank lines made the site-packages directory show up more than once in sys.path. Ido Michael authored this, with Malcolm Smith and Tal Einat contributing.

[bpo-33944](https://bugs.python.org/issue?@action=redirect&bpo=33944): Added tracing of site-packages within site.py when verbose mode is on.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
