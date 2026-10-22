# Imports, dispatch handler and whole listener process

[Following source context](whole-worker-process-function.md)

### A more elaborate multiprocessing example

The working example below shows logging put to use with multiprocessing by means of configuration files. The configurations stay fairly basic, yet they serve to convey how more involved ones might be built in an actual multiprocessing setting.

In this example the main process launches a listener process plus a handful of worker processes. Three distinct configurations apply, one for the main process, one for the listener, and one for the workers (who all share a single configuration). Visible here are: logging inside the main process; the workers writing their logs into a QueueHandler; and the listener operating a QueueListener alongside a more involved logging configuration, taking events that come in over the queue and forwarding them to the handlers named in the configuration. Keep in mind that these configurations serve purely to illustrate, but you ought to be able to fit this example to your own setting.

Here is the script - with luck the docstrings and comments make clear how it operates:

Open the [complete example modules](../../examples/multiprocess-logging/INDEX.md) for the complete definitions, imports and entrypoint.

[Subject index](INDEX.md) · [Coupled example phase](whole-worker-process-function.md) · [Coupled example phase](main-function-queue-and-initial-worker-configuration.md) · [Coupled example phase](main-function-complete-listener-configuration.md) · [Coupled example phase](main-function-process-startup-joins-and-shutdown.md) · [Whole worker process function](whole-worker-process-function.md) · [Main function queue and initial/worker configuration](main-function-queue-and-initial-worker-configuration.md) · [Main function complete listener configuration](main-function-complete-listener-configuration.md) · [Main function process startup, joins and shutdown](main-function-process-startup-joins-and-shutdown.md) · [Previous source context](custom-log-rotation-namer-and-rotator.md)
