# xml.dom - Accessor Methods

### Accessor Methods

For IDL `attribute` declarations, the OMG IDL-to-Python mapping sets up accessor functions, following roughly the same approach the Java mapping takes. Mapping the IDL declarations

```python
readonly attribute string someValue;
         attribute string anotherValue;

```

produces three accessor functions: a “get” method covering `someValue` (`_get_someValue()`), plus both “get” and “set” methods covering `anotherValue` (`_get_anotherValue()` and `_set_anotherValue()`). Notably, the mapping makes no demand that the IDL attributes be reachable like ordinary Python attributes: `object.someValue` is *not* guaranteed to function and could raise an [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

By contrast, the Python DOM API *does* insist that ordinary attribute access function. As a result, the usual stand-ins that Python IDL compilers churn out are unlikely to work, and a client reaching DOM objects through CORBA may have to rely on wrapper objects. That adds a bit of extra thought for CORBA DOM clients, yet the implementers who have actually run DOM over CORBA from Python see no trouble in it. In some DOM implementations, attributes marked `readonly` may not actually block write access.

The Python DOM API places no requirement on accessor functions at all. Where they do appear, they ought to match the shape the Python IDL mapping prescribes, yet such methods are seen as superfluous given that the attributes can be reached straight from Python. A `readonly` attribute should never be given a “set” accessor.

Not every requirement of the W3C DOM API is captured by the IDL definitions — among them the idea that certain objects, like whatever `getElementsByTagName()` hands back, are “live”. The Python DOM API leaves it up to implementations whether to enforce requirements of that kind.

[Subject index](INDEX.md) · [Previous](type-mapping.md) · [Owning module, declaration or section: xml.dom](xml-dom-the-document-object-model-api.md)
