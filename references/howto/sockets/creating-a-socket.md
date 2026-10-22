# Creating a Socket

### Creating a Socket

In broad strokes, the click on the link that landed you on this page set your browser doing roughly this:

```python
# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("www.python.org", 80))

```

Once `connect` finishes, you can put the socket `s` to work sending off a request for the page's text. That very socket then takes in the reply and afterward gets thrown away — yes, thrown away. A client socket ordinarily serves a single exchange, or maybe a handful of them in sequence.

Things run a touch more involved on the web server side. To begin with, the web server stands up a “server socket”:

```python
# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind((socket.gethostname(), 80))
# become a server socket
serversocket.listen(5)

```

A couple of points worth flagging: invoking `socket.gethostname()` is what lets the socket show up to the world at large. Had we instead written `s.bind(('localhost', 80))` or `s.bind(('127.0.0.1', 80))`, we'd still own a “server” socket, just one confined to the local machine. Writing `s.bind(('', 80))` declares that the socket answers on whatever addresses the machine carries.

Another point: ports with small numbers generally belong to the “well known” services (HTTP, SNMP, and so forth). For casual experimentation, grab a comfortably large value with four digits.

Lastly, what you hand `listen` instructs the socket library to hold a backlog of up to 5 pending connect requests (the usual ceiling) before it starts turning away callers. Provided the surrounding code behaves, that headroom is ample.

With a “server” socket now in hand and attending to port 80, we're ready to drop into the web server's mainloop:

```python
while True:
    # accept connections from outside
    (clientsocket, address) = serversocket.accept()
    # now do something with the clientsocket
    # in this case, we'll pretend this is a threaded server
    ct = make_client_thread(clientsocket)
    ct.start()

```

In practice this loop has 3 broad implementations open to it — handing each `clientsocket` off to a thread, forking a fresh process per `clientsocket`, or reworking the whole app around non-blocking sockets so it can multiplex our “server” socket together with every live `clientsocket` via `select`. We'll revisit that. For the moment the crucial takeaway is this: producing “client” sockets is the *entire* job of a “server” socket. No data leaves it. No data arrives at it. All it does is hand back “client” sockets. Every `clientsocket` springs into being because some *separate* “client” socket fired a `connect()` at the host and port we've bound to. The instant that `clientsocket` exists, we loop back around to await further connections. Meanwhile the two “clients” can converse freely over a port handed out on the fly, one that gets reclaimed the moment their exchange wraps up.

[Subject index](INDEX.md) · [Previous source context](history.md) · [Following source context](ipc.md)
