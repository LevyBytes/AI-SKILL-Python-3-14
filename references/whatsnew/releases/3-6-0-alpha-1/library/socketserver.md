# Python 3.6.0 alpha 1 / library / socketserver

[bpo-26309](https://bugs.python.org/issue?@action=redirect&bpo=26309): Within the "socketserver" module, the request (and its connected socket) is now shut down whenever verify_request() yields false. Aviv Palivoda contributed the patch.

[bpo-23430](https://bugs.python.org/issue?@action=redirect&bpo=23430): The socketserver module was changed so it only catches request-handler exceptions deriving from Exception rather than BaseException. As a result, SystemExit and KeyboardInterrupt no longer reach the handle_error() method and will now halt a single-threaded server.

[bpo-26404](https://bugs.python.org/issue?@action=redirect&bpo=26404): socketserver gained a context manager. Aviv Palivoda contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
