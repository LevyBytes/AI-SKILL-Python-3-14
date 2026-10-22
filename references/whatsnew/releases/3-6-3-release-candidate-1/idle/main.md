# Python 3.6.3 release candidate 1 / idle / main

[bpo-30779](https://bugs.python.org/issue?@action=redirect&bpo=30779): IDLE: Extract the ConfigChanges class from configdialog and house it in config; test. * Within config, place the dump test code inside a function; execute it together with unittest under `if __name__ == '__main__'`. * Add the class config.ConfigChanges, derived from changes_class_v4.py on the bpo issue. * Add the class test_config.ChangesTest, drawing partly on configdialog_tests_v1.py. * Rework configdialog to lean on ConfigChanges; consult tracker msg297804. * Rework test_configdialog to track the configdialog changes. * Strip out configdialog functions that went unused or migrated to ConfigChanges. Portions of the patch came from Cheryl Sabella.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
