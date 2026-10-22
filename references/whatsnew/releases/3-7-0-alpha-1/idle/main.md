# Python 3.7.0 alpha 1 / idle / main

[bpo-30779](https://bugs.python.org/issue?@action=redirect&bpo=30779): IDLE: Split a ConfigChanges class out of configdialog and place it in config; test it. * Within config, move the dump test code into a function; run that plus unittest under ‘if __name__ == ‘__main__’. * Add the config.ConfigChanges class derived from changes_class_v4.py on the bpo issue. * Add the test_config.ChangesTest class, drawing partly on configdialog_tests_v1.py. * Rework configdialog to lean on ConfigChanges; refer to tracker msg297804. * Rework test_configdialog to align with the configdialog changes. * Remove configdialog functions that went unused or migrated to ConfigChanges. Cheryl Sabella contributed parts of the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
