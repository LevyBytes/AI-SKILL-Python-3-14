# multiprocessing - Authentication keys

### Authentication keys

When you call `Connection.recv`, the incoming data is unpickled automatically. Sadly, unpickling data from an untrusted source poses a security risk. For that reason `Listener` and `Client()` turn to the [`hmac`](https://docs.python.org/3.14/library/hmac.html#module-hmac) module to deliver digest authentication.

An authentication key is a byte string you can picture as a password: with a connection set up, each end will require the other to prove it knows the authentication key. (Proving that both ends use the same key does **not** entail sending the key across the connection.)

When authentication is asked for but no authentication key is named, the value that `current_process().authkey` returns gets used (see `Process`). Any `Process` object the current process creates inherits this value automatically. This means that (by default) every process in a multi-process program shares one authentication key usable when setting up connections among themselves.

Fitting authentication keys can likewise be generated with [`os.urandom()`](https://docs.python.org/3.14/library/os.html#os.urandom).

This authentication safeguards `Listener` and `Client()` connections, the ones reachable by address. It does not extend to the anonymous pipes that `Pipe()` makes or that `Queue` uses internally. `multiprocessing` treats every local process running under the same user as trusted; on most operating systems such processes can reach one another's pipe file descriptors regardless. Applications needing isolation between same-user processes have to set it up at the operating-system level – say, by running workers under a separate user account or inside a sandbox.

[Subject index](INDEX.md) · [Previous](address-formats.md) · [Continue](multiprocessing-get-logger-to-multiprocessing-log-to-stderr.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
