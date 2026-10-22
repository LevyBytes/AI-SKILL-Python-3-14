# Python 3.9.0 alpha 2 / macos / posix

[bpo-37931](https://bugs.python.org/issue?@action=redirect&bpo=37931): Repaired a crash on OSX dynamic builds that struck when the posix module was re-initialized following a Py_Finalize if the environment had been altered since the earlier `import posix`. Benoît Hudson supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
