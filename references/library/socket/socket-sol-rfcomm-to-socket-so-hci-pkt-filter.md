# socket: Bluetooth protocol levels and HCI filtering

socket.SOL_RFCOMM

 socket.SOL_L2CAP

 socket.SOL_HCI

 socket.SOL_SCO

 socket.SOL_BLUETOOTH

Passed as the level argument to a Bluetooth socket object's `setsockopt()` and `getsockopt()` methods.

`SOL_BLUETOOTH` exists only on Linux. The other constants exist wherever the matching protocol is supported.

 SO_L2CAP_*

 socket.L2CAP_LM

 L2CAP_LM_*

 SO_RFCOMM_*

 RFCOMM_LM_*

 SO_SCO_*

 SO_BTH_*

 BT_*

Passed as the option name and value argument to a Bluetooth socket object's `setsockopt()` and `getsockopt()` methods.

`BT_*` and `L2CAP_LM` exist only on Linux. `SO_BTH_*` exist only on Windows. The remaining constants may exist on Linux and on various BSD platforms.

Added in version 3.14.

 socket.HCI_FILTER

 socket.HCI_TIME_STAMP

 socket.HCI_DATA_DIR

 socket.SO_HCI_EVT_FILTER

 socket.SO_HCI_PKT_FILTER

Option names for use with `BTPROTO_HCI`. Whether they are available, and how the option values are formatted, varies by platform.

[Subject index](INDEX.md) · [Previous](socket-sio-rcvall-to-socket-bdaddr-le-random.md) · [Owning module, declaration or section: socket](socket-low-level-networking-interface.md) · [Owning module, declaration or section: Constants](socket-af-unix-to-socket-sock-nonblock.md) · [Required continuation of the source contract](socket-hci-dev-none-to-socket-so-reuseport-lb.md)
