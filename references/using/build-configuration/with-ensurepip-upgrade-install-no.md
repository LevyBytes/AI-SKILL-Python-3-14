# --with-ensurepip=[upgrade/install/no]

--with-ensurepip=[upgrade|install|no]

Pick which [`ensurepip`](https://docs.python.org/3.14/library/ensurepip.html#module-ensurepip) command runs during Python installation:

- `upgrade` (default): runs the `python -m ensurepip --altinstall --upgrade` command.

- `install`: runs the `python -m ensurepip --altinstall` command;

- `no`: skips ensurepip;

Added in version 3.6.

[Subject index](INDEX.md) · [Previous source section](disable-test-modules.md) · [Following source section](performance-options.md)
