# doctest.DocTestParser: `get_doctest()`, `get_examples()`, `parse()`

get_doctest(*string*, *globs*, *name*, *filename*, *lineno*)

Pull every doctest example out of the supplied string and gather them into a `DocTest` object.

The new `DocTest` object takes *globs*, *name*, *filename*, and *lineno* as its attributes. Further detail lives in the `DocTest` documentation.

 get_examples(*string*, *name='&lt;string&gt;'*)

Pull every doctest example out of the supplied string and give them back as a list of `Example` objects. The line numbering starts at 0. That optional *name* argument labels this string and figures only into error messages.

 parse(*string*, *name='&lt;string&gt;'*)

Split the supplied string into examples plus the text between them, then give it back as a list that alternates `Example`s with strings. Numbering for the `Example`s begins at 0. That optional *name* argument labels this string and comes into play only within error messages.

[Subject index](INDEX.md) · [Previous](doctest-doctestparser-class.md) · [Continue](doctest-testresults-class.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md) · [Owning module, declaration or section: doctest.DocTestParser](doctest-doctestparser-class.md) · [Owning module, declaration or section: DocTestParser objects](doctest-doctestparser-class.md)
