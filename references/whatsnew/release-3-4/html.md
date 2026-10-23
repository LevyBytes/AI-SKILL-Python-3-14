# What's New In Python 3.4 / html - html

### html

A new function, [`unescape()`](https://docs.python.org/3.14/library/html.html#html.unescape), turns HTML5 character references into their matching Unicode characters. (Contributed by Ezio Melotti in [bpo-2927](https://bugs.python.org/issue?@action=redirect&bpo=2927).)

[`HTMLParser`](https://docs.python.org/3.14/library/html.parser.html#html.parser.HTMLParser) gains a fresh keyword argument named *convert_charrefs* which, set to `True`, will translate every character reference on its own. To keep older code working, the parameter starts out as `False`; a later Python release will flip that default to `True`, so consider passing it directly and adjusting your program to adopt the behavior now. (Contributed by Ezio Melotti in [bpo-13633](https://bugs.python.org/issue?@action=redirect&bpo=13633).)

The *strict* argument of [`HTMLParser`](https://docs.python.org/3.14/library/html.parser.html#html.parser.HTMLParser) has been marked deprecated. (Contributed by Ezio Melotti in [bpo-15114](https://bugs.python.org/issue?@action=redirect&bpo=15114).)

[Subject index](INDEX.md) · [Previous source section](hmac.md) · [Release/subject declaration](release-highlights.md) · [Next source section](http.md)
