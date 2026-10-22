# email.generator: `email.generator.DecodedGenerator`

*class *email.generator.DecodedGenerator(*outfp*, *mangle_from_=None*, *maxheaderlen=None*, *fmt=None*, ***, *policy=None*)

Behaves as `Generator` does, with one difference: for each subpart of the message given to `Generator.flatten()`, a subpart whose main type is *text* has its decoded payload printed, whereas a subpart whose main type is not *text* is handled by populating the string *fmt* with details drawn from the part and printing that populated string in its place.

Populating *fmt* is done by running `fmt % part_info`, in which `part_info` is a dictionary built from these keys and their values:

- `type` – The complete MIME type belonging to the non-*text* part

- `maintype` – The principal MIME type carried by the non-*text* part

- `subtype` – The MIME subtype held by the non-*text* part

- `filename` – The file name attached to the non-*text* part

- `description` – Whatever description goes with the non-*text* part

- `encoding` – The content transfer encoding used on the non-*text* part

Leave *fmt* at `None` and this default *fmt* takes over:

>

“[Non-text (%(type)s) part of message omitted, filename %(filename)s]”

The optional *_mangle_from_* and *maxheaderlen* carry the same meaning they do for the `Generator` base class.

Footnotes

[Subject index](INDEX.md) · [Previous](text-generator-class-and-output.md) · [Owning module, declaration or section: email.generator](email-generator-bytesgenerator-class.md)
