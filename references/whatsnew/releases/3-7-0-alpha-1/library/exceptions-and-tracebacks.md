# Python 3.7.0 alpha 1 / library / exceptions and tracebacks

[bpo-27358](https://bugs.python.org/issue?@action=redirect&bpo=27358): Sped up the merging of var-keyword arguments and sharpened the error message produced when a non-mapping is supplied as one.

[bpo-30185](https://bugs.python.org/issue?@action=redirect&bpo=30185): KeyboardInterrupt tracebacks in the forkserver helper process are now avoided when Ctrl-C arrives.

[bpo-29960](https://bugs.python.org/issue?@action=redirect&bpo=29960): When _random.Random.setstate() throws an exception, the generator state is now kept intact. Bryan Olson wrote the patch.

[bpo-31234](https://bugs.python.org/issue?@action=redirect&bpo=31234): socket.create_connection() now clears a reference cycle by hand: on success it wipes the variable that holds the last exception.

[bpo-29692](https://bugs.python.org/issue?@action=redirect&bpo=29692): Arbitrary unchaining of RuntimeError exceptions within contextlib.contextmanager was corrected. Siddharth Velankar contributed the patch.

[bpo-29649](https://bugs.python.org/issue?@action=redirect&bpo=29649): Exception messages from struct.pack_into() for buffer-size and offset problems were improved. Andrew Nester contributed the patch.

[bpo-28699](https://bugs.python.org/issue?@action=redirect&bpo=28699): Inside multiprocessing.pool, a pool bug where an exception raised at the very start of an iterable could be swallowed or hang the program was corrected. Davin Potts and Xiang Zhang contributed the patch.

[bpo-27517](https://bugs.python.org/issue?@action=redirect&bpo=27517): The LZMA compressor and decompressor stopped raising exceptions when handed empty data on two successive calls. Benjamin Fogle authored the patch.

[bpo-29615](https://bugs.python.org/issue?@action=redirect&bpo=29615): SimpleXMLRPCDispatcher will no longer chain KeyError (or any other exception) onto exceptions thrown by the dispatched methods. Petr Motejlek contributed the patch.

[bpo-30245](https://bugs.python.org/issue?@action=redirect&bpo=30245): A potential overflow while building the struct.pack_into error message was corrected. Yuan Liu wrote the patch.

[bpo-30508](https://bugs.python.org/issue?@action=redirect&bpo=30508): Once the “cancel()” method on a Task/Future has run, exceptions are no longer logged.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
