# Python 3.9.0 alpha 2 / library / overview

Formerly the code raised a `KeyError` under both the Python and C implementation. The trigger was the supplied index of an invalid input not being present in the memo structure, which is where the pickle keeps a record of the objects it has encountered. Malformed input would prompt either a `BINGET` or `LONG_BINGET` load against the memo, and because the computed index was bogus, a `KeyError` resulted. Claudiu Popa authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
