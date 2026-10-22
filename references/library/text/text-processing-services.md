# Text Processing Services

# Text, Textwrap

## Overview

Topics in this file: Text Processing Services; plus textwrap — Text wrapping and filling.

## Text Processing Services

### Text Processing Services

This chapter covers modules offering a broad assortment of string-handling operations along with other facilities for working with text.

For text work, the [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs) module — covered within [Binary Data Services](https://docs.python.org/3.14/library/binary.html#binaryservices) — is likewise quite pertinent. You should also consult the writeup of Python’s built-in string type over in [Text Sequence Type — str](https://docs.python.org/3.14/library/stdtypes.html#textseq).

- [`string` — Common string operations](https://docs.python.org/3.14/library/string.html)
  - [String constants](https://docs.python.org/3.14/library/string.html#string-constants)
  - [Custom string formatting](https://docs.python.org/3.14/library/string.html#custom-string-formatting)
  - [Format string syntax](https://docs.python.org/3.14/library/string.html#format-string-syntax)
    - [Format specification mini-language](https://docs.python.org/3.14/library/string.html#format-specification-mini-language)
    - [Format examples](https://docs.python.org/3.14/library/string.html#format-examples)

  - [Template strings ($-strings)](https://docs.python.org/3.14/library/string.html#template-strings-strings)
  - [Helper functions](https://docs.python.org/3.14/library/string.html#helper-functions)

- [`string.templatelib` — Support for template string literals](https://docs.python.org/3.14/library/string.templatelib.html)
  - [Template strings](https://docs.python.org/3.14/library/string.templatelib.html#template-strings)
  - [Types](https://docs.python.org/3.14/library/string.templatelib.html#types)
  - [Helper functions](https://docs.python.org/3.14/library/string.templatelib.html#helper-functions)

- [`re` — Regular expression operations](https://docs.python.org/3.14/library/re.html)
  - [Regular Expression Syntax](https://docs.python.org/3.14/library/re.html#regular-expression-syntax)
  - [Module Contents](https://docs.python.org/3.14/library/re.html#module-contents)
    - [Flags](https://docs.python.org/3.14/library/re.html#flags)
    - [Functions](https://docs.python.org/3.14/library/re.html#functions)
    - [Exceptions](https://docs.python.org/3.14/library/re.html#exceptions)

  - [Regular Expression Objects](https://docs.python.org/3.14/library/re.html#regular-expression-objects)
  - [Match Objects](https://docs.python.org/3.14/library/re.html#match-objects)
  - [Regular Expression Examples](https://docs.python.org/3.14/library/re.html#regular-expression-examples)
    - [Checking for a Pair](https://docs.python.org/3.14/library/re.html#checking-for-a-pair)
    - [Simulating scanf()](https://docs.python.org/3.14/library/re.html#simulating-scanf)
    - [search() vs. match()](https://docs.python.org/3.14/library/re.html#search-vs-match)
    - [Making a Phonebook](https://docs.python.org/3.14/library/re.html#making-a-phonebook)
    - [Text Munging](https://docs.python.org/3.14/library/re.html#text-munging)
    - [Finding all Adverbs](https://docs.python.org/3.14/library/re.html#finding-all-adverbs)
    - [Finding all Adverbs and their Positions](https://docs.python.org/3.14/library/re.html#finding-all-adverbs-and-their-positions)
    - [Raw String Notation](https://docs.python.org/3.14/library/re.html#raw-string-notation)
    - [Writing a Tokenizer](https://docs.python.org/3.14/library/re.html#writing-a-tokenizer)

- [`difflib` — Helpers for computing deltas](https://docs.python.org/3.14/library/difflib.html)
  - [SequenceMatcher objects](https://docs.python.org/3.14/library/difflib.html#sequencematcher-objects)
  - [SequenceMatcher examples](https://docs.python.org/3.14/library/difflib.html#sequencematcher-examples)
  - [Differ objects](https://docs.python.org/3.14/library/difflib.html#differ-objects)
  - [Differ example](https://docs.python.org/3.14/library/difflib.html#differ-example)
  - [A command-line interface to difflib](https://docs.python.org/3.14/library/difflib.html#a-command-line-interface-to-difflib)
  - [ndiff example](https://docs.python.org/3.14/library/difflib.html#ndiff-example)

- [`textwrap` — Text wrapping and filling](https://docs.python.org/3.14/library/textwrap.html)
- [`unicodedata` — Unicode Database](https://docs.python.org/3.14/library/unicodedata.html)
- [`stringprep` — Internet String Preparation](https://docs.python.org/3.14/library/stringprep.html)
- [`readline` — GNU readline interface](https://docs.python.org/3.14/library/readline.html)
  - [Init file](https://docs.python.org/3.14/library/readline.html#init-file)
  - [Line buffer](https://docs.python.org/3.14/library/readline.html#line-buffer)
  - [History file](https://docs.python.org/3.14/library/readline.html#history-file)
  - [History list](https://docs.python.org/3.14/library/readline.html#history-list)
  - [Startup hooks](https://docs.python.org/3.14/library/readline.html#startup-hooks)
  - [Completion](https://docs.python.org/3.14/library/readline.html#completion)
  - [Example](https://docs.python.org/3.14/library/readline.html#example)

- [`rlcompleter` — Completion function for GNU readline](https://docs.python.org/3.14/library/rlcompleter.html)

[Subject index](INDEX.md) · [Continue](../textwrap/textwrap-wrap-to-textwrap-dedent.md)
