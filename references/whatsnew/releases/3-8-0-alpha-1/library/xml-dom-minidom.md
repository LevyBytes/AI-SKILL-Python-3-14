# Python 3.8.0 alpha 1 / library / xml dom minidom

[bpo-33274](https://bugs.python.org/issue?@action=redirect&bpo=33274): The W3C DOM Level 1 specification defines Element.removeAttributeNode()'s return value as "The Attr node that was removed." xml.dom.minidom now satisfies that requirement.

[bpo-35052](https://bugs.python.org/issue?@action=redirect&bpo=35052): Corrected xml.dom.minidom cloneNode() on a document containing an entity: hand the proper arguments to that entity's user data handler.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
