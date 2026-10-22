# urllib.robotparser.RobotFileParser: `set_url()`, `read()`, `parse()`, `can_fetch()`, `mtime()`, `modified()`, `crawl_delay()`, `request_rate()`, `site_maps()`

set_url(*url*)

Sets the URL referring to a `robots.txt` file.

 read()

Reads the `robots.txt` URL and feeds it to the parser.

 parse(*lines*)

Parses the lines argument.

 can_fetch(*useragent*, *url*)

Gives back `True` when the *useragent* may fetch the *url* under the rules held in the parsed `robots.txt` file.

 mtime()

Gives back the moment the `robots.txt` file was most recently fetched. That comes in handy for long-running web spiders obliged to look for fresh `robots.txt` files at intervals.

 modified()

Sets the time the `robots.txt` file was last fetched to the current time.

 crawl_delay(*useragent*)

Gives back the value of the `Crawl-delay` parameter drawn from `robots.txt` for the *useragent* at hand. Where no such parameter exists, where it has no bearing on the *useragent* given, or where the `robots.txt` entry for this parameter carries invalid syntax, `None` is returned.

Added in version 3.6.

 request_rate(*useragent*)

Hands back what the `Request-rate` parameter from `robots.txt` holds, shaped as a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) `RequestRate(requests, seconds)`. Should that parameter be absent, should it not apply to the *useragent* given, or should the `robots.txt` entry for it bear invalid syntax, the return is `None`.

Added in version 3.6.

 site_maps()

Yields what the `Sitemap` parameter from `robots.txt` contains, packaged as a [`list()`](https://docs.python.org/3.14/library/stdtypes.html#list). When that parameter is missing or the `robots.txt` entry for it has invalid syntax, the return value is `None`.

Added in version 3.8.

The example that follows shows the `RobotFileParser` class in basic use:

```python
>>> import urllib.robotparser
>>> rp = urllib.robotparser.RobotFileParser()
>>> rp.set_url("http://www.pythontest.net/robots.txt")
>>> rp.read()
>>> rrate = rp.request_rate("*")
>>> rrate.requests
1
>>> rrate.seconds
1
>>> rp.crawl_delay("*")
6
>>> rp.can_fetch("*", "http://www.pythontest.net/")
True
>>> rp.can_fetch("*", "http://www.pythontest.net/no-robots-here/")
False

```

[Subject index](INDEX.md) · [Previous](urllib-robotparser-robotfileparser-class.md) · [Continue](../uu/uu-encode-and-decode-uuencode-files.md) · [Owning module, declaration or section: urllib.robotparser](urllib-robotparser-robotfileparser-class.md) · [Owning module, declaration or section: urllib.robotparser.RobotFileParser](urllib-robotparser-robotfileparser-class.md)
