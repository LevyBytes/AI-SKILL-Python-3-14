# Python 3.7.0 alpha 1 / idle / tests and documentation

[bpo-6739](https://bugs.python.org/issue?@action=redirect&bpo=6739): IDLE: Confirm user-entered key sequences by attempting to bind them through tk. Add tests for all 3 validation functions. G Polo wrote the first version of the patch. Cheryl Sabella added the tests.

[bpo-30642](https://bugs.python.org/issue?@action=redirect&bpo=30642): Repair reference leaks within the IDLE tests. Louie Lu and Terry Jan Reedy supplied the patches.

[bpo-30290](https://bugs.python.org/issue?@action=redirect&bpo=30290): Help-about: adopt pep8 names and add tests. Raise coverage to 100%. Louie Lu, Cheryl Sabella, and Terry Jan Reedy supplied the patches.

[bpo-30303](https://bugs.python.org/issue?@action=redirect&bpo=30303): Add a _utest option to textview; add new tests. Raise coverage to 100%. Louie Lu and Terry Jan Reedy supplied the patches.

[bpo-31480](https://bugs.python.org/issue?@action=redirect&bpo=31480): IDLE - let the tests succeed while the zzdummy extension stays disabled by default.

[bpo-31001](https://bugs.python.org/issue?@action=redirect&bpo=31001): Supply tests covering the configdialog highlight tab. Cheryl Sabella supplied the patch.

[bpo-31205](https://bugs.python.org/issue?@action=redirect&bpo=31205): IDLE: Split a KeysPage(Frame) class out of ConfigDialog. The lightly adjusted tests still pass. Cheryl Sabella supplied the patch.

[bpo-31002](https://bugs.python.org/issue?@action=redirect&bpo=31002): Supply tests covering the configdialog keys tab. Cheryl Sabella supplied the patch.

[bpo-31050](https://bugs.python.org/issue?@action=redirect&bpo=31050): Split a GenPage(Frame) class out of ConfigDialog. The lightly adjusted tests still pass. Cheryl Sabella supplied the patch.

[bpo-31004](https://bugs.python.org/issue?@action=redirect&bpo=31004): IDLE - Split a FontPage(Frame) class out of ConfigDialog. The lightly adjusted tests still pass. Repair the General tests. Cheryl Sabella supplied most of the patch.

[bpo-31060](https://bugs.python.org/issue?@action=redirect&bpo=31060): IDLE - Wrap up the reorganization of ConfigDialog methods. Clustering the methods that belong to each tab and to the buttons will help with writing tests and refining the tabs, and it will make splitting the clusters into classes possible.

[bpo-31003](https://bugs.python.org/issue?@action=redirect&bpo=31003): IDLE: Supply more tests for the General tab.

[bpo-30993](https://bugs.python.org/issue?@action=redirect&bpo=30993): IDLE - Refine the configdialog font page along with its tests. Within configdialog: spell out causal pathways inside the create_font_tab docstring. Trim some attribute names. Relocate set_samples calls into var_changed_font (an idea from Cheryl Sabella). Move related functions so they sit after the create widgets function. Within test_configdialog: repair test_font_set so it no longer depends on order. Repair the renamed test_indent_scale so it actually exercises the widget. Tweak tests to track the moved set_samples call. Add tests covering the load functions. Group every font test into one class and the tab indent tests into another. Apart from two lines, these tests fully cover the related functions.

[bpo-30981](https://bugs.python.org/issue?@action=redirect&bpo=30981): IDLE – Supply additional configdialog font page tests.

[bpo-30917](https://bugs.python.org/issue?@action=redirect&bpo=30917): Supply tests for idlelib.config.IdleConf. Push coverage up from 46% to 96%. Louie Lu supplied the patch.

[bpo-30899](https://bugs.python.org/issue?@action=redirect&bpo=30899): IDLE: Supply tests for the ConfigParser subclasses in config. Louie Lu supplied the patch.

[bpo-30495](https://bugs.python.org/issue?@action=redirect&bpo=30495): IDLE: Refine textview using docstrings, PEP8 names, and additional tests. Cheryl Sabella supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
