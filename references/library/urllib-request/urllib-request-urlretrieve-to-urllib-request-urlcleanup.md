# urllib.request — Legacy interface

### Legacy interface

The functions and classes below were carried over from the Python 2 `urllib` module (not from `urllib2`). It is possible they will be deprecated somewhere down the road.

`urllib.request.urlretrieve(*url*, *filename=None*, *reporthook=None*, *data=None*)`

Fetch a network object identified by a URL and write it to a local file. When the URL refers to a file that is already local, no copy happens unless you provide filename. The return value is a tuple `(filename, headers)`, in which *filename* gives the local file name where the object can be located, and *headers* (for a remote object) is whatever the `info()` method on the object that `urlopen()` returned produced. The exceptions raised match those of `urlopen()`.

Where the second argument appears, it names the file location to copy into (and when it is missing, that location becomes a tempfile whose name is generated). Where the third argument appears, it is a callable invoked once as the network connection is set up and again following every block that is subsequently read. Three arguments reach that callable: how many blocks have moved so far, the block size in bytes, and the file's overall size. On older FTP servers that send back no file size when asked to retrieve, this third argument can come through as `-1`.

Here is an example showing the way it is most often used:

```python
>>> import urllib.request
>>> local_filename, headers = urllib.request.urlretrieve('https://python.org/')
>>> html = open(local_filename)
>>> html.close()

```

When the *url* carries the `http:` scheme identifier, you can supply the optional *data* argument to request a `POST` (the request type defaults to `GET`). That *data* argument has to be a bytes object laid out in the standard *application/x-www-form-urlencoded* format; refer to the [`urllib.parse.urlencode()`](https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.urlencode) function.

A [`ContentTooShortError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.ContentTooShortError) gets raised by `urlretrieve()` once it notices that less data was on hand than anticipated (the anticipated figure being whatever a *Content-Length* header states). An interrupted download is one situation where this happens.

Here *Content-Length* counts as a floor: should additional data remain, urlretrieve keeps reading it, yet should the available data fall short, it throws the exception.

Even then, the data you downloaded remains within reach, since it sits in the exception instance's `content` attribute.

Absent any *Content-Length* header, urlretrieve has no way to verify how large the downloaded data is, so it simply hands it back. You are then left to presume the download went through fine.

 urllib.request.urlcleanup()

Clears out whatever temporary files earlier `urlretrieve()` calls might have left lying around.

[Subject index](INDEX.md) · [Previous](examples.md) · [Continue](urllib-request-restrictions.md) · [Owning module, declaration or section: urllib.request](urllib-request-urlopen-to-urllib-request-build-opener.md)
