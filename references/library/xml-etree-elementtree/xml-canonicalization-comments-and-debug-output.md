# xml.etree.ElementTree: `xml.etree.ElementTree.canonicalize()`, `xml.etree.ElementTree.Comment()`, `xml.etree.ElementTree.dump()`

### Reference

### Functions

 xml.etree.ElementTree.canonicalize(*xml_data=None*, ***, *out=None*, *from_file=None*, ***options*)

[C14N 2.0](https://www.w3.org/TR/xml-c14n2/) transformation function.

Canonicalization serves to normalise XML output so that byte-by-byte comparisons and digital signatures become feasible. By narrowing the latitude available to XML serializers, it yields a more tightly constrained XML representation. Its chief constraints concern where namespace declarations sit, how attributes are ordered, and ignorable whitespace.

Given as its input either a string of XML data (*xml_data*) or else a file path or file-like object (*from_file*), the function converts that into the canonical form and emits the result through the *out* file(-like) object when one is supplied, or otherwise hands it back as a text string. Because the output file is given text rather than bytes, it ought to be opened in text mode using `utf-8` encoding.

Typical uses:

```python
xml_data = "<root>...</root>"
print(canonicalize(xml_data))

with open("c14n_output.xml", mode='w', encoding='utf-8') as out_file:
    canonicalize(xml_data, out=out_file)

with open("c14n_output.xml", mode='w', encoding='utf-8') as out_file:
    canonicalize(from_file="inputfile.xml", out=out_file)

```

Here are the configuration *options*:

- *with_comments*: set to true to include comments (default: false)

- *strip_text*: set to true to strip whitespace before and after text content

(default: false)

- *rewrite_prefixes*: set to true to replace namespace prefixes by “n{number}”

(default: false)

- *qname_aware_tags*: a set of qname aware tag names in which prefixes

should be replaced in text content (default: empty)

- *qname_aware_attrs*: a set of qname aware attribute names in which prefixes

should be replaced in text content (default: empty)

- *exclude_attrs*: a set of attribute names that should not be serialised

- *exclude_tags*: a set of tag names that should not be serialised

Throughout the option list above, "a set" denotes any collection or iterable of strings, with no ordering implied.

Added in version 3.8.

 xml.etree.ElementTree.Comment(*text=None*)

Comment element factory. This factory function builds a special element that the standard serializer renders as an XML comment. The comment string may be supplied either as a bytestring or as a Unicode string. *text* is a string holding the comment string. Hands back an element instance standing for a comment.

Be aware that `XMLParser` passes over comments in the input rather than building comment objects from them. An `ElementTree` ends up with comment nodes only when they have been added into the tree by means of one of the `Element` methods.

 xml.etree.ElementTree.dump(*elem*)

Writes an element tree or element structure to sys.stdout. This function is meant strictly for debugging.

How the output looks depends on the implementation. In the present version, it comes out as a regular XML file.

*elem* is an element tree or an individual element.

Changed in version 3.8: The `dump()` function now keeps attributes in the order the user laid them out.

[Subject index](INDEX.md) · [Continue](xml-string-parsing-and-serialization.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md)
