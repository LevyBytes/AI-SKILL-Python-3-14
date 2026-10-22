# Running a logging socket listener in production

### Running a logging socket listener in production

Running a logging listener in production may call for a process-management tool such as [Supervisor](http://supervisord.org/). [Here is a Gist](https://gist.github.com/vsajip/4b227eeec43817465ca835ca66f75e2b) that supplies the minimal set of files needed to run the functionality above under Supervisor. The collection includes these files:

| File | Purpose |
| --- | --- |
| `prepare.sh` | A Bash script that readies the testing environment |
| `supervisor.conf` | The Supervisor configuration file, carrying entries both for the listener and for a multi-process web application |
| `ensure_app.sh` | A Bash script that verifies Supervisor is running under the configuration described above |
| `log_listener.py` | The socket listener program that takes in log events and writes them out to a file |
| `main.py` | A simple web application that logs through a socket wired to the listener |
| `webapp.json` | A JSON configuration file for the web application |
| `client.py` | A Python script to exercise the web application |

For its web application this example relies on [Gunicorn](https://gunicorn.org/), a widely used web application server that spins up several worker processes to service incoming requests. The arrangement demonstrates how those workers can all append to a single shared log file without stepping on each other — every one of them routes through the socket listener.

To exercise these files, carry out the steps below within a POSIX environment:

1.

Grab [the Gist](https://gist.github.com/vsajip/4b227eeec43817465ca835ca66f75e2b) as a ZIP archive by clicking the Download ZIP button.

2.

Extract the files listed above from the archive into a scratch directory.

3.

Inside that scratch directory, execute `bash prepare.sh` to set everything up. Doing so produces a `run` subdirectory that will hold the Supervisor-related and log files, plus a `venv` subdirectory holding a virtual environment in which `bottle`, `gunicorn` and `supervisor` get installed.

4.

Execute `bash ensure_app.sh` to confirm that Supervisor is up and running with the configuration described above.

5.

Execute `venv/bin/python client.py` to drive the web application, which in turn causes records to be written into the log.

6.

Examine the log files within the `run` subdirectory. The newest log lines should appear in files whose names match the `app.log*` pattern. Their ordering won't follow any predictable sequence, because separate worker processes handled them concurrently in a non-deterministic fashion.

7.

To bring down both the listener and the web application, run `venv/bin/supervisorctl -c supervisor.conf shutdown`.

In the rare case that the ports as configured collide with something already present in your test environment, you may have to adjust the configuration files.

By default the configuration relies on a TCP socket bound to port 9020. If you'd rather use a Unix Domain socket in place of a TCP socket, proceed as follows:

1.

Within `listener.json`, introduce a `socket` key set to the path of the domain socket you intend to use. When that key exists, the listener binds to the matching domain socket instead of a TCP socket (and the `port` key is disregarded).

2.

Within `webapp.json`, edit the socket handler configuration dictionary so the `host` value points to the path of the domain socket, and assign the `port` value to `null`.

[Subject index](INDEX.md) · [Previous source context](socket-logging-receiver-launch-output-and-pickle-security.md) · [Following source context](adding-contextual-information-to-your-logging-output.md)
