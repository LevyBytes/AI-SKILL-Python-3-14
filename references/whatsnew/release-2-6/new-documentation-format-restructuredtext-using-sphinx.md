# What’s New in Python 2.6 / New Documentation Format: reStructuredText Using Sphinx

### New Documentation Format: reStructuredText Using Sphinx

Ever since the project got underway around 1989, the Python docs had been authored in LaTeX. Through the 1980s and the early years of the 1990s, most documentation got printed on paper for reading later rather than being read on a screen. LaTeX saw heavy use because its printed results looked good while staying easy to author once you’d picked up the markup’s basic conventions.

LaTeX remains in use today for producing works headed to the printer, but the world of programming tooling has moved on. Rather than printing stacks of documentation, we now read through it on the web, and HTML has risen to be the format that matters most. The trouble is that turning LaTeX into HTML is rather involved, and Fred L. Drake Jr., who edited the Python docs for many years, devoted considerable time to keeping that conversion going. Now and then someone would float the idea of moving the docs to SGML and afterward XML, but doing the conversion well is a sizable undertaking, and nobody ever put in the time to see it through.

Across the 2.6 development cycle, Georg Brandl invested heavily in assembling a new toolchain to handle the documentation. The package that came out of that work goes by the name Sphinx, and you can get it from [https://www.sphinx-doc.org/](https://www.sphinx-doc.org/).

Sphinx focuses on HTML, turning out cleanly styled, contemporary HTML; you can still get printed output by way of conversion to LaTeX. Its source format is reStructuredText, a markup language with support for custom directives and extensions that sees wide use within the Python community.

Sphinx stands on its own as a writing package, and close to twenty other projects ([listed on the Sphinx web site](https://www.sphinx-doc.org/en/master/examples.html)) have taken it up to handle their documentation.

See also

[Documenting Python](https://devguide.python.org/documenting/)

Describes how to write for Python’s documentation.

[Sphinx](https://www.sphinx-doc.org/)

Documentation and code for the Sphinx toolchain.

[Docutils](https://docutils.sourceforge.io)

The underlying reStructuredText parser and toolset.

[Subject index](INDEX.md) · [Previous source section](new-issue-tracker-roundup.md) · [Next source section](pep-343-the-with-statement.md) · [Release/subject declaration](python-3-0.md)
