# winsound: `winsound.Beep()`, `winsound.PlaySound()`, `winsound.MessageBeep()`, `winsound.SND_FILENAME`, `winsound.SND_ALIAS`, `winsound.SND_LOOP`, `winsound.SND_MEMORY`, `winsound.SND_PURGE`, `winsound.SND_ASYNC`, `winsound.SND_NODEFAULT`

# Winsound

### `winsound` — Sound-playing interface for Windows

---

Through the `winsound` module you reach the elementary sound-playing facilities that Windows platforms expose. A handful of functions and constants come bundled with it.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

 winsound.Beep(*frequency*, *duration*)

Sound the PC's speaker. Pitch, expressed in hertz, is dictated by the *frequency* parameter, which has to fall within 37 through 32,767. How long the tone holds, measured in milliseconds, is set by the *duration* parameter. Where the platform cannot drive the speaker, a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) results.

 winsound.PlaySound(*sound*, *flags*)

Invoke the Platform API's underlying `PlaySound()` function. What you pass as the *sound* parameter can be a filename, a system sound alias, audio bytes given as a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object), or else `None`. How that value is read hinges on *flags*, which may be several of the constants documented further down OR-ed together bitwise. Supplying `None` for the *sound* parameter halts whatever waveform sound is presently sounding. Should the platform report a problem, a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) results.

 winsound.MessageBeep(*type=MB_OK*)

Invoke the Platform API's underlying `MessageBeep()` function. It emits whatever sound the registry has on file. Which one gets played is chosen by the *type* argument, whose allowed settings are `-1`, `MB_ICONASTERISK`, `MB_ICONEXCLAMATION`, `MB_ICONHAND`, `MB_ICONQUESTION`, and `MB_OK`, each covered below. Passing `-1` gives you a “simple beep,” serving as the last resort whenever no other sound can sound. Should the platform report a problem, a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) results.

 winsound.SND_FILENAME

Here the *sound* parameter names a WAV file. Steer clear of pairing it with `SND_ALIAS`.

 winsound.SND_ALIAS

Here the *sound* parameter holds a sound association name drawn from the registry. Where the registry lacks that name, the system default sound plays — unless `SND_NODEFAULT` has also been given. With no default sound registered, a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is raised. Steer clear of pairing it with `SND_FILENAME`.

Every Win32 system handles at minimum the entries listed here; the majority of systems handle a good many more:

| `PlaySound()` *name* | Corresponding Control Panel Sound name |
| --- | --- |
| `'SystemAsterisk'` | Asterisk |
| `'SystemExclamation'` | Exclamation |
| `'SystemExit'` | Exit Windows |
| `'SystemHand'` | Critical Stop |
| `'SystemQuestion'` | Question |

For example:

```python
import winsound
# Play Windows exit sound.
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

# Probably play Windows default sound, if any is registered (because
# "*" probably isn't the registered name of any sound).
winsound.PlaySound("*", winsound.SND_ALIAS)

```

 winsound.SND_LOOP

Keep replaying the sound on a loop. To dodge blocking, the `SND_ASYNC` flag has to accompany it. It will not work alongside `SND_MEMORY`.

 winsound.SND_MEMORY

For `PlaySound()`, the *sound* parameter here is an in-memory image of a WAV file, supplied as a [bytes-like object](https://docs.python.org/3.14/glossary.html#term-bytes-like-object).

Note

Playing asynchronously from an in-memory image is not something this module can do, so combining this flag with `SND_ASYNC` will raise [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

 winsound.SND_PURGE

Halt every instance of the given sound that is playing.

Note

Current Windows platforms offer no support for this flag.

 winsound.SND_ASYNC

Hand control back right away, letting sounds run asynchronously.

 winsound.SND_NODEFAULT

When the named sound is nowhere to be found, refrain from playing the system default sound.

[Subject index](INDEX.md) · [Continue](winsound-snd-nostop-to-winsound-mb-iconwarning.md)
