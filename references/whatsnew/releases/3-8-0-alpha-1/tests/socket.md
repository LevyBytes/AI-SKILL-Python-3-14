# Python 3.8.0 alpha 1 / tests / socket

[bpo-34587](https://bugs.python.org/issue?@action=redirect&bpo=34587): test_socket: Drop RDSTest.testCongestion(). The test attempts to saturate the receiver's socket buffer and looks for an error. Yet the RDS protocol imposes no such requirement. What's more, the Linux RDS implementation expects the message producer to throttle its rate; triggering an error is not the receiver's job. By design the test fails on Fedora 28, so simply remove it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
