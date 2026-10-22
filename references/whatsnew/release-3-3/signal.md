# What's New In Python 3.3 / signal — signal

### signal

- Fresh functions land in the [`signal`](https://docs.python.org/3.14/library/signal.html#module-signal) module:

  - [`pthread_sigmask()`](https://docs.python.org/3.14/library/signal.html#signal.pthread_sigmask): read or adjust whichever signal mask belongs to the calling thread (Contributed by Jean-Paul Calderone in [bpo-8407](https://bugs.python.org/issue?@action=redirect&bpo=8407));

  - [`pthread_kill()`](https://docs.python.org/3.14/library/signal.html#signal.pthread_kill): send a signal to a thread;

  - [`sigpending()`](https://docs.python.org/3.14/library/signal.html#signal.sigpending): examine pending functions;

  - [`sigwait()`](https://docs.python.org/3.14/library/signal.html#signal.sigwait): wait a signal;

  - [`sigwaitinfo()`](https://docs.python.org/3.14/library/signal.html#signal.sigwaitinfo): wait for a signal, returning detailed information about it;

  - [`sigtimedwait()`](https://docs.python.org/3.14/library/signal.html#signal.sigtimedwait): like [`sigwaitinfo()`](https://docs.python.org/3.14/library/signal.html#signal.sigwaitinfo) but with a timeout.

- Into the wakeup file descriptor the signal handler now writes the signal number as one byte rather than a nul byte. That makes it feasible to await more than a single signal and identify which signals fired.

- [`signal.signal()`](https://docs.python.org/3.14/library/signal.html#signal.signal) along with [`signal.siginterrupt()`](https://docs.python.org/3.14/library/signal.html#signal.siginterrupt) now raise an OSError in place of a RuntimeError: OSError carries an errno attribute.

[Subject index](INDEX.md) · [Previous source section](shutil.md) · [Next source section](smtpd.md) · [Release/subject declaration](summary-release-highlights.md)
