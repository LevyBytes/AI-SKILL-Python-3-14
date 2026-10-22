# xml.parsers.expat: Amplification protection, buffer settings and error position

xmlparser.SetBillionLaughsAttackProtectionMaximumAmplification(*max_factor*, */*)

Sets the largest tolerated amplification factor for protection against [billion laughs](https://en.wikipedia.org/wiki/Billion_laughs_attack) attacks.

During parsing, the amplification factor is computed as `(direct + indirect) / direct`, where `direct` counts the bytes read from the primary document while parsing and `indirect` counts the bytes added by expanding entities and reading external DTD files.

The *max_factor* value has to be a non-NaN [`float`](https://docs.python.org/3.14/library/functions.html#float) value at or above 1.0. Real-world observations with small benign files show peak amplifications of factor 15,000 across the whole payload and of factor 30,000 mid-parse. The activation threshold above all should be picked with care to keep false positives away.

A parser object's maximum amplification factor is normally 100, though the real default hinges on the underlying Expat library.

An `ExpatError` is raised when this method runs against a non-root parser or when *max_factor* falls outside the valid range. The matching `lineno` and `offset` should not be relied on, as they may carry no special meaning.

Note

The maximum amplification factor only comes into play once the threshold adjustable through `SetBillionLaughsAttackProtectionActivationThreshold()` has been exceeded.

Added in version 3.14.6.

 xmlparser.SetAllocTrackerActivationThreshold(*threshold*, */*)

Sets how many bytes of dynamic memory must be allocated to switch on protection against runaway RAM use.

A parser object's allocation activation threshold is normally 64 MiB, though the real default hinges on the underlying Expat library.

An `ExpatError` is raised when this method runs against a non-root parser. The matching `lineno` and `offset` should not be relied on, as they may carry no special meaning.

Added in version 3.14.1.

 xmlparser.SetAllocTrackerMaximumAmplification(*max_factor*, */*)

Sets the largest amplification factor between direct input and bytes of dynamic memory allocated.

During parsing, the amplification factor is computed as `allocated / direct`, where `direct` counts the bytes read from the primary document while parsing and `allocated` counts the bytes of dynamic memory allocated across the parser hierarchy.

The *max_factor* value has to be a non-NaN [`float`](https://docs.python.org/3.14/library/functions.html#float) value at or above 1.0. Even with benign files, amplification factors above 100.0 can be observed near the start of parsing. The activation threshold above all should be picked with care to keep false positives away.

A parser object's maximum amplification factor is normally 100, though its real default hinges on the underlying Expat library.

An `ExpatError` is raised when this method runs against a non-root parser or when *max_factor* falls outside the valid range. The matching `lineno` and `offset` should not be relied on, as they may carry no special meaning.

Note

The maximum amplification factor only comes into play once the threshold adjustable through `SetAllocTrackerActivationThreshold()` has been exceeded.

Added in version 3.14.1.

`xmlparser` objects have the following attributes:

 xmlparser.buffer_size

The size of the buffer in use when `buffer_text` is true. You can set a new buffer size by assigning a new integer value to this attribute. Changing the size flushes the buffer.

 xmlparser.buffer_text

Setting this to true makes the `xmlparser` object buffer the textual content Expat returns, so as to avoid multiple calls to the `CharacterDataHandler()` callback wherever it can. This can boost performance considerably, since Expat ordinarily splits character data into chunks at each line ending. This attribute defaults to false and may be changed whenever you like. Note that while it is false, data lacking newlines may also get chunked.

 xmlparser.buffer_used

When `buffer_text` is enabled, the number of bytes held in the buffer. Those bytes are UTF-8 encoded text. This attribute carries no meaningful interpretation while `buffer_text` is false.

 xmlparser.ordered_attributes

Setting this attribute to a non-zero integer makes the attributes get reported as a list instead of a dictionary. The attributes appear in the order they were found in the document text. Each attribute contributes two list entries: first its name, then its value. (This same format was used by older versions of this module.) This attribute is false by default; it may be changed whenever you like.

 xmlparser.specified_attributes

When set to a non-zero integer, the parser reports only those attributes that were specified in the document instance, and not those derived from attribute declarations. Applications that set this have to be especially careful to draw on whatever extra information the declarations make available, as needed to meet the standards for how XML processors behave. This attribute is false by default; it may be changed whenever you like.

The following attributes hold values about the most recent error an `xmlparser` object met, and will hold correct values only once a call to `Parse()` or `ParseFile()` has raised an `xml.parsers.expat.ExpatError` exception.

 xmlparser.ErrorByteIndex

Byte index at which an error occurred.

 xmlparser.ErrorCode

Numeric code identifying the problem. You can pass this value to the `ErrorString()` function, or compare it against one of the constants defined in the `errors` object.

 xmlparser.ErrorColumnNumber

Column number at which an error occurred.

[Subject index](INDEX.md) · [Previous](expat-parsing-and-entity-protection-threshold.md) · [Continue](expat-error-location-and-element-handlers.md) · [Owning module, declaration or section: xml.parsers.expat](expat-parser-factory-and-exception.md) · [Owning module, declaration or section: XMLParser Objects](expat-parsing-and-entity-protection-threshold.md)
