# Python 3.7.0 alpha 1 / library / ttk repair destroy method labeledscale optionmenu classes

[bpo-31135](https://bugs.python.org/issue?@action=redirect&bpo=31135): ttk: repair the destroy() method on the LabeledScale and OptionMenu classes. The parent destroy() method now runs even when the used attribute is absent. The LabeledScale.destroy() method now also clears the label and scale attributes explicitly so the garbage collector can dispose of every widget.

[Subject index](INDEX.md) · [Release version, date and status](../../release-overview/overview.md)
