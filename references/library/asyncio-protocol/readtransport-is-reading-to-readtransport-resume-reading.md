# Read-only Transports

### Read-only Transports

 ReadTransport.is_reading()

Return `True` if the transport is receiving new data.

Added in version 3.7.

 ReadTransport.pause_reading()

Halt the transport's receiving side. Nothing will reach the protocol's `protocol.data_received()` method until `resume_reading()` runs.

Changed in version 3.7: This call is idempotent — invoking it on a transport that is already paused or closed is harmless.

 ReadTransport.resume_reading()

Restart the receiving side. Should any data be available to read, the protocol's `protocol.data_received()` method gets invoked once more.

Changed in version 3.7: This call is idempotent — invoking it on a transport that is already reading is harmless.

[Subject index](INDEX.md) · [Previous](basetransport-get-protocol.md) · [Continue](writetransport-abort-to-writetransport-write-eof.md)
