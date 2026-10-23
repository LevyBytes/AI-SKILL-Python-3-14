# What’s New in Python 2.3 / New, Improved, and Deprecated Modules - shelve, xml.dom.minidom

Should you run into any incompatibilities, the previous behavior is recoverable: set the `wantobjects` variable in the `Tkinter` module to false before the first `tkapp` object is constructed.

```python
import Tkinter
Tkinter.wantobjects = 0

```

Please file a bug for any breakage that this change introduces.

- A fresh `DictMixin` class now lives in the `UserDict` module, supplying every dictionary method to classes that already expose a small mapping interface. This makes it far easier to author classes meant to stand in for dictionaries, like those found in the [`shelve`](https://docs.python.org/3.14/library/shelve.html#module-shelve) module.

By including the mix-in among the superclasses, the class receives the complete dictionary interface as soon as it implements [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__), [`__setitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__setitem__), [`__delitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__delitem__), and `keys()`. Consider this example:

```python
>>> import UserDict
>>> class SeqDict(UserDict.DictMixin):
...     """Dictionary lookalike implemented with lists."""
...     def __init__(self):
...         self.keylist = []
...         self.valuelist = []
...     def __getitem__(self, key):
...         try:
...             i = self.keylist.index(key)
...         except ValueError:
...             raise KeyError
...         return self.valuelist[i]
...     def __setitem__(self, key, value):
...         try:
...             i = self.keylist.index(key)
...             self.valuelist[i] = value
...         except ValueError:
...             self.keylist.append(key)
...             self.valuelist.append(value)
...     def __delitem__(self, key):
...         try:
...             i = self.keylist.index(key)
...         except ValueError:
...             raise KeyError
...         self.keylist.pop(i)
...         self.valuelist.pop(i)
...     def keys(self):
...         return list(self.keylist)
...
>>> s = SeqDict()
>>> dir(s)      # See that other dictionary methods are implemented
['__cmp__', '__contains__', '__delitem__', '__doc__', '__getitem__',
 '__init__', '__iter__', '__len__', '__module__', '__repr__',
 '__setitem__', 'clear', 'get', 'has_key', 'items', 'iteritems',
 'iterkeys', 'itervalues', 'keylist', 'keys', 'pop', 'popitem',
 'setdefault', 'update', 'valuelist', 'values']

```

(Contributed by Raymond Hettinger.)

- By passing an optional encoding argument to the [`toxml()`](https://docs.python.org/3.14/library/xml.dom.minidom.html#xml.dom.minidom.Node.toxml) and [`toprettyxml()`](https://docs.python.org/3.14/library/xml.dom.minidom.html#xml.dom.minidom.Node.toprettyxml) methods of DOM nodes, the DOM implementation in [`xml.dom.minidom`](https://docs.python.org/3.14/library/xml.dom.minidom.html#module-xml.dom.minidom) is now able to emit XML output in a chosen encoding.

- An XML-RPC extension for dealing with nil data values, such as Python's `None`, is now handled by the `xmlrpclib` module. Unmarshalling an XML-RPC response always accepts nil values. If you want to produce requests that include `None`, pass a true value for the *allow_none* parameter while constructing a `Marshaller` instance.

- Writing self-documenting XML-RPC servers is made possible by the new `DocXMLRPCServer` module. Launch it in demo mode (as a program) to watch it work. Directing a web browser at the RPC server yields pydoc-style documentation; directing xmlrpclib at the server lets you call the real methods. (Contributed by Brian Quinlan.)

- Internationalized domain names (RFCs 3454, 3490, 3491, and 3492) are now supported. With the "idna" encoding you can translate between a Unicode domain name and its ASCII-compatible encoding (ACE).

```python
>{}>{}> u"www.Alliancefrançaise.nu".encode("idna")
'www.xn--alliancefranaise-npb.nu'

```

[Subject index](INDEX.md) · [Next source section](unicode-network-hostnames-and-stringprep.md) · [Release/subject declaration](standard-set-type.md) · [Release/subject declaration](standard-library-module-changes.md) · [Preceding release/subject continuation](text-threading-and-timing-updates.md)
