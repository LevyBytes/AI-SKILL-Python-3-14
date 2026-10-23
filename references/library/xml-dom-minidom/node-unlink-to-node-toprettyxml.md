# xml.dom.minidom - DOM Objects

### DOM Objects

You'll find the DOM API for Python defined within the [`xml.dom`](https://docs.python.org/3.14/library/xml.dom.html#module-xml.dom) module documentation. What this section sets out is where that API and `xml.dom.minidom` diverge.

 Node.unlink()

Sever the DOM's internal references so it can be garbage collected even on Python builds that lack cyclic GC. And where cyclic GC does exist, this still frees up sizable chunks of memory sooner, which makes calling it on DOM objects the moment they're done with a sound habit. You need invoke it only on the `Document` object, though calling it on child nodes works too, throwing away that node's children.

There's a way to sidestep calling this method by hand: the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. In the code below, *dom* is unlinked for you the instant the `with` block ends:

```python
with xml.dom.minidom.parse(datasource) as dom:
    ... # Work with dom.

```

 Node.writexml(*writer*, *indent=''*, *addindent=''*, *newl=''*, *encoding=None*, *standalone=None*)

Send XML out to the writer object. That writer takes text rather than bytes as its input, and it ought to expose a `write()` method lining up with the file object interface. The *indent* parameter gives the current node's indentation, while *addindent* gives the extra indentation layered on for that node's subnodes. The *newl* parameter names the string used to cap off newlines.

On a `Document` node, you can supply the further keyword argument *encoding* to set the encoding field of the XML header.

In the same vein, spelling out the *standalone* argument prompts the standalone document declarations to be placed into the XML document's prologue. Set the value to `True` and `standalone="yes"` goes in; otherwise it becomes `"no"`. Leave the argument unstated and no such declaration appears in the document at all.

Changed in version 3.8: From now on, `writexml()` keeps attributes in whatever order the user laid them out.

Changed in version 3.9: The *standalone* parameter was added.

 Node.toxml(*encoding=None*, *standalone=None*)

Hand back a string or byte string holding the XML that the DOM node stands for.

Supply an explicit *encoding* [1] argument and you get a byte string in that named encoding. Leave *encoding* off and the result is a Unicode string whose XML declaration names no encoding at all. Putting this string into any encoding besides UTF-8 is likely a mistake, given that UTF-8 is XML's default encoding.

The *standalone* argument acts just the way it does in `writexml()`.

Changed in version 3.8: From now on, `toxml()` keeps attributes in the order the user originally gave them.

Changed in version 3.9: The *standalone* parameter was added.

 Node.toprettyxml(*indent='\t'*, *newl='\n'*, *encoding=None*, *standalone=None*)

Hand back a pretty-printed rendering of the document. The *indent* names the indentation string and falls back to a tabulator, while *newl* names the string put out at each line's close and falls back to `\n`.

As for the *encoding* argument, it works like the matching argument over on `toxml()`.

The *standalone* argument, too, acts exactly the way it does in `writexml()`.

Changed in version 3.8: From now on, `toprettyxml()` keeps attributes in the very order the user supplied.

Changed in version 3.9: The *standalone* parameter was added.

[Subject index](INDEX.md) · [Previous](xml-dom-minidom-parse-to-xml-dom-minidom-parsestring.md) · [Continue](dom-example.md) · [Owning module, declaration or section: xml.dom.minidom](xml-dom-minidom-parse-to-xml-dom-minidom-parsestring.md)
