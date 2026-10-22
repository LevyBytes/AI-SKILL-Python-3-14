# Python 3.7.0 alpha 1 / library / socket

[bpo-28480](https://bugs.python.org/issue?@action=redirect&bpo=28480): Repaired the socket module build failure that arose when multithreading was turned off.

[bpo-28399](https://bugs.python.org/issue?@action=redirect&bpo=28399): Deleted the UNIX socket from the FS ahead of binding. Коренберг Марк provided the patch.

[bpo-27906](https://bugs.python.org/issue?@action=redirect&bpo=27906): Closed socket accept exhaustion that surfaced under heavy TCP traffic. Kevin Conway provided the patch.

[bpo-30987](https://bugs.python.org/issue?@action=redirect&bpo=30987): Support for the CAN ISO-TP protocol was added to the socket module.

[bpo-27584](https://bugs.python.org/issue?@action=redirect&bpo=27584): `AF_VSOCK` was added to the socket interface, enabling communication between virtual machines and the host they run on.

[bpo-29743](https://bugs.python.org/issue?@action=redirect&bpo=29743): An open socket was leaking when the transport got closed mid-handshake. Nikolay Kim supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
