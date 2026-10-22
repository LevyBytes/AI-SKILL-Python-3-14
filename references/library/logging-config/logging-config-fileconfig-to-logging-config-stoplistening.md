# logging.config: `logging.config.fileConfig()`, `logging.config.listen()`, `logging.config.stopListening()`

logging.config.fileConfig(*fname*, *defaults=None*, *disable_existing_loggers=True*, *encoding=None*)

Loads the logging configuration out of a file in [`configparser`](https://docs.python.org/3.14/library/configparser.html#module-configparser) format. The file should follow the layout given in Configuration file format. An application may invoke this function more than once, which lets an end user pick among several ready-made configurations (provided the developer supplies a way to display the options and load the selected one).

It raises [`FileNotFoundError`](https://docs.python.org/3.14/library/exceptions.html#FileNotFoundError) when the file is missing and [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) when the file is invalid or empty.

Parameters:

- **fname** – A filename, a file-like object, or an instance descended from [`RawConfigParser`](https://docs.python.org/3.14/library/configparser.html#configparser.RawConfigParser). When a `RawConfigParser`-derived instance is supplied, it is taken as is. Otherwise a [`ConfigParser`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser) is created, and it reads the configuration from whatever was given in `fname`. Should that object have a [`readline()`](https://docs.python.org/3.14/library/readline.html#module-readline) method, it is treated as a file-like object and read via [`read_file()`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser.read_file); if not, it is treated as a filename and handed to [`read()`](https://docs.python.org/3.14/library/configparser.html#configparser.ConfigParser.read).

- **defaults** – Use this argument to specify defaults that should be handed to the `ConfigParser`.

- **disable_existing_loggers** – When given as `False`, any loggers that already exist at the moment of this call stay enabled. The default of `True` preserves the older behaviour in a backward-compatible manner. That behaviour disables every existing non-root logger unless it or one of its ancestors is named explicitly in the logging configuration.

- **encoding** – The encoding to use when opening the file in the case where *fname* is a filename.

Changed in version 3.4: A value of `fname` may now be an instance of a subclass of [`RawConfigParser`](https://docs.python.org/3.14/library/configparser.html#configparser.RawConfigParser). This makes the following possible:

>
- Employing a configuration file in which the logging configuration forms only one piece of the broader application configuration.

- Employing a configuration that was read from a file and subsequently adjusted by the consuming application (for instance based on command-line parameters or other facets of the runtime environment) prior to being handed off to `fileConfig`.

Changed in version 3.10: Added the *encoding* parameter.

Changed in version 3.12: An exception is raised when the supplied file is missing or is invalid or empty.

 logging.config.listen(*port=DEFAULT_LOGGING_CONFIG_PORT*, *verify=None*)

Brings up a socket server on the given port and waits for new configurations. When no port is given, the module's default `DEFAULT_LOGGING_CONFIG_PORT` applies. Logging configurations are to be transmitted as a file fit for processing through `dictConfig()` or `fileConfig()`. The function returns a [`Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) instance on which you may call [`start()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.start) to launch the server, and which you may [`join()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.join) at a fitting time. Calling `stopListening()` shuts the server down.

When supplied, the `verify` argument should be a callable that checks whether bytes arriving over the socket are valid and ought to be processed. One way to achieve this is by encrypting and/or signing what travels across the socket, so that the `verify` callable can carry out signature checking and/or decryption. The `verify` callable receives a single argument — the bytes arriving over the socket — and should hand back the bytes to be processed, or `None` to signal that the bytes ought to be thrown away. Those returned bytes might match the bytes that came in (for example, when only verification takes place), or they might be entirely different (perhaps when decryption has occurred).

To dispatch a configuration to the socket, read the configuration file in and transmit it over the socket as a sequence of bytes, prefixed by a four-byte length string packed in binary form using `struct.pack('>L', n)`.

Note

Since parts of the configuration get routed through [`eval()`](https://docs.python.org/3.14/library/functions.html#eval), relying on this function can expose its users to a security risk. Even though the function only binds to a socket on `localhost`, so it won't take connections from remote machines, there are situations where untrusted code could execute under the account of the process invoking `listen()`. To be precise, if the process calling `listen()` runs on a multi-user machine where the users have no basis for trusting each other, then a malicious user could contrive to run essentially arbitrary code inside a victim user's process, just by connecting to the victim's `listen()` socket and dispatching a configuration that executes whatever code the attacker wishes to have run inside the victim's process. Doing this is especially trivial when the default port is in use, but it remains feasible even with a different port. To sidestep the risk of this occurring, use the `verify` argument to `listen()` so that unrecognised configurations are kept from being applied.

Changed in version 3.4: The `verify` argument was added.

Note

If you wish to dispatch configurations to the listener that leave existing loggers enabled, you'll have to use a JSON format for the configuration, which will route through `dictConfig()` for configuration. This approach lets you set `disable_existing_loggers` to `False` in the configuration you transmit.

 logging.config.stopListening()

Halts the listening server that a call to `listen()` brought into being. This is ordinarily invoked ahead of calling `join()` on the value that `listen()` returned.

[Subject index](INDEX.md) · [Previous](logging-config-dictconfig.md) · [Continue](security-considerations.md) · [Owning module, declaration or section: logging.config](logging-config-logging-configuration.md) · [Owning module, declaration or section: Configuration functions](logging-config-dictconfig.md)
