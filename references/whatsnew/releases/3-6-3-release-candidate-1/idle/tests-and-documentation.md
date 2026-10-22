# Python 3.6.3 release candidate 1 / idle / tests and documentation

[bpo-6739](https://bugs.python.org/issue?@action=redirect&bpo=6739): IDLE: Confirm key sequences a user typed by attempting to bind them through tk. Tests for each of the 3 validation functions were added. G Polo supplied the original patch. Cheryl Sabella contributed the tests.

[bpo-31480](https://bugs.python.org/issue?@action=redirect&bpo=31480): IDLE - get the tests passing while the zzdummy extension stays off by default.

[bpo-31001](https://bugs.python.org/issue?@action=redirect&bpo=31001): Supply tests covering the configdialog highlight tab. Cheryl Sabella wrote the patch.

[bpo-31205](https://bugs.python.org/issue?@action=redirect&bpo=31205): IDLE: Extract the KeysPage(Frame) class out of ConfigDialog. The lightly adjusted tests still pass. Cheryl Sabella wrote the patch.

[bpo-31002](https://bugs.python.org/issue?@action=redirect&bpo=31002): Supply tests covering the configdialog keys tab. Cheryl Sabella wrote the patch.

[bpo-31050](https://bugs.python.org/issue?@action=redirect&bpo=31050): Extract the GenPage(Frame) class out of ConfigDialog. The lightly adjusted tests still pass. Cheryl Sabella wrote the patch.

[bpo-31004](https://bugs.python.org/issue?@action=redirect&bpo=31004): IDLE - Extract the FontPage(Frame) class out of ConfigDialog. The lightly adjusted tests still pass. The General tests were repaired. Cheryl Sabella supplied most of the patch.

[bpo-31060](https://bugs.python.org/issue?@action=redirect&bpo=31060): IDLE - Wrap up reorganizing the ConfigDialog methods. Clustering the methods tied to each tab and to the buttons will help with writing tests, refining the tabs, and ultimately separating the clusters into classes.

[bpo-31003](https://bugs.python.org/issue?@action=redirect&bpo=31003): IDLE: Supply further tests for the General tab.

[bpo-30993](https://bugs.python.org/issue?@action=redirect&bpo=30993): IDLE - Refine the configdialog font page along with its tests. Within configdialog: spell out the causal pathways inside the create_font_tab docstring. Trim a few attribute names. Relocate the set_samples calls into var_changed_font (an idea owed to Cheryl Sabella). Shift related functions to sit after the create-widgets function. Within test_configdialog: repair test_font_set so its ordering no longer matters. Repair the renamed test_indent_scale so it actually exercises the widget. Tune the tests around the moved set_samples call. Supply tests for the load functions. Group every font test into one class and the tab-indent tests into a separate one. Aside from two lines, these tests fully exercise the associated functions.

[bpo-30981](https://bugs.python.org/issue?@action=redirect&bpo=30981): IDLE — Supply further configdialog font page tests.

[bpo-30917](https://bugs.python.org/issue?@action=redirect&bpo=30917): Supply tests for idlelib.config.IdleConf. Coverage climbs from 46% to 96%. Louie Lu wrote the patch.

[bpo-30899](https://bugs.python.org/issue?@action=redirect&bpo=30899): IDLE: Supply tests covering the ConfigParser subclasses within config. Louie Lu wrote the patch.

[bpo-30495](https://bugs.python.org/issue?@action=redirect&bpo=30495): IDLE: Refine textview with docstrings, PEP8 names, and additional tests. Cheryl Sabella wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
