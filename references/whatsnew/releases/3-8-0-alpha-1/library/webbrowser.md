# Python 3.8.0 alpha 1 / library / webbrowser

[bpo-34019](https://bugs.python.org/issue?@action=redirect&bpo=34019): webbrowser: Fixed the arguments handed to Opera Browser when launching a fresh URL through the `webbrowser` module. Patch by Bumsik Kim.

[bpo-31014](https://bugs.python.org/issue?@action=redirect&bpo=31014): Corrected the creation of a controller for [`webbrowser`](https://docs.python.org/3.14/library/webbrowser.html#module-webbrowser) whenever a user points the BROWSER environment variable at an entry's path. Based on patch by John Still.

[bpo-35308](https://bugs.python.org/issue?@action=redirect&bpo=35308): Corrected a `webbrowser` regression in which default browsers could take precedence over the browsers named in the `BROWSER` environment variable.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
