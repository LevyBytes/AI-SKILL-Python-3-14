# mimetypes: `mimetypes.types_map`, `mimetypes.common_types`

mimetypes.types_map

A dictionary that maps filename extensions onto MIME types.

 mimetypes.common_types

A dictionary that maps filename extensions onto non-standard yet frequently encountered MIME types.

A sample of the module in use:

```python
>>> import mimetypes
>>> mimetypes.init()
>>> mimetypes.knownfiles
['/etc/mime.types', '/etc/httpd/mime.types', ... ]
>>> mimetypes.suffix_map['.tgz']
'.tar.gz'
>>> mimetypes.encodings_map['.gz']
'gzip'
>>> mimetypes.types_map['.tgz']
'application/x-tar-gz'

```

[Subject index](INDEX.md) · [Previous](mimetypes-guess-type-to-mimetypes-encodings-map.md) · [Continue](mimetypes-mimetypes-class.md) · [Owning module, declaration or section: mimetypes](mimetypes-guess-type-to-mimetypes-encodings-map.md)
