# Python 3.6.3 release candidate 1 / library / functions and types

[bpo-31135](https://bugs.python.org/issue?@action=redirect&bpo=31135): ttk: the destroy() method on the LabeledScale and OptionMenu classes was repaired. The parent destroy() now runs even when the relevant used attribute is absent. To assist the garbage collector in tearing down every widget, LabeledScale.destroy() additionally wipes the label and scale attributes outright.

[bpo-31107](https://bugs.python.org/issue?@action=redirect&bpo=31107): Corrected the mangled attribute computation in `copyreg._slotnames()` for any class whose name opens with an underscore. Shane Harvey supplied the patch.

[bpo-30879](https://bugs.python.org/issue?@action=redirect&bpo=30879): When handed a bytes-like argument, os.listdir() together with os.scandir() now yield names as bytes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
