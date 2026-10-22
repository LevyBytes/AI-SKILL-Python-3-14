# Python 3.6.0 beta 3 / library / numeric behavior

[bpo-27939](https://bugs.python.org/issue?@action=redirect&bpo=27939): Repaired bugs within tkinter.ttk.LabeledScale and tkinter.Scale that came from holding the scale internally as a float value in Tk. tkinter.IntVar now functions when a float value is assigned to the underlying Tk variable.

[bpo-18219](https://bugs.python.org/issue?@action=redirect&bpo=18219): Speed up csv.DictWriter when there is a large number of columns. Mariatta Wijaya wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
