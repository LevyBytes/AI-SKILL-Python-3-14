# Unicode Properties

### Unicode Properties

A database of details about code points forms part of the Unicode specification. For every defined code point, the details cover the character’s name, its category, and the numeric value where relevant (for characters that stand for numeric concepts such as the Roman numerals, fractions like one-third and four-fifths, and so on). Display-related properties are present too, for instance how the code point should be used in bidirectional text.

The program below shows a bit of information about several characters and prints the numeric value of one specific character:

```python
import unicodedata

u = chr(233) + chr(0x0bf2) + chr(3972) + chr(6000) + chr(13231)

for i, c in enumerate(u):
    print(i, '%04x' % ord(c), unicodedata.category(c), end=" ")
    print(unicodedata.name(c))

# Get numeric value of second character
print(unicodedata.numeric(u[1]))

```

Running it produces:

```none
0 00e9 Ll LATIN SMALL LETTER E WITH ACUTE
1 0bf2 No TAMIL NUMBER ONE THOUSAND
2 0f84 Mn TIBETAN MARK HALANTA
3 1770 Lo TAGBANWA LETTER SA
4 33af So SQUARE RAD OVER S SQUARED
1000.0

```

The category codes are abbreviations spelling out what sort of character it is. They fall into groupings such as “Letter”, “Number”, “Punctuation”, or “Symbol”, each of which then splits into subcategories. Drawing on the codes from the output above, `'Ll'` stands for ‘Letter, lowercase’, `'No'` stands for “Number, other”, `'Mn'` is “Mark, nonspacing”, and `'So'` is “Symbol, other”. Refer to [the General Category Values section of the Unicode Character Database documentation](https://www.unicode.org/reports/tr44/#General_Category_Values) for the full list of category codes.

[Subject index](INDEX.md) · [Previous source context](unicode-literals-in-python-source-code.md) · [Following source context](comparing-strings.md)
