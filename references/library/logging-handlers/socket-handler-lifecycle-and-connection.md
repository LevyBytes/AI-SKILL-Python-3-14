# logging.handlers.SocketHandler: `close()`, `emit()`, `handleError()`, `makeSocket()`, `makePickle()`, `send()`, `createSocket()`

close()

Closes the socket.

 emit()

Pickles the record's attribute dictionary and writes it onto the socket in binary form. Should the socket hit an error, the packet is silently dropped. When the connection was lost earlier, it re-establishes the connection. To unpickle the record back into a [`LogRecord`](https://docs.python.org/3.14/library/logging.html#logging.LogRecord) at the receiving end, use the [`makeLogRecord()`](https://docs.python.org/3.14/library/logging.html#logging.makeLogRecord) function.

 handleError()

Handles an error that has cropped up during `emit()`. The likeliest culprit is a lost connection. Closes the socket so that a retry can occur on the next event.

 makeSocket()

This is a factory method letting subclasses spell out the exact type of socket they want. The default implementation builds a TCP socket ([`socket.SOCK_STREAM`](https://docs.python.org/3.14/library/socket.html#socket.SOCK_STREAM)).

 makePickle(*record*)

Pickles the record's attribute dictionary in binary form with a length prefix, and returns it ready to travel across the socket. The specifics of this operation amount to:

```python
data = pickle.dumps(record_attr_dict, 1)
datalen = struct.pack('>L', len(data))
return datalen + data

```

Bear in mind that pickles aren't fully secure. If security worries you, you might want to override this method to put a more secure mechanism in place. For instance, you can sign pickles with HMAC and then verify them at the receiving end, or alternatively you can switch off unpickling of global objects at the receiving end.

 send(*packet*)

Dispatch a pickled byte-string *packet* over the socket. The layout of the dispatched byte-string follows what the documentation for `makePickle()` lays out.

This function makes room for partial sends, which can occur when the network is busy.

 createSocket()

Attempts to create a socket; should it fail, it falls back on an exponential back-off algorithm. On the first failure, the handler drops the message it was trying to send. When the same instance later handles further messages, it won't attempt to connect until some time has gone by. The default parameters make the initial delay one second, and if the connection still can't be made after that delay, the handler doubles the delay each time up to a ceiling of 30 seconds.

The handler attributes below govern this behaviour:

- `retryStart` (initial delay, defaulting to 1.0 seconds).

- `retryFactor` (multiplier, defaulting to 2.0).

- `retryMax` (maximum delay, defaulting to 30.0 seconds).

What this means is that should the remote listener come up *after* the handler has already been used, you could lose messages (because the handler won't so much as attempt a connection until the delay has run out, instead just silently dropping messages throughout the delay period).

[Subject index](INDEX.md) · [Previous](logging-handlers-sockethandler-class.md) · [Continue](logging-handlers-datagramhandler-class.md) · [Owning module, declaration or section: logging.handlers](handler-types-overview.md) · [Owning module, declaration or section: logging.handlers.SocketHandler](logging-handlers-sockethandler-class.md) · [Owning module, declaration or section: SocketHandler](logging-handlers-sockethandler-class.md)
