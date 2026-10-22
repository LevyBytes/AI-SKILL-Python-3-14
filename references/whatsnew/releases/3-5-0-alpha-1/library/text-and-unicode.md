# Python 3.5.0 alpha 1 / library / text and unicode

[bpo-20998](https://bugs.python.org/issue?@action=redirect&bpo=20998): A bug in re.fullmatch() with a repeated single character pattern under ignore case was fixed. Matthew Barnett contributed the first patch.

[bpo-1519638](https://bugs.python.org/issue?@action=redirect&bpo=1519638): Groups that go unmatched are now swapped for empty strings within re.sub() and re.subn().

[bpo-19940](https://bugs.python.org/issue?@action=redirect&bpo=19940): Rather than the local timezone, ssl.cert_time_to_seconds() now reads the supplied time string as being in UTC, per RFC 5280.

[bpo-21832](https://bugs.python.org/issue?@action=redirect&bpo=21832): Named tuple inputs are now required to be exact strings.

[bpo-12523](https://bugs.python.org/issue?@action=redirect&bpo=12523): When it is not handed a bytes string, asynchat.async_chat.push() now raises a TypeError

[bpo-21781](https://bugs.python.org/issue?@action=redirect&bpo=21781): Strings exceeding 2 GB are now accepted by ssl.RAND_add().

[bpo-22033](https://bugs.python.org/issue?@action=redirect&bpo=22033): The reprs of most classes written in Python now carry the real class name instead of a hardcoded string.

[bpo-19884](https://bugs.python.org/issue?@action=redirect&bpo=19884): readline: When stdout is not a terminal, the meta modifier key is now disabled to keep the ANSI sequence `"\033[1034h"` out of stdout. Certain terminals (for example TERM=xterm-256color?) rely on this sequence to turn on 8 bit character support.

[bpo-12728](https://bugs.python.org/issue?@action=redirect&bpo=12728): Distinct Unicode characters that share an uppercase form but differ in lowercase are now matched within case-insensitive regular expressions.

[bpo-22406](https://bugs.python.org/issue?@action=redirect&bpo=22406): The uu_codec codec, which had been ported to 3.x incorrectly, was fixed. The work builds on a patch from Martin Panter.

[bpo-21171](https://bugs.python.org/issue?@action=redirect&bpo=21171): Repaired the undocumented filter API belonging to the rot13 codec. Berker Peksag wrote the patch.

[bpo-22226](https://bugs.python.org/issue?@action=redirect&bpo=22226): The leading character of the ?status? key returned by Treeview.heading() is no longer dropped.

[bpo-22818](https://bugs.python.org/issue?@action=redirect&bpo=22818): Splitting against a pattern capable of matching an empty string now triggers a warning. Patterns that match nothing but empty strings are now turned away.

[bpo-20145](https://bugs.python.org/issue?@action=redirect&bpo=20145): Whenever the second argument isn’t a string or a compiled regex, `assertRaisesRegex` and `assertWarnsRegex` now throw a `TypeError`.

[bpo-23112](https://bugs.python.org/issue?@action=redirect&bpo=23112): SimpleHTTPServer was fixed so a redirect adding a trailing slash properly preserves the query string and fragment.

[bpo-21951](https://bugs.python.org/issue?@action=redirect&bpo=21951): A Tkinter crash on AIX when a Tcl command was called with an empty string or tuple argument was fixed.

[bpo-20574](https://bugs.python.org/issue?@action=redirect&bpo=20574): Built an incremental decoder for cp65001 code (Windows code page 65001, Microsoft UTF-8).

[bpo-20283](https://bugs.python.org/issue?@action=redirect&bpo=20283): As documented, RE pattern methods now take the string keyword parameters. The pattern and source keyword parameters stay on as deprecated aliases.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
