# Socket logging receiver launch, output and pickle security

Start the server first, then launch the client. The client side prints nothing to the console; over on the server side, output resembling the following should appear:

```none
About to start TCP server...
   59 root            INFO     Jackdaws love my big sphinx of quartz.
   59 myapp.area1     DEBUG    Quick zephyrs blow, vexing daft Jim.
   69 myapp.area1     INFO     How quickly daft jumping zebras vex.
   69 myapp.area2     WARNING  Jail zesty vixen who grabbed pay from quack.
   69 myapp.area2     ERROR    The five boxing wizards jump quickly.

```

Be aware that pickle carries some security concerns under certain circumstances. Should those apply to your case, a different serialization scheme can be substituted by overriding the [`makePickle()`](https://docs.python.org/3.14/library/logging.handlers.html#logging.handlers.SocketHandler.makePickle) method and supplying your own logic there, along with reworking the script above to rely on that alternative serialization.

[Subject index](INDEX.md) · [Complete socket logging receiver implementation](complete-socket-logging-receiver-implementation.md) · [Previous source context](complete-socket-logging-receiver-implementation.md) · [Following source context](running-a-logging-socket-listener-in-production.md)
