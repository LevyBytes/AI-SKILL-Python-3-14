# Python 3.8.0 alpha 1 / library / build and platforms

[bpo-31425](https://bugs.python.org/issue?@action=redirect&bpo=31425): Support sockets belonging to the AF_QIPCRTR address family that the Linux kernel provides. It serves to talk with services like GPS or radio that run on Qualcomm hardware. Patch by Bjorn Andersson.

[bpo-33542](https://bugs.python.org/issue?@action=redirect&bpo=33542): Stop `uuid.get_node` from picking up a DUID rather than a MAC under Windows. Patch by Zvi Effron

[bpo-28167](https://bugs.python.org/issue?@action=redirect&bpo=28167): Drop platform.linux_distribution, deprecated ever since 3.5.

[bpo-32493](https://bugs.python.org/issue?@action=redirect&bpo=32493): Fixed the test for `uuid_enc_be` availability inside `configure.ac`. Patch by Michael Felt.

[bpo-28167](https://bugs.python.org/issue?@action=redirect&bpo=28167): The `platform.linux_distribution` and `platform.dist` functions now emit a `DeprecationWarning` and stand slated for removal in Python 3.8

[bpo-33281](https://bugs.python.org/issue?@action=redirect&bpo=33281): Repair a ctypes.util.find_library regression seen on macOS.

[bpo-34563](https://bugs.python.org/issue?@action=redirect&bpo=34563): On Windows, corrected multiprocessing.Connection for very large reads: fixed _winapi.PeekNamedPipe() and _winapi.ReadFile() for reads exceeding INT_MAX (typically `2**31-1`).

[bpo-23057](https://bugs.python.org/issue?@action=redirect&bpo=23057): Release the Proactor event loop from blocking once a keyboard interrupt arrives on Windows

[bpo-35371](https://bugs.python.org/issue?@action=redirect&bpo=35371): Corrected a possible crash in `os.utime()` on Windows triggered by passing incorrect arguments.

[bpo-31047](https://bugs.python.org/issue?@action=redirect&bpo=31047): Corrected an `ntpath.abspath` regression where a trailing separator was left in place on Windows. Patch by Tim Graham.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
