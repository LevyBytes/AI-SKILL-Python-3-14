# info and geturl

### info and geturl

Whatever urlopen gives back (or the [`HTTPError`](https://docs.python.org/3.14/library/urllib.error.html#urllib.error.HTTPError) instance) comes with two handy methods, `info()` and `geturl()`, and lives in the [`urllib.response`](https://docs.python.org/3.14/library/urllib.request.html#module-urllib.response) module.

- **geturl** - hands back the genuine URL of the page that was retrieved. That matters because `urlopen` (or whatever opener object was in play) might have chased a redirect, so the URL of the page you actually got may differ from the one you asked for.

- **info** - hands back a dictionary-style object describing the retrieved page, most notably the headers the server transmitted. At present it's an [`http.client.HTTPMessage`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPMessage) instance.

Headers you'll usually find here are ‘Content-length’, ‘Content-type’, and the like. The [Quick Reference to HTTP Headers](https://jkorpela.fi/http.html) offers a handy catalog of HTTP headers along with short notes on what each means and how it's used.

[Subject index](INDEX.md) · [Previous source context](combined-http-transport-handler.md) · [Following source context](openers-and-handlers.md)
