# xml.dom - NamedNodeMap Objects

### NamedNodeMap Objects

`NamedNodeMap` does *not* derive from `Node`.

 NamedNodeMap.length

How long the attribute list is.

 NamedNodeMap.item(*index*)

Hand back the attribute at a given index. Although the sequence in which you receive the attributes is unspecified, it stays the same throughout a DOM's lifetime. Each entry is an attribute node. Read its value off the `value` attribute.

There are experimental methods too that lend this class more map-like behavior. You may rely on those, or instead rely on the standardized `getAttribute*()` family of methods carried by the `Element` objects.

[Subject index](INDEX.md) · [Previous](attr-name-to-attr-value.md) · [Continue](comment-data.md) · [Owning module, declaration or section: xml.dom](xml-dom-the-document-object-model-api.md)
