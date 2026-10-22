# urllib.parse — URL parsing security

### URL parsing security

The `urlsplit()` and `urlparse()` APIs do no **validation** of their inputs. They might not flag inputs that other applications would deem invalid. They might equally accept inputs that elsewhere would not pass as URLs. Their aim is practical usefulness, not purity.

Rather than throwing an exception on odd input, they may instead hand back certain component parts as empty strings. Or some components may hold rather more than they arguably ought to.

Where the values from these APIs may flow anywhere with security implications, we advise users to code defensively. Run some checks in your own code before placing trust in a returned component part. Is that `scheme` reasonable? Is that `path` plausible? Is anything off about that `hostname`? and so on.

There is no universal, well-settled definition of what a URL is. Applications differ in their needs and the constraints they want. The living [WHATWG spec](https://url.spec.whatwg.org/#concept-basic-url-parser), for one, lays out what user-facing web clients such as a web browser require, whereas [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html) is broader. These functions fold in elements of both yet cannot claim conformance to either. Because the APIs—and existing user code that expects particular behaviors—predate both standards, we are extremely careful about altering API behavior.

[Subject index](INDEX.md) · [Previous](urllib-parse-urljoin-to-urllib-parse-unwrap.md) · [Continue](parsing-ascii-encoded-bytes.md) · [Owning module, declaration or section: urllib.parse](urllib-parse-parse-urls-into-components.md)
