# xml.parsers.expat - Content Model Descriptions

### Content Model Descriptions

A content model is expressed through nested tuples. Every tuple holds four entries — the type, the quantifier, the name, and a tuple holding the children. Each child is itself just another content model description.

For the leading pair of fields, the permitted values are constants living in the `xml.parsers.expat.model` module. You can sort those constants into a pair of categories: one for the model type and one for the quantifier.

Within the model type category you will find these constants:

 xml.parsers.expat.model.XML_CTYPE_ANY

The element identified by the model name was given a content model of `ANY` in its declaration.

 xml.parsers.expat.model.XML_CTYPE_CHOICE

The element in question permits selecting one among several alternatives; content models like `(A | B | C)` rely on this.

 xml.parsers.expat.model.XML_CTYPE_EMPTY

This is the model type carried by elements whose declaration marks them `EMPTY`.

 xml.parsers.expat.model.XML_CTYPE_MIXED

 xml.parsers.expat.model.XML_CTYPE_NAME

 xml.parsers.expat.model.XML_CTYPE_SEQ

When a model stands for a sequence of models lined up in succession, this model type flags it. Models written like `(A, B, C)` use it.

Within the quantifier category you will find these constants:

 xml.parsers.expat.model.XML_CQUANT_NONE

With no modifier supplied, it occurs precisely one time, the way `A` does.

 xml.parsers.expat.model.XML_CQUANT_OPT

Here the model is optional, showing up either a single time or never, like `A?`.

 xml.parsers.expat.model.XML_CQUANT_PLUS

The model has to show up at least once, possibly more (as in `A+`).

 xml.parsers.expat.model.XML_CQUANT_REP

The model is allowed any count from none upward, the way `A*` is.

[Subject index](INDEX.md) · [Previous](example.md) · [Continue](expat-parse-and-document-structure-errors.md) · [Owning module, declaration or section: xml.parsers.expat](expat-parser-factory-and-exception.md)
