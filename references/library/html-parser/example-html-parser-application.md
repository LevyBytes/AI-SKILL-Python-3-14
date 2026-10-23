# html.parser - Example HTML Parser Application

### Example HTML Parser Application

For a starting illustration, what follows is a minimal HTML parser built on the `HTMLParser` class that echoes start tags, end tags, and data the moment each one shows up:

```python
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')

```

What it prints is the following:

```none
Encountered a start tag: html
Encountered a start tag: head
Encountered a start tag: title
Encountered some data  : Test
Encountered an end tag : title
Encountered an end tag : head
Encountered a start tag: body
Encountered a start tag: h1
Encountered some data  : Parse me!
Encountered an end tag : h1
Encountered an end tag : body
Encountered an end tag : html

```

[Subject index](INDEX.md) · [Previous](html-parser-htmlparser-class.md) · [Continue](htmlparser-feed-to-htmlparser-handle-pi.md) · [Owning module, declaration or section: html.parser](html-parser-htmlparser-class.md)
