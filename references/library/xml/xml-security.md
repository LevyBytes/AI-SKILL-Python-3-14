# XML security

### XML security

Whenever attacker-controlled XML is parsed, whether in Python or elsewhere, an attacker may misuse XML features to mount denial of service attacks, reach local files, open network connections to other hosts, or bypass firewalls.

For parsing XML, Python's built-in XML parsers depend on the [libexpat](https://github.com/libexpat/libexpat) library, usually referred to as Expat.

Out of the box, Expat by itself neither reads local files nor opens network connections.

Versions of Expat below 2.7.2 can be exposed to the "billion laughs", "quadratic blowup" and "large tokens" vulnerabilities, or to excessive consumption of dynamic memory. A copy of Expat is bundled with Python, and whether Python relies on the bundled copy or a system-wide one is determined by how the Python interpreter [`has been configured`](https://docs.python.org/3.14/using/configure.html#cmdoption-with-system-expat) within your environment. If it relies on those older Expat versions, Python may be exposed. Inspect `pyexpat.EXPAT_VERSION`.

[`xmlrpc`](https://docs.python.org/3.14/library/xmlrpc.html#module-xmlrpc) is **vulnerable** to the "decompression bomb" attack.

billion laughs / exponential entity expansion

The [Billion Laughs](https://en.wikipedia.org/wiki/Billion_laughs) attack — also called exponential entity expansion — relies on several layers of nested entities. Every entity references another entity multiple times, and the last entity definition holds a short string. That exponential growth yields several gigabytes of text and burns through a great deal of memory and CPU time.

quadratic blowup entity expansion

A quadratic blowup attack resembles a [Billion Laughs](https://en.wikipedia.org/wiki/Billion_laughs) attack; it likewise exploits entity expansion. Rather than nesting entities, it repeats a single large entity, a few thousand characters long, again and again. Though less efficient than the exponential variant, it sidesteps parser defenses that prohibit deeply nested entities.

decompression bomb

Decompression bombs (aka [ZIP bomb](https://en.wikipedia.org/wiki/Zip_bomb)) affect every XML library capable of parsing compressed XML streams, such as gzipped HTTP streams or LZMA-compressed files. From an attacker's standpoint, this can shrink the volume of transmitted data by three orders of magnitude or beyond.

large tokens

Expat must re-parse unfinished tokens; absent the safeguard added in Expat 2.6.0, this can produce quadratic runtime exploitable to cause denial of service in the XML-parsing application. The flaw is tracked as [**CVE 2023-52425**](https://www.cve.org/CVERecord?id=CVE-2023-52425).

[Subject index](INDEX.md) · [Previous](xml-processing-modules.md) · [Continue](../xml-sax-handler/xml-sax-handler-contenthandler-class.md)
