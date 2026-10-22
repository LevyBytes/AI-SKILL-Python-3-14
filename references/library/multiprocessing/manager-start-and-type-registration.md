# multiprocessing.managers.BaseManager: `start()`, `get_server()`, `connect()`, `shutdown()`, `register()`

*authkey* is the authentication key that serves to vet the legitimacy of incoming connections reaching the server process. When *authkey* is `None`, `current_process().authkey` is the one used. Otherwise *authkey* applies, and it has to be a byte string.

*serializer* has to be `'pickle'` (using [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle) serialization) or `'xmlrpclib'` (using [`xmlrpc.client`](https://docs.python.org/3.14/library/xmlrpc.client.html#module-xmlrpc.client) serialization).

*ctx* is either a context object or `None` (which uses the current context). With `None`, this call can fix the global start method. See Global start method for more details.

*shutdown_timeout* is a timeout, in seconds, that the `shutdown()` method spends waiting for the process the manager uses to finish. Should the shutdown exceed that, the process is terminated. Should terminating the process also exceed it, the process is killed.

Changed in version 3.11: Added the *shutdown_timeout* parameter.

 start([*initializer*[, *initargs*]])

Launch a subprocess to start the manager. When *initializer* is not `None`, the subprocess calls `initializer(*initargs)` as it starts.

 get_server()

Gives back a `Server` object that stands for the actual server under the Manager's control. The `Server` object supports the `serve_forever()` method:

```python
>>> from multiprocessing.managers import BaseManager
>>> manager = BaseManager(address=('', 50000), authkey=b'abc')
>>> server = manager.get_server()
>>> server.serve_forever()

```

On top of that, `Server` carries an `address` attribute.

 connect()

Hook a local manager object up to a remote manager process:

```python
>>> from multiprocessing.managers import BaseManager
>>> m = BaseManager(address=('127.0.0.1', 50000), authkey=b'abc')
>>> m.connect()

```

 shutdown()

Halt the process the manager uses. This is available only when `start()` was used to launch the server process.

You can call this more than once.

 register(*typeid*[, *callable*[, *proxytype*[, *exposed*[, *method_to_typeid*[, *create_method*]]]]])

A classmethod usable for registering a type or callable with the manager class.

*typeid* is a “type identifier” that serves to identify one particular type of shared object. It has to be a string.

*callable* is a callable used to build objects for this type identifier. When a manager instance is going to connect to the server through the `connect()` method, or when the *create_method* argument is `False`, this can be left as `None`.

*proxytype* is a subclass of `BaseProxy` used to build proxies for shared objects bearing this *typeid*. When `None`, a proxy class gets built automatically.

*exposed* serves to name a sequence of method names that proxies for this typeid should be permitted to reach using `BaseProxy._callmethod()`. (When *exposed* is `None`, `proxytype._exposed_` is used in its place should it exist.) When no exposed list is given, every “public method” of the shared object becomes reachable. (A “public method” here means any attribute that has a [`__call__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__call__) method and whose name does not start with `'_'`.)

*method_to_typeid* is a mapping that serves to name the return type for those exposed methods that ought to return a proxy. It maps method names onto typeid strings. (When *method_to_typeid* is `None`, `proxytype._method_to_typeid_` is used in its place should it exist.) When a method's name is missing from this mapping's keys, or when the mapping is `None`, the object the method returns gets copied by value.

*create_method* decides whether a method, named *typeid*, should be built that can instruct the server process to make a new shared object and hand back a proxy to it. Its default is `True`.

`BaseManager` instances additionally carry one read-only property:

 address

The address the manager uses.

Changed in version 3.3: The context management protocol is now supported by Manager objects – see [Context Manager Types](https://docs.python.org/3.14/library/stdtypes.html#typecontextmanager). [`__enter__()`](https://docs.python.org/3.14/library/stdtypes.html#contextmanager.__enter__) launches the server process (when it is not already running) and then returns the manager object. [`__exit__()`](https://docs.python.org/3.14/library/stdtypes.html#contextmanager.__exit__) calls `shutdown()`.

Earlier releases had [`__enter__()`](https://docs.python.org/3.14/library/stdtypes.html#contextmanager.__enter__) leave the manager's server process unstarted whenever it was not yet running.

[Subject index](INDEX.md) · [Continue](sync-manager-shared-object-factories.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md) · [Owning module, declaration or section: multiprocessing.managers.BaseManager](multiprocessing-managers-basemanager-class.md) · [Owning module, declaration or section: Managers](multiprocessing-manager.md) · [Preceding source contract and version conditions](multiprocessing-managers-basemanager-class.md)
