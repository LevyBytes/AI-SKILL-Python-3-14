# msvcrt — Console I/O

### Console I/O

 msvcrt.kbhit()

Hands back a value other than zero whenever a keystroke is queued up for reading; when none is pending, it hands back 0.

 msvcrt.getch()

Take one keystroke and hand back its character as a byte string, with nothing shown on the console. The call waits when no keystroke is ready yet, though it never holds out for Enter. Pressing a special function key makes it hand back `'\000'` or `'\xe0'`, after which a follow-up call hands back the keycode. There is no way for this routine to pick up a Control-C keystroke.

 msvcrt.getwch()

The wide-character counterpart to `getch()`; it hands back a Unicode value.

 msvcrt.getche()

Works like `getch()`, except that a keystroke standing for a printable character does get shown.

 msvcrt.getwche()

The wide-character form of `getche()`; its result is a Unicode value.

 msvcrt.putch(*char*)

Send the byte string *char* straight to the console, bypassing any buffering.

 msvcrt.putwch(*unicode_char*)

The wide-character counterpart to `putch()`; it takes a Unicode value.

 msvcrt.ungetch(*char*)

Make the byte string *char* go back onto the console buffer so that it becomes whatever `getch()` or `getche()` reads next.

 msvcrt.ungetwch(*unicode_char*)

The wide-character form of `ungetch()`; it takes a Unicode value.

[Subject index](INDEX.md) · [Previous](msvcrt-locking-to-msvcrt-get-osfhandle.md) · [Continue](msvcrt-heapmin-to-msvcrt-libraries-assembly-name-prefix.md) · [Owning module, declaration or section: msvcrt](msvcrt-useful-routines-from-the-ms-vc-runtime.md)
