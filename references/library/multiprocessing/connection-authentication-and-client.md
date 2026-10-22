# multiprocessing: `multiprocessing.connection.deliver_challenge()`, `multiprocessing.connection.answer_challenge()`, `multiprocessing.connection.Client()`

### Listeners and Clients

Message passing between processes is normally handled through queues or through `Connection` objects that `Pipe()` hands back.

The `multiprocessing.connection` module, however, opens up some extra flexibility. At bottom it offers a high-level, message-oriented API for working with sockets or Windows named pipes. It additionally supports *digest authentication* by way of the [`hmac`](https://docs.python.org/3.14/library/hmac.html#module-hmac) module, plus polling several connections together.

 multiprocessing.connection.deliver_challenge(*connection*, *authkey*)

Send a randomly generated message to the connection's far end and wait for a response.

When that response matches the message's digest computed with *authkey* as the key, a welcome message goes out to the connection's far end. Otherwise `AuthenticationError` is raised.

 multiprocessing.connection.answer_challenge(*connection*, *authkey*)

Take in a message, work out its digest using *authkey* as the key, and then send that digest back.

When no welcome message comes in, `AuthenticationError` is raised.

 multiprocessing.connection.Client(*address*[, *family*[, *authkey*]])

Try to open a connection to the listener that is using address *address*, giving back a `Connection`.

The connection's type follows from the *family* argument, but this can usually be dropped since it is normally deducible from the layout of *address*. (See Address Formats)

When *authkey* is supplied and not `None`, it should be a byte string and serves as the secret key for an HMAC-based authentication challenge. No authentication happens when *authkey* is `None`. `AuthenticationError` is raised when authentication fails. See Authentication keys.

[Subject index](INDEX.md) · [Previous](process-pool-apply-async-map-imap-and-timeout-example.md) · [Continue](connection-listener-lifecycle.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
