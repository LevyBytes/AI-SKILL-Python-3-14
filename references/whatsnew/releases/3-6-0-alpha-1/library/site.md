# Python 3.6.0 alpha 1 / library / site

[bpo-24633](https://bugs.python.org/issue?@action=redirect&bpo=24633): site-packages/README -> README.txt.

[bpo-26587](https://bugs.python.org/issue?@action=redirect&bpo=26587): .pth files handled by the site module may now name files (for instance zip files) to append onto sys.path.

[bpo-26099](https://bugs.python.org/issue?@action=redirect&bpo=26099): When the sitecustomize module can be imported but executing it raises an ImportError, the site module now writes an error to stderr. The same applies to usercustomize.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
