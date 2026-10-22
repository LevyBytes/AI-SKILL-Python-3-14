# shlex: Shell-token input, pushback and source configuration

### shlex Objects

These methods are provided by a `shlex` instance:

`shlex.get_token()`

Hand back a token. Where tokens were already pushed on via `push_token()`, take one off the stack; otherwise pull one from the input stream. Should reading hit an immediate end-of-file, the value `eof` is given back (which is the empty string (`''`) outside POSIX mode and `None` within it).

`shlex.push_token(*str*)`

Place the argument back onto the token stack.

`shlex.read_token()`

Pull a raw token. Skip over the pushback stack and leave source requests uninterpreted. (You won't usually reach for this entry point; it appears here merely for completeness.)

`shlex.sourcehook(*filename*)`

Whenever `shlex` spots a source request (described under `source` further down), this method receives the next token as its argument and is meant to hand back a tuple made up of a filename together with an opened file-like object.

By default this method begins by stripping any surrounding quotes from the argument. The result is left untouched if it is an absolute pathname, or if no earlier source request was active, or if the prior source happened to be a stream (`sys.stdin`, say). Failing that, when the result is a relative pathname, the directory portion of the filename sitting directly before it on the source inclusion stack gets prepended (mirroring how the C preprocessor deals with `#include "file.h"`).

Whatever comes out of those manipulations is taken as a filename and handed back as the tuple's first element, with [`open()`](https://docs.python.org/3.14/library/functions.html#open) invoked on it to produce the second. (Mind that this is the opposite ordering of the arguments at instance initialization!)

The point of exposing this hook is to let you build directory search paths, tack on file extensions, and pull off other namespace tricks. No matching 'close' hook exists, yet a shlex instance does invoke the [`close()`](https://docs.python.org/3.14/library/io.html#io.IOBase.close) method on the sourced input stream once it hits EOF.

When you want finer control over source stacking, reach for the `push_source()` and `pop_source()` methods.

`shlex.push_source(*newstream*, *newfile=None*)`

Place an input source stream on top of the input stack. Supplying the filename argument makes it available afterward for error messages. The `sourcehook()` method relies on this very same method internally.

`shlex.pop_source()`

Take the most recently pushed input source back off the input stack. This is exactly the method invoked internally once the lexer reaches EOF on a stacked input stream.

`shlex.error_leader(*infile=None*, *lineno=None*)`

This method builds the leading part of an error message styled after a Unix C compiler's error label; that format is `'"%s", line %d: '`, with `%s` swapped for the name of the active source file and `%d` for the present input line number (you may override both via the optional arguments).

The point of this helper is to nudge `shlex` users toward emitting error messages in the standard, machine-parseable layout that Emacs and other Unix tools recognize.

A `shlex` subclass's instances carry several public instance variables that either steer lexical analysis or serve debugging needs:

`shlex.commenters`

Holds the characters treated as comment starters. Everything from a comment starter through to the line's end is discarded. Contains only `'#'` by default.

`shlex.wordchars`

Holds the characters that build up into multi-character tokens. The default set covers every ASCII alphanumeric plus underscore. Under POSIX mode the Latin-1 accented characters join in too. When `punctuation_chars` is non-empty, this attribute also picks up the characters `~-./*?=` (which turn up in filename patterns and command-line parameters), and any character present in `punctuation_chars` gets pulled out of `wordchars` should it be there. Setting `whitespace_split` to `True` renders all of this moot.

`shlex.whitespace`

The characters regarded as whitespace and passed over. Whitespace marks the edges of tokens. The default covers space, tab, linefeed, and carriage-return.

`shlex.escape`

The characters regarded as escape. These come into play only under POSIX mode, and by default the set is just `'\'`.

`shlex.quotes`

The characters regarded as string quotes. A token keeps growing until the matching quote turns up again (so the various quote kinds shield one another, just as in the shell). The default takes in ASCII single and double quotes.

`shlex.escapedquotes`

Those characters within `quotes` that will act on the escape characters laid out in `escape`. Active only under POSIX mode, with a default of just `'"'`.

`shlex.whitespace_split`

Set to `True`, tokens get divided solely at whitespace. That proves handy, for instance, when parsing command lines through `shlex` to obtain tokens much like shell arguments. Combined with `punctuation_chars`, tokens are divided on whitespace on top of those characters.

Changed in version 3.8: Compatibility between the `punctuation_chars` attribute and the `whitespace_split` attribute was introduced.

`shlex.infile`

The name of the input file currently in use, as first established when the class was instantiated or stacked by subsequent source requests. Inspecting it can help while assembling error messages.

`shlex.instream`

The input stream out of which this `shlex` instance reads its characters.

[Subject index](INDEX.md) · [Previous](shlex-shlex-class.md) · [Continue](shlex-source-to-shlex-punctuation-chars.md) · [Owning module, declaration or section: shlex](shlex-split-to-shlex-join.md)
