# stringprep: Stringprep character-table membership predicates

## stringprep — Internet String Preparation

### `stringprep` — Internet String Preparation

**Source code:** [Lib/stringprep.py](https://github.com/python/cpython/tree/3.14/Lib/stringprep.py)

---

Whenever you name entities (host names, say) on the internet, you frequently have to test two such names for “equality”. The precise way that test runs can hinge on the application domain - for instance, whether or not it ought to ignore letter case. On top of that, you may have to limit which names are permitted, accepting only those built solely from “printable” characters.

A procedure for “preparing” Unicode strings within internet protocols is laid out by [**RFC 3454**](https://datatracker.ietf.org/doc/html/rfc3454.html). Strings get run through this preparation step before they head out over the wire, leaving them in a fixed normalized shape. The RFC spells out a collection of tables that you can bundle together into profiles. Every profile has to state the tables it draws on, plus whichever optional pieces of the `stringprep` procedure it includes. A familiar example of a `stringprep` profile is `nameprep`, employed for internationalized domain names.

Only the tables from [**RFC 3454**](https://datatracker.ietf.org/doc/html/rfc3454.html) are surfaced by the `stringprep` module. Since holding those tables as dictionaries or lists would be enormous, the module leans on the Unicode character database under the hood. Its own source was itself produced by the `mkstringprep.py` utility.

Because of that, the tables show up as functions rather than as data structures. The RFC carries two sorts of tables: sets and mappings. With a set, `stringprep` hands you a “characteristic function” - that is, one that gives back `True` when the argument belongs to the set. With a mapping, it hands you the mapping function, which takes the key and returns its paired value. What follows is a roster of every function the module makes available.

 stringprep.in_table_a1(*code*)

Check whether *code* falls within tableA.1 (Unassigned code points in Unicode 3.2).

 stringprep.in_table_b1(*code*)

Check whether *code* falls within tableB.1 (Commonly mapped to nothing).

 stringprep.map_table_b2(*code*)

Hand back the value that *code* maps to under tableB.2 (Mapping for case-folding used with NFKC).

 stringprep.map_table_b3(*code*)

Hand back the value that *code* maps to under tableB.3 (Mapping for case-folding used with no normalization).

 stringprep.in_table_c11(*code*)

Check whether *code* falls within tableC.1.1 (ASCII space characters).

 stringprep.in_table_c12(*code*)

Check whether *code* falls within tableC.1.2 (Non-ASCII space characters).

 stringprep.in_table_c11_c12(*code*)

Check whether *code* falls within tableC.1 (Space characters, the combination of C.1.1 together with C.1.2).

 stringprep.in_table_c21(*code*)

Check whether *code* falls within tableC.2.1 (ASCII control characters).

 stringprep.in_table_c22(*code*)

Check whether *code* falls within tableC.2.2 (Non-ASCII control characters).

 stringprep.in_table_c21_c22(*code*)

Check whether *code* falls within tableC.2 (Control characters, the combination of C.2.1 together with C.2.2).

 stringprep.in_table_c3(*code*)

Check whether *code* falls within tableC.3 (Private use).

 stringprep.in_table_c4(*code*)

Check whether *code* falls within tableC.4 (Non-character code points).

 stringprep.in_table_c5(*code*)

Check whether *code* falls within tableC.5 (Surrogate codes).

 stringprep.in_table_c6(*code*)

Check whether *code* falls within tableC.6 (Inappropriate for plain text).

 stringprep.in_table_c7(*code*)

Check whether *code* falls within tableC.7 (Inappropriate for canonical representation).

 stringprep.in_table_c8(*code*)

Check whether *code* falls within tableC.8 (Change display properties or are deprecated).

 stringprep.in_table_c9(*code*)

Check whether *code* falls within tableC.9 (Tagging characters).

[Subject index](INDEX.md) · [Continue](stringprep-in-table-d1-to-stringprep-in-table-d2.md)
