# Logging arbitrary objects as messages

### Using arbitrary objects as messages
Up to now, the sections and examples have taken for granted that whatever message you hand off while logging an event is a string. That, though, is not your only option. Any object at all can serve as the message, and the logging machinery will invoke its [`__str__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__str__) method whenever a string form is needed. Indeed, you can skip producing a string form entirely should you wish — the [`SocketHandler`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SocketHandler), for instance, dispatches an event by pickling it and pushing it across the network.

[Subject index](INDEX.md) · [Previous source context](exceptions-raised-during-logging.md) · [Optimization](optimization.md) · [Previous source context](optimization.md) · [Following source context](optimization.md)
