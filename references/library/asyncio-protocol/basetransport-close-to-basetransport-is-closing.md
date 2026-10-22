# asyncio.protocol: `BaseTransport.close()`, `BaseTransport.is_closing()`

### Base Transport

 BaseTransport.close()

Close the transport.

When the transport holds a buffer of outgoing data, that buffered data gets flushed asynchronously. Nothing further will be received. Once every byte of buffered data has been flushed, the protocol's `protocol.connection_lost()` method is invoked with [`None`](https://docs.python.org/3.14/library/constants.html#None) passed as the argument. Don't keep using the transport after it has been closed.

 BaseTransport.is_closing()

Return `True` if the transport is closing or is closed.

[Subject index](INDEX.md) · [Previous](asyncio-subprocesstransport-class.md) · [Continue](basetransport-get-extra-info-to-basetransport-set-protocol.md)
