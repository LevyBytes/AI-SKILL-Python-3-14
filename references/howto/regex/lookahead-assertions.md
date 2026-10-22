# Lookahead assertions

### Lookahead assertions

The lookahead assertion is yet another zero-width assertion. Lookahead assertions come in both a positive and a negative flavour, and they look like this:

`(?=...)`

Positive lookahead assertion. It succeeds when the enclosed regular expression, shown here as `...`, matches successfully at the present spot, and otherwise it fails. However, after the enclosed expression has been attempted, the matching engine moves forward not at all; the remainder of the pattern is attempted from the very spot where the assertion began.

`(?!...)`

Negative lookahead assertion. The reverse of the positive assertion, it succeeds when the enclosed expression *doesn’t* match at the present position in the string.

To put this in concrete terms, let's examine a situation where a lookahead helps. Picture a basic pattern meant to match a filename and break it into a base name and an extension, with a `.` dividing them. As an example, within `news.rc`, `news` serves as the base name while `rc` is the filename's extension.

The pattern that matches this is fairly straightforward:

`.*[.].*$`

Note that the `.` calls for special handling because it is a metacharacter, hence its placement inside a character class so that only that one character matches. Note as well the closing `$`; it's there to force the whole rest of the string into the extension. This regular expression matches `foo.bar` and `autoexec.bat` and `sendmail.cf` and `printers.conf`.

Now let's make the problem a touch harder; suppose you want to match filenames whose extension isn't `bat`. A couple of flawed tries:

`.*[.][^b].*$`

That first try above attempts to rule out `bat` by insisting the extension's opening character not be a `b`. It is mistaken, since the pattern then also fails to match `foo.bar`.

`.*[.]([^b]..|.[^a].|..[^t])$`

Things turn uglier as you try to mend the first solution by demanding that one of these hold: the extension's first character isn't `b`; the second isn't `a`; or the third isn't `t`. This takes `foo.bar` and turns away `autoexec.bat`, yet it insists on a three-letter extension and won't take a filename whose extension is two letters, such as `sendmail.cf`. We'll make the pattern more complicated again as we try to set it right.

`.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$`

For the third try, the second and third letters are each turned optional so that extensions under three characters, like `sendmail.cf`, can match.

By now the pattern has grown truly tangled, which leaves it tough to read and grasp. Worse still, if the requirement shifts and you decide to bar both `bat` and `exe` as extensions, the pattern would become even more tangled and bewildering.

A negative lookahead slices straight through the whole muddle:

`.*[.](?!bat$)[^.]*$`

Here is what the negative lookahead conveys: when the expression `bat` fails to match at this spot, proceed with the rest of the pattern; should `bat$` match, the full pattern fails. That closing `$` is needed so that a case such as `sample.batch`, whose extension merely opens with `bat`, is still permitted. The `[^.]*` guarantees the pattern still works once the filename holds several dots.

Barring one more filename extension is straightforward now; just tack it on as another alternative within the assertion. The pattern below rules out filenames closing in either `bat` or `exe`:

`.*[.](?!bat$|exe$)[^.]*$`

[Subject index](INDEX.md) · [Previous source context](non-capturing-and-named-groups.md) · [Following source context](modifying-strings.md)
