# subprocess — Security Considerations

### Security Considerations

In contrast to certain other popen functions, this library never silently decides to invoke a system shell. As a result, any character at all, shell metacharacters included, can be handed to child processes without danger. Should the shell be invoked deliberately through `shell=True`, the application takes on the duty of quoting every whitespace and metacharacter correctly so as to prevent [shell injection](https://en.wikipedia.org/wiki/Shell_injection#Shell_injection) vulnerabilities. On [some platforms](https://docs.python.org/3.14/library/shlex.html#shlex-quote-warning), [`shlex.quote()`](https://docs.python.org/3.14/library/shlex.html#shlex.quote) can handle this escaping.

Under Windows, the operating system may run batch files (`*.bat` or `*.cmd`) inside a system shell no matter which arguments get passed to this library. The upshot is that arguments may be interpreted under shell rules while lacking any escaping that Python would add. When you deliberately run a batch file whose arguments come from untrusted sources, think about passing `shell=True` so that Python escapes special characters. Further discussion appears at [gh-114539](https://github.com/python/cpython/issues/114539).

[Subject index](INDEX.md) · [Previous](exceptions.md) · [Continue](popen-poll-to-popen-stdin.md) · [Owning module, declaration or section: subprocess](subprocess-subprocess-management.md)
