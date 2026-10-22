# xml.etree.ElementTree — Supported XPath syntax

### Supported XPath syntax

| Syntax | Meaning |
| --- | --- |
| `tag` | Picks out every child element carrying the named tag. As an illustration, `spam` grabs each child element called `spam`, while `spam/egg` grabs each grandchild called `egg` beneath any child called `spam`. The form `{namespace}*` grabs every tag within the named namespace, `{*}spam` grabs tags called `spam` in any namespace (or in none), and `{}*` grabs solely the tags lying outside any namespace. Changed in version 3.8: Support for star-wildcards was added. |
| `*` | Picks out every child element, comments and processing instructions included. As an illustration, `*/egg` grabs each grandchild called `egg`. |
| `.` | Picks out the node currently in focus. This proves handy chiefly at a path's start, signaling that the path is a relative one. |
| `//` | Picks out every subelement at any depth below the current element. As an illustration, `.//egg` grabs each `egg` element across the whole tree. |
| `..` | Picks out the parent element. Hands back `None` should the path try to climb above the ancestors of the start element (the one on which `find` ran). |
| `[@attrib]` | Picks out every element carrying the named attribute. |
| `[@attrib='value']` | Picks out every element where the named attribute holds the stated value. Quotes are not allowed in the value. |
| `[@attrib!='value']` | Picks out every element where the named attribute fails to hold the stated value. Quotes are not allowed in the value. Added in version 3.10. |
| `[tag]` | Picks out every element owning a child called `tag`. Support extends to immediate children only. |
| `[.='text']` | Picks out every element whose full text content, descendants and all, matches the stated `text`. Added in version 3.7. |
| `[.!='text']` | Picks out every element whose full text content, descendants and all, fails to match the stated `text`. Added in version 3.10. |
| `[tag='text']` | Picks out every element owning a child called `tag` whose full text content, descendants and all, matches the stated `text`. |
| `[tag!='text']` | Picks out every element owning a child called `tag` whose full text content, descendants and all, fails to match the stated `text`. Added in version 3.10. |
| `[position]` | Picks out every element sitting at the stated position. That position may be given as an integer (where 1 marks the first slot), as the expression `last()` (for the final slot), or as an offset measured back from the final slot (for instance `last()-1`). |

Predicates (the expressions inside square brackets) have to come after a tag name, an asterisk, or a preceding predicate. A `position` predicate has to come after a tag name.

[Subject index](INDEX.md) · [Previous](example-all-dublin-core-title-tags-in-the-document.md) · [Continue](xml-canonicalization-comments-and-debug-output.md) · [Owning module, declaration or section: xml.etree.ElementTree](xml-etree-elementtree-the-elementtree-xml-api.md)
