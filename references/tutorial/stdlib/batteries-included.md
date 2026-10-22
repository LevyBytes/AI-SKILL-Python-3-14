# 10.12. Batteries included

### 10.12. Batteries included

Python embraces a “batteries included” outlook, most visible in the powerful, well-rounded features of its bigger packages. Consider:

- Thanks to the [`xmlrpc.client`](https://docs.python.org/3.14/library/xmlrpc.client.html#module-xmlrpc.client) and [`xmlrpc.server`](https://docs.python.org/3.14/library/xmlrpc.server.html#module-xmlrpc.server) modules, wiring up remote procedure calls becomes nearly effortless. Their names notwithstanding, you never have to touch or even understand XML directly.

- As a library for handling email messages — MIME among them, plus other [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)-style documents — the [`email`](https://docs.python.org/3.14/library/email.html#module-email) package stands apart from [`smtplib`](https://docs.python.org/3.14/library/smtplib.html#module-smtplib) and [`poplib`](https://docs.python.org/3.14/library/poplib.html#module-poplib), which genuinely transmit and receive mail. Instead it furnishes a full kit for assembling or parsing elaborate message structures (attachments included) and for carrying out internet encoding and header conventions.

- Parsing the well-liked JSON interchange format is solidly covered by the [`json`](https://docs.python.org/3.14/library/json.html#module-json) package. For files in Comma-Separated Value form — a format databases and spreadsheets widely understand — the [`csv`](https://docs.python.org/3.14/library/csv.html#module-csv) module reads and writes them directly. Handling XML falls to the [`xml.etree.ElementTree`](https://docs.python.org/3.14/library/xml.etree.elementtree.html#module-xml.etree.ElementTree), [`xml.dom`](https://docs.python.org/3.14/library/xml.dom.html#module-xml.dom) and [`xml.sax`](https://docs.python.org/3.14/library/xml.sax.html#module-xml.sax) packages. Taken together, this collection of modules and packages makes moving data between Python programs and outside tools far easier.

- Wrapping the SQLite database library, the [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) module gives you a persistent store you can read and modify through a mildly nonstandard dialect of SQL.

- A handful of modules cover internationalization, including [`gettext`](https://docs.python.org/3.14/library/gettext.html#module-gettext), [`locale`](https://docs.python.org/3.14/library/locale.html#module-locale), together with the [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs) package.

[Subject index](INDEX.md) · [Previous source section](quality-control.md)
