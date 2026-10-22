# unicodedata: Unicode properties, normalization and database versions

unicodedata.category(*chr*)

Hands back, as a string, the general category tied to the character *chr*. Each general category name is made of two letters. Consult the [General Category Values section of the Unicode Character Database documentation](https://www.unicode.org/reports/tr44/tr44-34.html#General_Category_Values) for the full set of category codes. As an illustration:

```python
>>> unicodedata.category('A')  # 'L'etter, 'u'ppercase
'Lu'

```

 unicodedata.bidirectional(*chr*)

Hands back, as a string, the bidirectional class tied to the character *chr*. When no such value exists, an empty string comes back. Refer to the [Bidirectional Class Values section of the Unicode Character Database](https://www.unicode.org/reports/tr44/tr44-34.html#Bidi_Class_Values) documentation for the complete list of bidirectional codes. As an illustration:

```python
>>> unicodedata.bidirectional('\N{ARABIC-INDIC DIGIT SEVEN}') # 'A'rabic, 'N'umber
'AN'

```

 unicodedata.combining(*chr*)

Hands back, as an integer, the canonical combining class tied to the character *chr*. It yields `0` whenever no combining class exists. For further detail, see the [Canonical Combining Class Values section of the Unicode Character Database](https://www.unicode.org/reports/tr44/tr44-34.html#Canonical_Combining_Class_Values).

 unicodedata.east_asian_width(*chr*)

Hands back, as a string, the east asian width tied to the character *chr*. To see the full set of widths, or for more detail, consult the [Unicode Standard Annex #11](https://www.unicode.org/reports/tr11/tr11-43.html).

 unicodedata.mirrored(*chr*)

Hands back, as an integer, the mirrored property tied to the character *chr*. It yields `1` when the character counts as a “mirrored” one within bidirectional text, and `0` if not. As an illustration:

```python
>>> unicodedata.mirrored('>')
1

```

 unicodedata.decomposition(*chr*)

Hands back, as a string, the character decomposition mapping tied to the character *chr*. Where no such mapping exists, what comes back is an empty string. As an illustration:

```python
>>> unicodedata.decomposition('Ã')
'0041 0303'

```

 unicodedata.normalize(*form*, *unistr*)

Give back the normal form *form* of the Unicode string *unistr*. The values *form* accepts are ‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’.

A range of normalization forms for a Unicode string is laid out by the Unicode standard, grounded in the notions of canonical equivalence and compatibility equivalence. Within Unicode, a single character can be written in more than one way. Take the character U+00C7 (LATIN CAPITAL LETTER C WITH CEDILLA): it may equally be written as the pair U+0043 (LATIN CAPITAL LETTER C) U+0327 (COMBINING CEDILLA).

Every character has two normal forms to consider — normal form C and normal form D. Normal form D (NFD), also called canonical decomposition, turns each character into its broken-apart form. Normal form C (NFC) runs a canonical decomposition first and then reassembles the pre-combined characters.

Beyond those two, a further pair of normal forms rests on compatibility equivalence. Unicode carries certain characters that ordinarily would have been merged with others. As an example, U+2160 (ROMAN NUMERAL ONE) is in truth identical to U+0049 (LATIN CAPITAL LETTER I), yet Unicode keeps it around to stay compatible with character sets already in use (gb2312, say).

Normal form KD (NFKD) carries out the compatibility decomposition — in other words, swaps every compatibility character for its equivalent. Normal form KC (NFKC) does the compatibility decomposition first and then the canonical composition.

Two unicode strings can be normalized and still appear identical to a person reading them, yet they might not test as equal when one carries combining characters and the other does not.

 unicodedata.is_normalized(*form*, *unistr*)

Give back whether the Unicode string *unistr* already sits in the normal form *form*. The values *form* accepts are ‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’.

Added in version 3.8.

On top of the functions, the module also surfaces this constant:

 unicodedata.unidata_version

Which version of the Unicode database this module draws on.

 unicodedata.ucd_3_2_0

An object carrying the very same methods as the whole module, except that it draws on Unicode database version 3.2, intended for applications that depend on exactly that release of the Unicode database (IDNA being one).

Footnotes

[Subject index](INDEX.md) · [Previous](unicodedata-lookup-to-unicodedata-numeric.md) · [Owning module, declaration or section: unicodedata](unicodedata-lookup-to-unicodedata-numeric.md)
