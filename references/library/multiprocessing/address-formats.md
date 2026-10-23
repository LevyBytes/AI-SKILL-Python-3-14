# multiprocessing - Address Formats

#### Address Formats

- An `'AF_INET'` address takes the shape of a tuple `(hostname, port)`, where *hostname* is a string and *port* is an integer.

- An `'AF_UNIX'` address takes the shape of a string naming a file on the filesystem.

- An `'AF_PIPE'` address takes the shape of a string `r'\\.\pipe\*PipeName*'`. To make `Client()` connect to a named pipe on a remote machine named *ServerName*, use an address shaped like `r'\\*ServerName*\pipe\*PipeName*'` instead.

Note that, by default, any string opening with two backslashes is taken to be an `'AF_PIPE'` address rather than an `'AF_UNIX'` address.

[Subject index](INDEX.md) · [Previous](pipe-connection-wait-example.md) · [Continue](authentication-keys.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
