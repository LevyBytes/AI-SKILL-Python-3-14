# Python 3.13.0 alpha 2 / idle / imports and modules

[bpo-35668](https://bugs.python.org/issue?@action=redirect&bpo=35668): Supply docstrings for the IDLE debugger module. Two bugs are fixed as well: properly initialize `Idb.botframe` (which belongs in Bdb); and in `Idb.in_rpc_code`, verify that `prev_frame` is not `None` before using it. test_debugger is also expanded considerably.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
