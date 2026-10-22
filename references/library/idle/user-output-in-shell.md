# User output in Shell

### User output in Shell

Whenever a program emits text, the outcome hinges on the output device receiving it. As IDLE runs user code, `sys.stdout` and `sys.stderr` feed into the display region of IDLE's Shell. A portion of its capabilities carries over from the Tk Text widget underneath, while the rest are deliberately added on. Where the distinction counts, Shell is built for development work rather than production runs.

By way of illustration, Shell discards no output at all. Point a program that produces endless output at Shell and it will in time exhaust memory, ending in a memory error. By contrast, certain system text windows retain only the final n lines of output. A Windows console, say, holds a user-configurable 1 to 9999 lines, defaulting to 300.

A Tk Text widget, and therefore IDLE's Shell, renders characters (codepoints) belonging to the BMP (Basic Multilingual Plane) portion of Unicode. Whether a given character shows up as a real glyph or as a replacement box comes down to the operating system and the fonts installed. A tab character pushes the text after it to the next tab stop. (Those land every 8 ‘characters’.) A newline character sends the following text onto a fresh line. Remaining control characters are either skipped or rendered as a space, a box, or something else, according to the operating system and font. (Walking the text cursor across such output with the arrow keys can produce some unexpected spacing.)

```python
>>> s = 'a\tb\a<\x02><\r>\bc\nd'  # Enter 22 chars.
>>> len(s)
14
>>> s  # Display repr(s)
'a\tb\x07<\x02><\r>\x08c\nd'
>>> print(s, end='')  # Display s as is.
# Result varies by OS and font.  Try it.

```

For echoing expression values interactively, the `repr` function does the job. What it hands back is a modified form of the input string where control codes, certain BMP codepoints, and every non-BMP codepoint get swapped out for escape codes. As the example above shows, this lets you pin down the characters in a string no matter how they happen to render.

As a rule, ordinary output and error output stay apart — on their own lines — from code input and from one another, and each is given its own highlight color.

With SyntaxError tracebacks, the usual ‘^’ that points at where the error was spotted gives way to highlighting the text in an error color. When code launched from a file throws other exceptions, you can right-click a traceback line to jump straight to the matching line in an IDLE editor, opening the file if need be.

Shell offers a dedicated feature that collapses output lines into a ‘Squeezed text’ label. This kicks in automatically once output runs past N lines (N defaults to 50). You can adjust N in the PyShell section under the General page of the Settings dialog. Output shorter than that can still be squeezed by right-clicking it. The trick helps with stretches long enough to bog down scrolling.

To restore squeezed output in place, double-click the label. Right-clicking the label instead lets you send it to the clipboard or to a separate view window.

[Subject index](INDEX.md) · [Previous](running-user-code.md) · [Continue](developing-tkinter-applications.md)
