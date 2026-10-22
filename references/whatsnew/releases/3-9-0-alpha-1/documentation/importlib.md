# Python 3.9.0 alpha 1 / documentation / importlib

[bpo-37521](https://bugs.python.org/issue?@action=redirect&bpo=37521): Repair the `importlib` examples so any freshly created module is placed via importlib.util.module_from_spec() into sys.modules right away, rather than once loader.exec_module() has run.

Credit goes to Benjamin Mintz, who spotted the bug.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
