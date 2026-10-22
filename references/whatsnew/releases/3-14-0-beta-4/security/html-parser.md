# Python 3.14.0 beta 4 / security / html parser

[gh-135661](https://github.com/python/cpython/issues/135661): Start and end tag parsing in [`html.parser.HTMLParser`](https://docs.python.org/3.14/library/html.parser.html#html.parser.HTMLParser) was corrected to follow the HTML5 standard.

  - Between `</` and the tag name, whitespace is no longer permitted. For instance, `</ script>` will not close the script section.

  - Neither vertical tabulation (`\v`) nor non-ASCII whitespaces count as whitespace any longer. The recognized whitespaces are limited to `\t\n\r\f` and the space character.

  - A null character (U+0000) will no longer terminate the tag name.

  - Within end tags, slashes and attributes following the tag name are now skipped, rather than stopping at the first `>` found inside a quoted attribute value. Consider `</script/foo=">"/>`.

  - Across both start and end tags, several slashes and whitespaces sitting between the final attribute and the closing `>` are now skipped. Consider `<a foo=bar/ //>`.

  - Several `=` characters placed between an attribute name and its value are no longer merged together. Consider `<a foo==bar>`, which yields the attribute “foo” holding the value “=bar”.

  - [Reverted in [gh-136927](https://github.com/python/cpython/issues/136927)] Any whitespaces sitting between the `=` separator and an attribute name or value are no longer dropped. Consider `<a foo =bar>`, which yields two attributes “foo” and “=bar”, each with value None; whereas `<a foo= bar>` yields two attributes: “foo” carrying value “” and “bar” carrying value None.

[gh-102555](https://github.com/python/cpython/issues/102555): Comment parsing within [`html.parser.HTMLParser`](https://docs.python.org/3.14/library/html.parser.html#html.parser.HTMLParser) was corrected to match the HTML5 standard. A comment is now closed by `--!>`. A comment is no longer closed by `-- >`. Abnormally terminated empty comments such as `<-->` and `<--->` are now supported.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
