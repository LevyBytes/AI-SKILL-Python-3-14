# xmlrpc.client — `xmlrpc.client` — XML-RPC client access

### `xmlrpc.client` — XML-RPC client access

**Source code:** [Lib/xmlrpc/client.py](https://github.com/python/cpython/tree/3.14/Lib/xmlrpc/client.py)

---

As a Remote Procedure Call mechanism, XML-RPC ships XML over an HTTP(S) link. A caller invokes parameterized, named methods on a far endpoint (identified by a URI) and receives structured results back. The code here lets you author the client side of such exchanges; it quietly performs every conversion needed between compatible Python values and their on-the-wire XML form.

Warning

Maliciously crafted input is not something the `xmlrpc.client` module is hardened against. To process data that is untrusted or unauthenticated, consult [XML security](https://docs.python.org/3.14/library/xml.html#xml-security).

Changed in version 3.5: When given HTTPS URIs, `xmlrpc.client` by default now carries out every certificate and hostname verification that is required.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module is either nonfunctional or absent. Consult [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further detail.

```
 *class *xmlrpc.client.ServerProxy(*uri*, *transport=None*, *encoding=None*, *verbose=False*, *allow_none=False*, *use_datetime=False*, *use_builtin_types=False*, ***, *headers=()*, *context=None*)
```

Acting as a handle onto a remote XML-RPC server, each `ServerProxy` instance drives the back-and-forth with it. You must supply a URI (Uniform Resource Indicator) first; usually this is just the server's URL. A transport factory instance comes second and is optional; absent one, an internal `SafeTransport` is used for https: URLs and an internal HTTP `Transport` is used in every other case. Third, also optional, is an encoding, which defaults to UTF-8. Fourth, again optional, is a debugging flag.

How the resulting proxy behaves is controlled by the parameters below. Setting *allow_none* to true makes the Python constant `None` get rendered into XML; otherwise the default is for `None` to throw a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). Although this is a popular add-on to the XML-RPC spec, not every client or server honors it; a write-up lives at [http://ontosys.com/xml-rpc/extensions.php](https://web.archive.org/web/20130120074804/http://ontosys.com/xml-rpc/extensions.php). Turning on the *use_builtin_types* flag makes date/time data surface as [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) objects and binary data surface as [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) objects; the flag starts out false. You may hand `datetime.datetime`, `bytes` and [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) objects to calls. The *headers* parameter optionally lists HTTP headers to attach to every request, given as a sequence of 2-tuples holding each header's name and value. (e.g. `[('Header-Name', 'value')]`). When the URL is HTTPS, *context* may be an [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext) that tunes the SSL settings of the HTTPS connection beneath. The deprecated *use_datetime* flag works much like *use_builtin_types* except that it covers only date/time data.

Changed in version 3.3: The *use_builtin_types* flag was added.

Changed in version 3.8: The *headers* parameter was added.

Both transports — HTTP and HTTPS alike — accept the URL-syntax extension for HTTP Basic Authentication: `http://user:pass@host:port/path`. During connection, when an XML-RPC method is called, the `user:pass` segment is base64-encoded into an HTTP ‘Authorization’ header and dispatched to the far server. Reach for this only when the far server demands a Basic Authentication username and password.

What you get back is a proxy whose methods stand in for the matching RPC calls on the far server. Should that server expose the introspection API, you can also ask the proxy which methods exist (service discovery) and retrieve other metadata tied to the server.

The conformable types (i.e. those marshallable through XML) are listed next; unless a note says otherwise, each round-trips back as the very same Python type:

| XML-RPC type | Python type |
| --- | --- |
| `boolean` | `bool` |
| `int`, `i1`, `i2`, `i4`, `i8` or `biginteger` | `int` spanning -2147483648 through 2147483647. Such values carry the `<int>` tag. |
| `double` or `float` | `float`. These values carry the `<double>` tag. |
| `string` | `str` |
| `array` | `list` or `tuple` whose members are conformable. On the way back, arrays arrive as `lists`. |
| `struct` | `dict`. Every key has to be a string, while values can be of any conformable type. You may supply instances of your own classes; only the `__dict__` attribute travels across. |
| `dateTime.iso8601` | `DateTime` or `datetime.datetime`. Which one you get back hinges on the *use_builtin_types* and *use_datetime* flags. |
| `base64` | `Binary`, `bytes` or `bytearray`. Which one you get back hinges on the *use_builtin_types* flag. |
| `nil` | The `None` constant. This may only be sent when *allow_none* is true. |
| `bigdecimal` | `decimal.Decimal`. Available solely as a return value. |

Those entries are every data type XML-RPC handles. A method call can additionally throw a dedicated `Fault` instance, which reports XML-RPC server errors, or a `ProtocolError`, which reports a problem down in the HTTP/HTTPS transport layer. A shared base class named `Error` is the parent of both `Fault` and `ProtocolError`. Be aware that, at present, the xmlrpc client module does not marshal instances belonging to subclasses of the built-in types.

While strings are being sent, XML-special characters like `<`, `>`, and `&` are escaped for you automatically. Even so, it falls to the caller to keep the string clear of characters XML forbids — for example the control characters whose ASCII codes fall between 0 and 31 (tab, newline and carriage return excepted, naturally); skip this and the resulting XML-RPC request will not be well-formed XML. Should you ever need to send raw bytes through XML-RPC, turn to the [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) classes, or to the `Binary` wrapper class covered further down.

The name `Server` lives on as an alias of `ServerProxy` purely for backward compatibility; fresh code ought to reach for `ServerProxy`.

Changed in version 3.5: Added the *context* argument.

Changed in version 3.6: Gained support for prefixed type tags (e.g. `ex:nil`), plus unmarshalling of the extra numeric types that the Apache XML-RPC implementation uses: `i1`, `i2`, `i8`, `biginteger`, `float` and `bigdecimal`. A write-up is at [https://ws.apache.org/xmlrpc/types.html](https://ws.apache.org/xmlrpc/types.html).

See also

[XML-RPC HOWTO](https://tldp.org/HOWTO/XML-RPC-HOWTO/index.html)

A solid walkthrough of how XML-RPC operates plus client tooling across several languages. It holds just about all an XML-RPC client author would want.

[XML-RPC Introspection](https://xmlrpc-c.sourceforge.io/introspection.html)

Covers the introspection extension to the XML-RPC protocol.

[XML-RPC Specification](http://xmlrpc.scripting.com/spec.html)

The authoritative spec.

[Subject index](INDEX.md) · [Previous](xml-rpc-client-access.md) · [Continue](xmlrpc-method-discovery-and-help.md)
