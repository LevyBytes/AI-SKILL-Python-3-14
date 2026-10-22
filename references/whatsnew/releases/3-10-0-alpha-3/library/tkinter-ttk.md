# Python 3.10.0 alpha 3 / library / tkinter ttk

[bpo-42328](https://bugs.python.org/issue?@action=redirect&bpo=42328): Repaired [`tkinter.ttk.Style.map()`](https://docs.python.org/3.14/library/tkinter.ttk.html#tkinter.ttk.Style.map). The function now takes the default-state representation as an empty sequence (the same shape `Style.map()` returns). Its result now has identical structure on every platform and is no longer affected by the value of `wantobjects`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
