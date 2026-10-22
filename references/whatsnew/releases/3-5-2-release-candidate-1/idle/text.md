# Python 3.5.2 release candidate 1 / idle / text

[bpo-5124](https://bugs.python.org/issue?@action=redirect&bpo=5124): On X11, pasting while text is selected now overwrites that selection. The behavior aligns with how pasting already works on Windows, Mac, the bulk of modern Linux applications, and ttk widgets. Serhiy Storchaka authored the original patch.

[bpo-27117](https://bugs.python.org/issue?@action=redirect&bpo=27117): Got the colorizer htest and turtledemo cooperating with dark themes. The logic that configures text widget colors moved into a new function.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
