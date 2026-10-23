# html.parser - Examples - Contract: The names of attributes get lowercased, quotes wrapping their values are stripped, and for attributes left empty (`checked`, say) the *value* comes back as `None`:

The names of attributes get lowercased, quotes wrapping their values are stripped, and for attributes left empty (`checked`, say) the *value* comes back as `None`:

```pycon
>>> parser.feed("<input TYPE='checkbox' checked required='' disabled=disabled>")
Start tag: input
     attr: ('type', 'checkbox')
     attr: ('checked', None)
     attr: ('required', '')
     attr: ('disabled', 'disabled')

```

Reading comments:

```pycon
>>> parser.feed('<!--a comment-->'
...             '<!--[if IE 9]>IE-specific content<![endif]-->')
Comment  : a comment
Comment  : [if IE 9]>IE-specific content<![endif]
```

Reading both named and numeric character references and turning each into the right char (note that all 3 of these references stand for `'>'`):

```pycon
>>> parser = MyHTMLParser()
>>> parser.feed('&gt;&#62;&#x3E;')
Data     : >>>

>>> parser = MyHTMLParser(convert_charrefs=False)
>>> parser.feed('&gt;&#62;&#x3E;')
Named ent: >
Num ent  : >
Num ent  : >
```

Passing partial chunks into `feed()` is fine, though `handle_data()` may run several times over when *convert_charrefs* is false:

```pycon
>>> for chunk in ['<sp', 'an>buff', 'ered', ' text</s', 'pan>']:
...     parser.feed(chunk)
...
Start tag: span
Data     : buff
Data     : ered
Data     :  text
End tag  : span

```

Reading malformed HTML (unquoted attributes, for instance) works as well:

```pycon
>>> parser.feed('<p><a class=link href=#main>tag soup</p ></a>')
Start tag: p
Start tag: a
     attr: ('class', 'link')
     attr: ('href', '#main')
Data     : tag soup
End tag  : p
End tag  : a

```

[Subject index](INDEX.md) · [Previous](examples-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: html.parser](html-parser-htmlparser-class.md) · [Owning module, declaration or section: Examples](examples-section-introduction-and-initial-examples.md)
