# os: `os.spawnl()`, `os.spawnle()`, `os.spawnlp()`, `os.spawnlpe()`, `os.spawnv()`, `os.spawnve()`, `os.spawnvp()`, `os.spawnvpe()`, `os.P_NOWAIT`, `os.P_NOWAITO`, `os.P_WAIT`, `os.P_DETACH`, `os.P_OVERLAY`

os.spawnl(*mode*, *path*, *...*)

 os.spawnle(*mode*, *path*, *...*, *env*)

 os.spawnlp(*mode*, *file*, *...*)

 os.spawnlpe(*mode*, *file*, *...*, *env*)

 os.spawnv(*mode*, *path*, *args*)

 os.spawnve(*mode*, *path*, *args*, *env*)

 os.spawnvp(*mode*, *file*, *args*)

 os.spawnvpe(*mode*, *file*, *args*, *env*)

Run the program *path* inside a new process.

(Keep in mind that the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module offers more capable facilities for spawning new processes and collecting their results; leaning on that module beats using these functions. Look especially at the [Replacing Older Functions with the subprocess Module](https://docs.python.org/3.14/library/subprocess.html#subprocess-replacements) section.)

When *mode* is `P_NOWAIT`, this function gives back the process id of the new process; when *mode* is `P_WAIT`, it gives back the process's exit code if it exits normally, otherwise `-signal`, where *signal* is the signal that killed the process. Under Windows, the process id is really the process handle, so it works with the `waitpid()` function.

Note that on VxWorks this function does not return `-signal` when the new process is killed. It raises an OSError exception instead.

The "l" and "v" forms of the `spawn*` functions differ in the way command-line arguments get passed. The "l" forms are arguably simplest when the number of parameters is fixed at the time the code is written; the individual parameters just turn into extra parameters of the `spawnl*()` functions. The "v" forms suit a variable parameter count, since the arguments arrive within a list or tuple as the *args* parameter. Either way, the arguments handed to the child process must begin with the name of the command being run.

Those forms carrying a second "p" toward the end (`spawnlp()`, `spawnlpe()`, `spawnvp()`, and `spawnvpe()`) consult the `PATH` environment variable to find the program *file*. Where the environment is being swapped out (through one of the `spawn*e` forms, covered in the next paragraph), the new environment supplies the `PATH` variable. The remaining forms, `spawnl()`, `spawnle()`, `spawnv()`, and `spawnve()`, will not consult the `PATH` variable to find the executable; *path* must hold a suitable absolute or relative path.

With `spawnle()`, `spawnlpe()`, `spawnve()`, and `spawnvpe()` (notice that each of these ends in "e"), the *env* parameter has to be a mapping that establishes the environment variables for the new process (they take the place of the current process' environment); the functions `spawnl()`, `spawnlp()`, `spawnv()`, and `spawnvp()` instead make the new process inherit the current process's environment. Bear in mind that keys and values inside the *env* dictionary have to be strings; invalid keys or values make the function fail, returning `127`.

By way of example, these calls to `spawnlp()` and `spawnvpe()` come out equivalent:

```python
import os
os.spawnlp(os.P_WAIT, 'cp', 'cp', 'index.html', '/dev/null')

L = ['cp', 'index.html', '/dev/null']
os.spawnvpe(os.P_WAIT, 'cp', L, os.environ)

```

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `os.spawn` with arguments `mode`, `path`, `args`, `env`.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows, not WASI, not Android, not iOS.

Windows lacks `spawnlp()`, `spawnlpe()`, `spawnvp()` and `spawnvpe()`. On Windows, `spawnle()` and `spawnve()` lack thread safety; our advice is to reach for the [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module in their place.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

[Soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) since version 3.14: The [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess) module is recommended instead.

 os.P_NOWAIT

 os.P_NOWAITO

Allowable values for the *mode* parameter of the `spawn*` family of functions. Given either of these values, the `spawn*` functions return the moment the new process has been created, handing back the process id.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

 os.P_WAIT

An allowable value for the *mode* parameter of the `spawn*` family of functions. Supplied as *mode*, the `spawn*` functions hold off returning until the new process has run to completion, then return the process's exit code when the run succeeds, or `-signal` when a signal kills the process.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix, Windows.

 os.P_DETACH

 os.P_OVERLAY

Allowable values for the *mode* parameter of the `spawn*` family of functions. These travel less well than the ones above. `P_DETACH` resembles `P_NOWAIT`, except the new process is detached from the calling process's console. Choosing `P_OVERLAY` replaces the current process; the `spawn*` function then will not return.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows.

[Subject index](INDEX.md) · [Previous](os-posix-spawnp-to-os-register-at-fork.md) · [Continue](os-startfile-to-os-times.md) · [Owning module, declaration or section: os](os-error-to-os-name.md) · [Owning module, declaration or section: Process Management](os-abort-to-os-ex-ok.md)
