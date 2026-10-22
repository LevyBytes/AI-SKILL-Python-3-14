# Data

### Data

There are times when you'll want to push data toward a URL (frequently one pointing at a CGI (Common Gateway Interface) script or some other web application). Over HTTP, the usual vehicle for this is the **POST** request. It's the very thing your browser performs when you fill out an HTML form on the web and submit it. POSTs needn't originate from forms, though — you can employ one to ship arbitrary data into an application of your own. For the everyday HTML-form scenario, the data has to be encoded in a standard fashion before being handed to the Request object through its `data` argument. A function out of the [`urllib.parse`](https://docs.python.org/3.14/library/urllib.parse.html#module-urllib.parse) library performs that encoding.

```python
import urllib.parse
import urllib.request

url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
   the_page = response.read()

```

Keep in mind that certain situations call for different encodings (uploading a file from an HTML form, for one — consult [HTML Specification, Form Submission](https://www.w3.org/TR/REC-html40/interact/forms.html#h-17.13) for the specifics).

Leave out the `data` argument and urllib falls back to a **GET** request. A notable contrast between GET and POST is that POST requests tend to carry “side-effects” — they alter the system's state somehow (say, by ordering a hundredweight of tinned spam from the website to be shipped to your doorstep). Even though the HTTP standard spells out that POSTs are supposed to *always* trigger side-effects while GET requests are supposed to *never* do so, nothing actually stops a GET from producing side-effects or a POST from producing none. You can likewise convey data inside an HTTP GET request by baking it into the URL itself.

This is done as follows:

```python
>>> import urllib.request
>>> import urllib.parse
>>> data = {}
>>> data['name'] = 'Somebody Here'
>>> data['location'] = 'Northampton'
>>> data['language'] = 'Python'
>>> url_values = urllib.parse.urlencode(data)
>>> print(url_values)  # The order may differ from below.
name=Somebody+Here&language=Python&location=Northampton
>>> url = 'http://www.example.com/example.cgi'
>>> full_url = url + '?' + url_values
>>> data = urllib.request.urlopen(full_url)

```

Observe how the complete URL is assembled by appending a `?` to it and then tacking the encoded values on after that.

[Subject index](INDEX.md) · [Previous source context](fetching-urls.md) · [Following source context](headers.md)
