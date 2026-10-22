# Definitions

### Introduction to Unicode

### Definitions

Software written today has to cope with an enormous range of characters. Programs are frequently internationalized so that their messages and output can appear in whichever language the user selects; a single program might be asked to emit an error message in English, French, Japanese, Hebrew, or Russian. Any of these languages may appear in web content, which can also carry assorted emoji symbols. Because Python’s string type relies on the Unicode Standard to represent characters, Python programs are able to handle all of these varied characters.

Unicode ([https://www.unicode.org/](https://www.unicode.org/)) is a specification whose goal is to catalog every character that human languages use and assign each one a unique code. The Unicode specifications get revised and updated over time so that fresh languages and symbols can be added.

A **character** is the most basic unit a text can be broken down into. ‘A’, ‘B’, ‘C’, and so on are each distinct characters. The same goes for ‘È’ and ‘Í’. Which characters exist depends on the language or context under discussion. As an illustration, there is a “Roman Numeral One” character, ‘Ⅰ’, that is distinct from the capital letter ‘I’. The two normally appear identical, yet they are separate characters carrying different meanings.

According to the Unicode standard, characters are denoted by **code points**. Each code point is an integer somewhere in the range 0 to 0x10FFFF (roughly 1.1 million possible values, though the [actual number assigned](https://www.unicode.org/versions/latest/#Summary) falls short of that). Throughout the standard and this document, a code point appears in the notation `U+265E`, meaning the character whose value is `0x265e` (9,822 in decimal).

Numerous tables in the Unicode standard enumerate characters alongside their associated code points:

```none
0061    'a'; LATIN SMALL LETTER A
0062    'b'; LATIN SMALL LETTER B
0063    'c'; LATIN SMALL LETTER C
...
007B    '{'; LEFT CURLY BRACKET
...
2167    'Ⅷ'; ROMAN NUMERAL EIGHT
2168    'Ⅸ'; ROMAN NUMERAL NINE
...
265E    '♞'; BLACK CHESS KNIGHT
265F    '♟'; BLACK CHESS PAWN
...
1F600   '😀'; GRINNING FACE
1F609   '😉'; WINKING FACE
...

```

Taken literally, these definitions mean that the phrase ‘this is character `U+265E`’ has no real meaning. `U+265E` is a code point standing in for one specific character; here it stands for the character ‘BLACK CHESS KNIGHT’, ‘♞’. Casually, though, people sometimes overlook this code-point-versus-character distinction.

When a character is shown on a screen or printed on paper, it appears as a collection of graphical elements known as a **glyph**. For an uppercase A, for instance, the glyph consists of two diagonal strokes plus a horizontal stroke, although the precise look hinges on the chosen font. Glyphs rarely concern most Python code; selecting the right glyph to render is usually handled by a GUI toolkit or a terminal’s font renderer.

[Subject index](INDEX.md) · [Previous source context](unicode-howto.md) · [Following source context](encodings.md)
