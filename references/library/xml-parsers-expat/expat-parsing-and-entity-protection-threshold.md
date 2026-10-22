# xml.parsers.expat: Expat parsing, external entities and protection thresholds

### XMLParser Objects

`xmlparser` objects have the following methods:

 xmlparser.Parse(*data*[, *isfinal*])

Parses the contents of the string *data*, invoking the right handler functions to process what was parsed. *isfinal* has to be true on the last call to this method; it permits parsing one file in fragments, not submitting several files. *data* may be the empty string at any point.

 xmlparser.ParseFile(*file*)

Parse XML data read from the object *file*. *file* needs only to supply the `read(nbytes)` method, returning the empty string when no more data remains.

 xmlparser.SetBase(*base*)

Sets the base used to resolve relative URIs found in system identifiers within declarations. Resolving relative identifiers is left up to the application: this value gets passed straight through as the *base* argument to the `ExternalEntityRefHandler()`, `NotationDeclHandler()`, and `UnparsedEntityDeclHandler()` functions.

 xmlparser.GetBase()

Returns a string holding the base set by an earlier call to `SetBase()`, or `None` when `SetBase()` was never called.

 xmlparser.GetInputContext()

Returns, as a string, the input data that produced the current event. The data is in the encoding of the entity that holds the text. When invoked while no event handler is active, the value returned is `None`.

 xmlparser.ExternalEntityParserCreate(*context*[, *encoding*])

Create a "child" parser for parsing an external parsed entity that content the parent parser parsed refers to. The *context* parameter ought to be the string handed to the `ExternalEntityRefHandler()` handler function covered below. That child parser comes with its `ordered_attributes` and `specified_attributes` set to this parser's values.

 xmlparser.SetParamEntityParsing(*flag*)

Control parsing of parameter entities (the external DTD subset included). The possible *flag* values are `XML_PARAM_ENTITY_PARSING_NEVER`, `XML_PARAM_ENTITY_PARSING_UNLESS_STANDALONE` and `XML_PARAM_ENTITY_PARSING_ALWAYS`. Returns true when setting the flag worked.

 xmlparser.UseForeignDTD([*flag*])

Calling this with a true value for *flag* (the default) makes Expat invoke the `ExternalEntityRefHandler` with [`None`](https://docs.python.org/3.14/library/constants.html#None) for every argument, so that an alternate DTD can be loaded. When the document carries no document type declaration, the `ExternalEntityRefHandler` is still invoked, but the `StartDoctypeDeclHandler` and `EndDoctypeDeclHandler` are not.

Passing a false value for *flag* undoes an earlier call that passed a true value, but otherwise does nothing.

This method may be called only before the `Parse()` or `ParseFile()` methods are called; calling it after either of those has run causes `ExpatError` to be raised with its [`code`](https://docs.python.org/3.14/library/code.html#module-code) attribute set to `errors.codes[errors.XML_ERROR_CANT_CHANGE_FEATURE_ONCE_PARSING]`.

 xmlparser.SetReparseDeferralEnabled(*enabled*)

Warning

There are security implications to calling `SetReparseDeferralEnabled(False)`, spelled out below; do be sure you grasp these consequences before you reach for the `SetReparseDeferralEnabled` method.

Expat 2.6.0 brought in a security mechanism dubbed "reparse deferral": rather than triggering denial of service through quadratic runtime from reparsing large tokens, the reparsing of unfinished tokens is now held off by default until enough input has arrived. Owing to that delay, registered handlers may — depending on how the input chunks pushed to Expat are sized — no longer fire immediately after new input is pushed to the parser. Where you want both immediate feedback and the duty of guarding against denial of service from large tokens, calling `SetReparseDeferralEnabled(False)` switches off reparse deferral for the current Expat parser instance, whether for a while or permanently. Calling `SetReparseDeferralEnabled(True)` lets you re-enable reparse deferral.

Be aware that, as a security fix, `SetReparseDeferralEnabled()` has been backported into a number of earlier CPython releases. Test whether `SetReparseDeferralEnabled()` is present via [`hasattr()`](https://docs.python.org/3.14/library/functions.html#hasattr) when your code has to run on an assortment of Python versions.

Added in version 3.13.

 xmlparser.GetReparseDeferralEnabled()

Reports whether reparse deferral is presently turned on for the Expat parser instance in question.

Added in version 3.13.

To tune the protections against several common XML vulnerabilities, `xmlparser` objects offer the following methods.

 xmlparser.SetBillionLaughsAttackProtectionActivationThreshold(*threshold*, */*)

Sets how many output bytes are needed to switch on protection against [billion laughs](https://en.wikipedia.org/wiki/Billion_laughs_attack) attacks.

That count of output bytes takes in the amplification from entity expansion and from reading DTD files.

A parser object's protection activation threshold is normally 8 MiB, though the real default hinges on the underlying Expat library.

An `ExpatError` is raised when this method runs against a non-root parser. The matching `lineno` and `offset` should not be relied on, as they may carry no special meaning.

Note

Setting activation thresholds under 4 MiB is known to break DITA 1.3 payload support, so it is not advised.

Added in version 3.14.6.

[Subject index](INDEX.md) · [Previous](expat-parser-factory-and-exception.md) · [Continue](expat-amplification-protection-and-error-position.md) · [Owning module, declaration or section: xml.parsers.expat](expat-parser-factory-and-exception.md)
