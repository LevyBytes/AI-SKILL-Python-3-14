# Python 3.11.0 alpha 1 / tests / platform

[bpo-45052](https://bugs.python.org/issue?@action=redirect&bpo=45052): The `WithProcessesTestSharedMemory.test_shared_memory_basics` test had been disabled because its `self.assertEqual(sms.size, sms2.size)` line kept failing. That line is now gone and the test runs once more.

The chief reason for dropping that line from the test is that the `size` of `SharedMemory` carries no guarantee of staying identical. The platform decides it.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
