# Headers

### Headers

Here we'll walk through a single HTTP header as a way of showing how headers get attached to an HTTP request of yours.

A number of websites [1] aren't fond of being visited by programs, or they hand out different versions depending on the browser [2]. Out of the box urllib announces itself as `Python-urllib/x.y` (here `x` and `y` stand for the major and minor version numbers of the Python release — for example `Python-urllib/2.5`), and that can throw a site off or simply fail outright. A browser advertises its identity by way of the `User-Agent` header [3]. As you build a Request object, you're free to supply a dictionary of headers. The example that follows issues the same request shown earlier, but presents itself as a build of Internet Explorer [4].

```python
import urllib.parse
import urllib.request

url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python' }
headers = {'User-Agent': user_agent}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)
with urllib.request.urlopen(req) as response:
   the_page = response.read()

```

A couple of handy methods live on the response as well. Those are covered in the info and geturl section, which follows once we've examined what unfolds when things break.

[Subject index](INDEX.md) · [Previous source context](data.md) · [Following source context](handling-exceptions.md)
