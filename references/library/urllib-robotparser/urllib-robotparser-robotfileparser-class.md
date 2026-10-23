# urllib.robotparser: `urllib.robotparser.RobotFileParser`

### `urllib.robotparser` - Parser for robots.txt

**Source code:** [Lib/urllib/robotparser.py](https://github.com/python/cpython/tree/3.14/Lib/urllib/robotparser.py)

---

A lone class, `RobotFileParser`, is what this module offers; it fields questions about whether some given user agent is permitted to fetch a URL on the site that put out the `robots.txt` file. To learn more about how `robots.txt` files are laid out, consult [**RFC 9309**](https://datatracker.ietf.org/doc/html/rfc9309.html).

 *class *urllib.robotparser.RobotFileParser(*url=''*)

Methods on this class let you read, parse, and field questions concerning the `robots.txt` file located at *url*.

[Subject index](INDEX.md) · [Previous](parser-for-robots-txt.md) · [Continue](robots-parser-access-rules-and-sitemaps.md)
