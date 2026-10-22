# Deploying web applications using Gunicorn and uWSGI

### Deploying web applications using Gunicorn and uWSGI

Shipping web applications behind [Gunicorn](https://gunicorn.org/) or [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) (or comparable servers) spins up several worker processes that field client requests. Within setups like these, steer clear of instantiating file-based handlers straight from your web application. Rather, route logs from the web application through a [`SocketHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SocketHandler) to a listener living in its own process. A process-management utility like Supervisor can wire this up - consult Running a logging socket listener in production for additional detail.

[Subject index](INDEX.md) · [Previous source context](using-concurrent-futures-processpoolexecutor.md) · [Following source context](using-file-rotation.md)
