# Matching characters

### Matching characters

The vast majority of letters and characters just match themselves. To illustrate, the regular expression `test` matches the string `test` precisely. (A case-insensitive mode, discussed further on, would also let that RE match `Test` or `TEST`.)

This rule has exceptions; certain characters are special *metacharacters*, and they do not match themselves. Rather, they announce that something unusual ought to be matched, or they alter neighboring parts of the RE by repeating them or shifting their meaning. A large share of this document goes into the various metacharacters and their effects.

Below is the full roster of the metacharacters; what each one means gets covered through the remainder of this HOWTO.

```none
. ^ $ * + ? { } [ ] \ | ( )

```

The earliest metacharacters worth examining are `[` and `]`. They serve to define a character class, a collection of characters you want to match against. You can spell out characters one by one, or denote a span of characters by giving two of them split by a `'-'`. So `[abc]` will match any of the characters `a`, `b`, or `c`; the equivalent `[a-c]` uses a range to express the same set of characters. Were you after only lowercase letters, the RE you would write is `[a-z]`.

> Here the rule shifts: metacharacters (except `\`) are not active inside classes. For example, `[akm$]` will match any of the characters `'a'`, `'k'`, `'m'`, or `'$'`; `'$'` normally counts as a metacharacter, yet within a character class it loses that special role.

To match the characters that fall outside the class, *complement* the set. You signal this by placing a `'^'` at the very start of the class. So `[^5]` matches every character apart from `'5'`. Should the caret turn up anywhere other than the front of a character class, it carries no special meaning. As an example: `[5^]` matches either a `'5'` or a `'^'`.

> Arguably the metacharacter that matters most is the backslash, `\`. As in Python string literals, the backslash can be followed by various characters to signal various special sequences. It’s also used to escape all the metacharacters so you can still match them in patterns; for example, if you need to match a `[` or `\`, you can precede them with a backslash to remove their special meaning: `\[` or `\\`.

A number of the special sequences that start with `'\'` stand for handy predefined character sets, like the digits, the letters, or everything that is not whitespace.

Consider an example: `\w` matches any alphanumeric character. When the regex pattern is given as bytes, that is the same as the class `[a-zA-Z0-9_]`. When the regex pattern is given as a string, `\w` matches every character flagged as a letter in the Unicode database furnished by the [`unicodedata`](https://docs.python.org/3.14/library/unicodedata.html#module-unicodedata) module. To adopt the narrower meaning of `\w` within a string pattern, pass the [`re.ASCII`](https://docs.python.org/3.14/library/re.html#re.ASCII) flag at the time you compile the regular expression.

What follows is not the entire roster of special sequences. The full set of sequences plus the expanded class definitions for Unicode string patterns lives in the closing portion of [Regular Expression Syntax](https://docs.python.org/3.14/library/re.html#re-syntax) within the Standard Library reference. Broadly, the Unicode variants match whatever character belongs to the matching category in the Unicode database.

`\d`

Matches any decimal digit; this is equivalent to the class `[0-9]`.

`\D`

Matches any non-digit character; this is equivalent to the class `[^0-9]`.

`\s`

Matches any whitespace character; this is equivalent to the class `[ \t\n\r\f\v]`.

`\S`

Matches any non-whitespace character; this is equivalent to the class `[^ \t\n\r\f\v]`.

`\w`

Matches any alphanumeric character; this is equivalent to the class `[a-zA-Z0-9_]`.

`\W`

Matches any non-alphanumeric character; this is equivalent to the class `[^a-zA-Z0-9_]`.

You can drop these sequences into a character class too. Take `[\s,.]`, a character class that matches any whitespace character, or `','` or `'.'`.

The closing metacharacter for this section is `.`. It matches everything other than a newline, and a separate mode ([`re.DOTALL`](https://docs.python.org/3.14/library/re.html#re.DOTALL)) makes it match a newline as well. `.` tends to appear wherever you want to match “any character”.

[Subject index](INDEX.md) · [Previous source context](simple-patterns.md) · [Following source context](repeating-things.md)
