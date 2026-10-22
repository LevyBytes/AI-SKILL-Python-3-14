# test.support.os_helper: `test.support.os_helper.EnvironmentVarGuard`

*class *test.support.os_helper.EnvironmentVarGuard

A class for temporarily setting or clearing environment variables. Instances work as a context manager and present a full dictionary interface for reading from or altering the underlying `os.environ`. Once the context manager is left, every change this instance made to environment variables is undone.

Changed in version 3.1: Added dictionary interface.

[Subject index](INDEX.md) · [Previous](filesystem-encoding-test-names.md) · [Continue](fake-path-and-environment-guard-helpers.md) · [Owning module, declaration or section: test.support.os_helper](filesystem-encoding-test-names.md)
