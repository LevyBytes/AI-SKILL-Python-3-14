# Python 3.6.6 release candidate 1 / library / ttk treeview insert may take iid whose boolean value false

[bpo-33096](https://bugs.python.org/issue?@action=redirect&bpo=33096): ttk.Treeview.insert may now take an iid whose boolean value is false. Be aware that iid=0 and iid=False end up identical. Garvit Khatri contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
