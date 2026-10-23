# secrets - Security Considerations

## Security Considerations

### Security Considerations

Specific security considerations apply to the modules below:

- [`base64`](https://docs.python.org/3.14/library/base64.html#module-base64): [base64 security considerations](https://docs.python.org/3.14/library/base64.html#base64-security) in [**RFC 4648**](https://datatracker.ietf.org/doc/html/rfc4648.html)

- [`hashlib`](https://docs.python.org/3.14/library/hashlib.html#module-hashlib): [all constructors take a "usedforsecurity" keyword-only argument disabling known insecure and blocked algorithms](https://docs.python.org/3.14/library/hashlib.html#hashlib-usedforsecurity)

- [`http.server`](https://docs.python.org/3.14/library/http.server.html#module-http.server) carries out only basic security checks and is therefore unfit for production deployment. Consult the [security considerations](https://docs.python.org/3.14/library/http.server.html#http-server-security).

- [`logging`](https://docs.python.org/3.14/library/logging.html#module-logging): [Logging configuration uses eval()](https://docs.python.org/3.14/library/logging.config.html#logging-eval-security)

- [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing): [Connection.recv() uses pickle](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-recv-pickle-security)

- [`pickle`](https://docs.python.org/3.14/library/pickle.html#module-pickle): [Restricting globals in pickle](https://docs.python.org/3.14/library/pickle.html#pickle-restrict)

- [`random`](https://docs.python.org/3.14/library/random.html#module-random) shouldn’t be used for security purposes, use [`secrets`](https://docs.python.org/3.14/library/secrets.html#module-secrets) instead

- [`shelve`](https://docs.python.org/3.14/library/shelve.html#module-shelve): [shelve is based on pickle and thus unsuitable for dealing with untrusted sources](https://docs.python.org/3.14/library/shelve.html#shelve-security)

- [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl): [SSL/TLS security considerations](https://docs.python.org/3.14/library/ssl.html#ssl-security)

- [`subprocess`](https://docs.python.org/3.14/library/subprocess.html#module-subprocess): [Subprocess security considerations](https://docs.python.org/3.14/library/subprocess.html#subprocess-security)

- [`tempfile`](https://docs.python.org/3.14/library/tempfile.html#module-tempfile): [mktemp is deprecated due to vulnerability to race conditions](https://docs.python.org/3.14/library/tempfile.html#tempfile-mktemp-deprecated)

- [`xml`](https://docs.python.org/3.14/library/xml.html#module-xml): [XML security](https://docs.python.org/3.14/library/xml.html#xml-security)

- [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile): [maliciously prepared .zip files can cause disk volume exhaustion](https://docs.python.org/3.14/library/zipfile.html#zipfile-resources-limitations)

You can run Python in isolated mode by way of the [`-I`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-I) command line option. Where that is not an option, the [`-P`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-P) option or the [`PYTHONSAFEPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONSAFEPATH) environment variable can stop a potentially unsafe path — for instance the working directory, the directory holding the script, or an empty string — from getting prepended to [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path).

[Subject index](INDEX.md)
