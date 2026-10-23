# sqlite3 - How to handle non-UTF-8 text encodings

### How to handle non-UTF-8 text encodings

As shipped, `sqlite3` relies on [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) when adapting SQLite values that carry the `TEXT` data type. That is fine for UTF-8 text, yet it can break on other encodings and on malformed UTF-8. A `text_factory` of your own can cover those situations.

Thanks to SQLite’s [flexible typing](https://www.sqlite.org/flextypegood.html), columns declared with the `TEXT` data type quite often hold non-UTF-8 encodings, or even raw arbitrary data. As an illustration, picture a database holding text in ISO-8859-2 (Latin-2) — say, a table of Czech-English dictionary entries. Given a `Connection` instance `con` already opened against that database, the Latin-2 text can be decoded with this `text_factory`:

```python
con.text_factory = lambda data: str(data, encoding="latin2")

```

When `TEXT` columns store malformed UTF-8 or arbitrary bytes, the approach below — taken from the [Unicode HOWTO](https://docs.python.org/3.14/howto/unicode.html#unicode-howto) — does the job:

```python
con.text_factory = lambda data: str(data, errors="surrogateescape")

```

Note

Strings that hold surrogates are not handled by the `sqlite3` module API.

See also

[Unicode HOWTO](https://docs.python.org/3.14/howto/unicode.html#unicode-howto)

[Subject index](INDEX.md) · [Previous](how-to-create-and-use-row-factories.md) · [Continue](transaction-control.md) · [Owning module, declaration or section: sqlite3](sqlite3-db-api-2-0-interface-for-sqlite-databases.md)
