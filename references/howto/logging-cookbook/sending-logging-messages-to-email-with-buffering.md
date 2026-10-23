# Sending logging messages to email, with buffering

### Sending logging messages to email, with buffering

To demonstrate emailing log messages such that each email carries a fixed number of them, you can derive a subclass from [`BufferingHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.BufferingHandler). The example below — which you can tailor to your own requirements — bundles a small test harness so the script accepts command line arguments covering the usual things SMTP delivery requires. (Invoke the downloaded script with `-h` to list the mandatory and optional arguments.)

The complete program is in the [upstream source](https://docs.python.org/3.14/howto/logging-cookbook.html#sending-logging-messages-to-email-with-buffering).

Assuming your SMTP server is configured properly, executing this script should result in eleven emails arriving at the address you name. Each of the first ten will carry ten log messages, while the final one will carry two. That totals the 102 messages the script declares.

[Subject index](INDEX.md) · [Previous source context](conditional-buffer-flush-output-and-decorator-syntax.md) · [Following source context](formatting-times-using-utc-via-configuration.md)
