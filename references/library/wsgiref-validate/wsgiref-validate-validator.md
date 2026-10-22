# wsgiref.validate — `wsgiref.validate` — WSGI conformance checker

### `wsgiref.validate` — WSGI conformance checker

While building new WSGI application objects, frameworks, servers, or middleware, validating the conformance of the new code with `wsgiref.validate` can prove handy. This module offers a function that produces WSGI application objects which validate the exchanges between a WSGI server or gateway and a WSGI application object, checking each side for protocol conformance.

Bear in mind that this utility offers no guarantee of full [**PEP 3333**](https://peps.python.org/pep-3333/) compliance; the module reporting no errors does not necessarily imply that none exist. That said, whenever this module does raise an error, it’s all but certain that either the server or the application falls short of 100% compliance.

The `paste.lint` module from Ian Bicking’s “Python Paste” library is the basis for this module.

 wsgiref.validate.validator(*application*)

Wrap *application* and hand back a new WSGI application object. The application that’s returned passes every request through to the original *application*, while verifying that both the *application* and the server calling it adhere to the WSGI specification and to [**RFC 2616**](https://datatracker.ietf.org/doc/html/rfc2616.html).

Whenever nonconformance is spotted, an [`AssertionError`](https://docs.python.org/3.14/library/exceptions.html#AssertionError) is raised; how that error gets handled, though, depends on the server. As an example, `wsgiref.simple_server` and other servers built on `wsgiref.handlers` (those that don’t replace the error-handling methods with something different) will just print a notice that an error happened and dump the traceback to `sys.stderr` or some other error stream.

This wrapper can additionally emit output through the [`warnings`](https://docs.python.org/3.14/library/warnings.html#module-warnings) module to flag behaviors that are dubious yet perhaps not strictly forbidden by [**PEP 3333**](https://peps.python.org/pep-3333/). Such warnings are sent to `sys.stderr` (*not* `wsgi.errors`, unless those two happen to be the same object) unless they’re silenced via Python command-line options or the `warnings` API.

Example usage:

```python
from wsgiref.validate import validator
from wsgiref.simple_server import make_server

# Our callable object which is intentionally not compliant to the
# standard, so the validator is going to break
def simple_app(environ, start_response):
    status = '200 OK'  # HTTP Status
    headers = [('Content-type', 'text/plain')]  # HTTP Headers
    start_response(status, headers)

    # This is going to break because we need to return a list, and
    # the validator is going to inform us
    return b"Hello World"

# This is the application wrapped in a validator
validator_app = validator(simple_app)

with make_server('', 8000, validator_app) as httpd:
    print("Listening on port 8000....")
    httpd.serve_forever()

```

[Subject index](INDEX.md) · [Previous](../wsgiref-simple-server/wsgi-request-handler-contract.md) · [Continue](../wsgiref-handlers/wsgiref-handlers-cgihandler-class.md)
