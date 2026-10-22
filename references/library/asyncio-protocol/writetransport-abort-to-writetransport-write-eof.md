# Write-only Transports

### Write-only Transports

 WriteTransport.abort()

Shut the transport down at once, rather than letting pending operations finish. Any buffered data is discarded. Nothing more will be received. In time the protocol's `protocol.connection_lost()` method gets invoked with [`None`](https://docs.python.org/3.14/library/constants.html#None) passed as the argument.

 WriteTransport.can_write_eof()

Return [`True`](https://docs.python.org/3.14/library/constants.html#True) if the transport supports `write_eof()`, [`False`](https://docs.python.org/3.14/library/constants.html#False) if not.

 WriteTransport.get_write_buffer_size()

Return the transport's output buffer size as it currently stands.

 WriteTransport.get_write_buffer_limits()

Retrieve the *high* and *low* watermarks governing write flow control. The return value is a tuple `(low, high)`, where both *low* and *high* are byte counts expressed as positive numbers.

Use `set_write_buffer_limits()` to set the limits.

Added in version 3.4.2.

 WriteTransport.set_write_buffer_limits(*high=None*, *low=None*)

Set the *high* and *low* watermarks for write flow control.

Expressed as byte counts, this pair of values dictates the moments at which the protocol's `protocol.pause_writing()` and `protocol.resume_writing()` methods fire. When both are provided, the low watermark cannot exceed the high watermark. Neither *high* nor *low* may be negative.

Once the buffer size reaches or passes the *high* value, `pause_writing()` fires. After writing has been paused, `resume_writing()` fires as soon as the buffer size falls to or below the *low* value.

What the defaults are depends on the implementation. When you supply only the high watermark, the low watermark takes an implementation-specific default that does not exceed the high watermark. A *high* of zero drags *low* down to zero too, so `pause_writing()` fires every time the buffer stops being empty. A *low* of zero means `resume_writing()` fires solely once the buffer empties out. Picking zero for either bound tends to be sub-optimal, since it cuts down on chances to overlap I/O with computation.

Use `get_write_buffer_limits()` to get the limits.

 WriteTransport.write(*data*)

Write some *data* bytes to the transport.

Calling this method won't block; the data is buffered and queued for asynchronous transmission.

 WriteTransport.writelines(*list_of_data*)

Send a list, or any other iterable, of data bytes through the transport. The effect matches invoking `write()` on every item the iterable produces, though the implementation may be more efficient.

 WriteTransport.write_eof()

Flush all buffered data, then shut the write end of the transport. Receiving can still continue.

Where the transport (SSL, for instance) lacks half-closed connection support, this method may raise [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

[Subject index](INDEX.md) · [Previous](readtransport-is-reading-to-readtransport-resume-reading.md) · [Continue](datagramtransport-sendto-to-datagramtransport-abort.md)
