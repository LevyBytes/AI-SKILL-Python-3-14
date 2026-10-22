# xmlrpc.client — Convenience Functions

### Convenience Functions

 xmlrpc.client.dumps(*params*, *methodname=None*, *methodresponse=None*, *encoding=None*, *allow_none=False*)

Turn *params* into an XML-RPC request, or — when *methodresponse* is true — into a response. For *params* you may pass either a tuple of arguments or an instance of the `Fault` exception class. With *methodresponse* true, just one value may come back, so *params* has to have length 1. When *encoding* is given, it sets the encoding for the generated XML; otherwise UTF-8 applies. Standard XML-RPC has no place for Python's [`None`](https://docs.python.org/3.14/library/constants.html#None) value; to permit it through an extension, hand a true value to *allow_none*.

 xmlrpc.client.loads(*data*, *use_datetime=False*, *use_builtin_types=False*)

Turn an XML-RPC request or response into Python objects, namely a `(params, methodname)`. Here *params* is a tuple of arguments, and *methodname* is a string — or `None` when the packet names no method. Where the XML-RPC packet stands for a fault condition, this function throws a `Fault` exception. Switching on the *use_builtin_types* flag makes date/time data come through as [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) objects and binary data come through as [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects; the flag starts out false.

The deprecated *use_datetime* flag resembles *use_builtin_types* but covers date/time data alone.

Changed in version 3.3: The *use_builtin_types* flag was added.

[Subject index](INDEX.md) · [Previous](xmlrpc-client-multicall-class.md) · [Continue](example-of-client-usage.md) · [Owning module, declaration or section: xmlrpc.client](xmlrpc-client-xml-rpc-client-access.md)
