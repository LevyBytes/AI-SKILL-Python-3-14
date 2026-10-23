# csv`csv` - CSV File Reading and Writing

# Csv

### `csv` - CSV File Reading and Writing

**Source code:** [Lib/csv.py](https://github.com/python/cpython/tree/3.14/Lib/csv.py)

---

What people call CSV (Comma Separated Values) is far and away the leading format for moving data into and out of spreadsheets and databases. The format had already seen heavy use for years before anyone tried to pin it down formally in [**RFC 4180**](https://datatracker.ietf.org/doc/html/rfc4180.html). Because no firm standard was ever settled on, small variations routinely crop up between what one program emits and what another expects. Such inconsistencies turn handling CSV files drawn from several origins into a chore. Even so, although the separators and quote markers differ from case to case, the broad shape stays close enough that a single module can manipulate this data effectively, shielding the programmer from the mechanics of reading and writing it.

Classes for reading and writing tabular data as CSV are supplied by the `csv` module. A programmer can effectively request, "store this data the way Excel likes it," or "pull data out of this Excel-produced file," with no need to grasp exactly how Excel renders CSV internally. Beyond Excel, a programmer may also characterize the CSV layouts that other tools recognize, or set up their own bespoke CSV formats.

Sequences are what the `csv` module's `reader` and `writer` objects consume and produce. For working with rows as dictionaries instead, the `DictReader` and `DictWriter` classes are available.

See also

[**PEP 305**](https://peps.python.org/pep-0305/) - CSV File API

The Python Enhancement Proposal that put forward adding this capability to the language.

[Subject index](INDEX.md) · [Continue](csv-reader-to-csv-field-size-limit.md)
