# Python 3.9.0 alpha 1 / library / constants

[bpo-37345](https://bugs.python.org/issue?@action=redirect&bpo=37345): Formal UDPLITE socket support is now in place. The capability existed beforehand, but detecting it is easier today via `hasattr(socket, 'IPPROTO_UDPLITE')`, and constants now exist for every value you need: `socket.IPPROTO_UDPLITE`, `UDPLITE_SEND_CSCOV`, and `UDPLITE_RECV_CSCOV`. Gabe Appleton wrote the patch.

[bpo-37085](https://bugs.python.org/issue?@action=redirect&bpo=37085): The socket module gained the optional Linux SocketCAN Broadcast Manager constants, which serve as flags for tuning BCM behaviour. Karl Ding wrote the patch.

[bpo-37685](https://bugs.python.org/issue?@action=redirect&bpo=37685): Corrected the `__eq__`, `__lt__` and similar definitions across several classes. For an unsupported type on the other side, they now hand back [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented). That lets the opposite operand take part (so, for instance, an equality test against [`ANY`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.ANY) yields `True`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
