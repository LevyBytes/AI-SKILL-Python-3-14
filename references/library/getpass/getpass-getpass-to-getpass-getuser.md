# getpass`getpass` - Portable password input

## getpass - Portable password input

### `getpass` - Portable password input

**Source code:** [Lib/getpass.py](https://github.com/python/cpython/tree/3.14/Lib/getpass.py)

---

[Availability](https://docs.python.org/3.14/library/intro.html#availability): not WASI.

On WebAssembly this module either fails to function or is absent. Refer to [WebAssembly platforms](https://docs.python.org/3.14/library/intro.html#wasm-availability) for further detail.

The `getpass` module provides two functions:

 getpass.getpass(*prompt='Password: '*, *stream=None*, ***, *echo_char=None*)

Ask the user for a password while suppressing the echo. The string *prompt*, defaulting to `'Password: '`, is what the user sees. On Unix, the prompt goes to the file-like object *stream*, using the replace error handler should that be necessary. *stream* defaults to the controlling terminal (`/dev/tty`), or to `sys.stderr` when that terminal can't be reached (Windows ignores this argument).

How the user's input appears as they type is governed by the *echo_char* argument. When *echo_char* is `None` (the default), the input stays hidden. Otherwise *echo_char* has to be one printable ASCII character, and every typed character is shown as that character instead. As an illustration, `echo_char='*'` shows asterisks in place of the real input.

When echo-free input can't be had, getpass() falls back on writing a warning message to *stream*, reading from `sys.stdin`, and raising a `GetPassWarning`.

Note

Should you invoke getpass from inside IDLE, the entry might happen in whatever terminal you started IDLE from instead of the idle window itself.

Note

On Unix systems, with *echo_char* set, the terminal gets configured to run in *[noncanonical mode](https://manpages.debian.org/termios(3)#Canonical_and_noncanonical_mode)*. Among other things, this means line editing shortcuts like Ctrl+U stop working and could feed unexpected characters into the input.

Changed in version 3.14: Added the *echo_char* parameter for keyboard feedback.

 *exception *getpass.GetPassWarning

A [`UserWarning`](https://docs.python.org/3.14/library/exceptions.html#UserWarning) subclass issued when password input may be echoed.

 getpass.getuser()

Return the “login name” of the user.

This function looks at the environment variables `LOGNAME`, `USER`, `LNAME`, and `USERNAME`, in that sequence, and gives back the value of the first one set to a non-empty string. Should none be set, the login name is fetched from the password database on systems providing the [`pwd`](https://docs.python.org/3.14/library/pwd.html#module-pwd) module; otherwise an [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) is raised.

Generally speaking, you should favor this function over [`os.getlogin()`](https://docs.python.org/3.14/library/os.html#os.getlogin).

Changed in version 3.13: Previously, various exceptions beyond just [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) were raised.

[Subject index](INDEX.md)
