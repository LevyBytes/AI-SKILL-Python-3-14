# difflib: `difflib.Differ`

*class *difflib.Differ

This class contrasts sequences of lines of text and emits human-readable differences, or deltas. Differ relies on `SequenceMatcher` both to line up the sequences of lines and to line up the sequences of characters inside lines that are alike (near-matching).

Every line of a `Differ` delta opens with a two-letter code:

| Code | Meaning |
| --- | --- |
| `'- '` | line unique to sequence 1 |
| `'+ '` | line unique to sequence 2 |
| `' '` | line common to both sequences |
| `'? '` | line not present in either input sequence |

Lines that open with "`?`" try to draw the reader's attention toward intraline differences and were absent from both input sequences. Such lines may prove confusing whenever the sequences hold whitespace characters like spaces, tabs or line breaks.

### Differ objects

Bear in mind that the deltas `Differ` produces make no claim to being **minimal** diffs. Quite the opposite: minimal diffs are frequently counter-intuitive, because they synch up wherever they can, occasionally on chance matches 100 pages apart. Confining synch points to contiguous matches keeps some sense of locality, at the periodic price of a longer diff.

The `Differ` class is built by this constructor:

 *class *difflib.Differ(*linejunk=None*, *charjunk=None*)

The optional keyword parameters *linejunk* and *charjunk* serve as filter functions (or `None`):

*linejunk*: A function taking one string argument that returns true when the string is junk. Its default is `None`, which means no line is regarded as junk.

*charjunk*: A function taking a single character argument (a string of length 1) that returns true when the character is junk. Its default is `None`, which means no character is regarded as junk.

These junk-filtering functions hasten the matching that locates differences and never lead to any differing lines or characters being skipped. For an explanation, read the description of the *isjunk* parameter on the `find_longest_match()` method.

`Differ` objects are put to use (deltas produced) through a single method:

[Subject index](INDEX.md) · [Previous](difflib-sequencematcher-class.md) · [Continue](difflib-htmldiff-class-to-difflib-htmldiff-make-table.md) · [Owning module, declaration or section: difflib](difflib-sequencematcher-class.md) · [Previous](sequencematcher-examples.md) · [Continue](difflib-differ-compare.md)
