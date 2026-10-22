# Subprocess Transports

### Subprocess Transports

 SubprocessTransport.get_pid()

Return the subprocess process id as an integer.

 SubprocessTransport.get_pipe_transport(*fd*)

Hand back the transport for the communication pipe tied to the integer file descriptor *fd*:

- `0`: writable streaming transport for standard input (*stdin*); becomes [`None`](https://docs.python.org/3.14/library/constants.html#None) when the subprocess wasn't started using `stdin=PIPE`

- `1`: readable streaming transport for standard output (*stdout*); becomes [`None`](https://docs.python.org/3.14/library/constants.html#None) when the subprocess wasn't started using `stdout=PIPE`

- `2`: readable streaming transport for standard error (*stderr*); becomes [`None`](https://docs.python.org/3.14/library/constants.html#None) when the subprocess wasn't started using `stderr=PIPE`

- other *fd*: [`None`](https://docs.python.org/3.14/library/constants.html#None)

 SubprocessTransport.get_returncode()

Hand back the subprocess return code as an integer, or [`None`](https://docs.python.org/3.14/library/constants.html#None) when it hasn't returned yet, paralleling the [`subprocess.Popen.returncode`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.returncode) attribute.

 SubprocessTransport.kill()

Kill the subprocess.

Under POSIX, the function delivers SIGKILL to the subprocess. Under Windows, this method serves as an alias for `terminate()`.

See also [`subprocess.Popen.kill()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.kill).

 SubprocessTransport.send_signal(*signal*)

Deliver the *signal* number to the subprocess, mirroring [`subprocess.Popen.send_signal()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.send_signal).

 SubprocessTransport.terminate()

Stop the subprocess.

Under POSIX, this method delivers [`SIGTERM`](https://docs.python.org/3.14/library/signal.html#signal.SIGTERM) to the subprocess. Under Windows, the Windows API function `TerminateProcess()` runs to stop the subprocess.

See also [`subprocess.Popen.terminate()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen.terminate).

 SubprocessTransport.close()

Kill the subprocess by calling the `kill()` method.

Should the subprocess not have returned so far, and shut the *stdin*, *stdout*, and *stderr* pipe transports.

[Subject index](INDEX.md) · [Previous](datagramtransport-sendto-to-datagramtransport-abort.md) · [Continue](protocols.md)
