# Using a Socket

### Using a Socket

Notice up front that the browser's “client” socket and the server's “client” socket are one and the same creature. Put differently, what you have is a “peer to peer” conversation. Stated yet another way, *the etiquette governing a conversation is yours to define as the designer*. As a rule the `connect`ing socket opens the dialogue, firing off a request or perhaps a signon — yet that's a choice you make in design, never a law the sockets impose.

Two families of verbs are available to you for talking back and forth. One option is `send` and `recv`; the other is to recast your client socket as a file-like object and reach for `read` and `write`. That second style mirrors how Java exposes its sockets. I'll skip over it beyond one caution: you have to call `flush` on these sockets. They are buffered “files”, and the classic slip-up is to `write` something and immediately `read` expecting an answer. Leave out the `flush` and you might hang on that reply indefinitely, the request still sitting in your output buffer.

Here we arrive at the chief obstacle with sockets — `send` and `recv` act upon the network buffers. They won't reliably move every byte you give them (or hope to pull from them), since wrangling those network buffers is their whole preoccupation. As a rule they come back once the relevant network buffers are full (`send`) or drained (`recv`), at which point they report the byte count they managed. Keeping at it — calling them over and over until your message is entirely processed — falls to *you*.

A `recv` that hands back 0 bytes signals that the far end has shut the connection or is partway through doing so. No further data will ever reach you over that connection. Sending data out may still work, however; more on that further down.

A protocol along the lines of HTTP rides a socket for just one transfer. The client dispatches a request and then reads back a reply. Done. The socket gets discarded. Because of that, a client can spot where the reply ends simply by getting 0 bytes.

Yet should you mean to keep the same socket around for more transfers, grasp that *there is no* EOT *on a socket.* Once more: a socket `send` or `recv` coming back after moving 0 bytes means the connection has snapped. While the link remains intact, a `recv` can leave you waiting indefinitely, because the socket gives *no* sign that nothing more awaits reading right now. Mull that over and a bedrock fact about sockets surfaces: every message has to *carry a fixed size* (yuck), *come with delimiters* (shrug), *announce its own length up front* (much better), *or finish by tearing the connection down*. Which route you take is wholly up to you, though some are more right than others.

Granting that ending the connection isn't your goal, the plainest answer is a fixed-length message:

```python
class MySocket:
    """demonstration class only
      - coded for clarity, not efficiency
    """

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)

```

The transmitting code shown works for nearly every messaging approach — in Python you push strings out, and `len()` gives you the size (holding true even when `\0` characters lurk inside). The trickier part is mostly the receiving side. (In C the gap is small, save that `strlen` is off the table once `\0`s are embedded in the message.)

Your simplest upgrade is to let the message's opening character flag its type, with the type then dictating the length. That leaves you running two `recv`s — the first fetching at minimum that leading character so the length can be looked up, the second looping to gather what remains. Choosing the delimited path instead, you'll read in some arbitrary chunk size (4096 or 8192 tends to line up nicely with network buffer sizes) and comb through the arrivals for a delimiter.

Watch out for one wrinkle: when your conversational protocol permits messages stacked one right after another (with no reply between) and you feed `recv` an arbitrary chunk size, you can wind up reading into the head of the next message. That fragment has to be set aside and kept until you need it.

Sticking the length on the front of the message — say as 5 numeric characters — grows hairier still, since (improbable as it sounds) those 5 characters may not all turn up in one `recv`. While tinkering you'll skate by, but under heavy network load your code shatters fast unless you run two `recv` loops, one to nail down the length and another to pull in the message's data portion. Nasty. That's also the moment you'll find that `send` can't always flush everything in a single pass. And even after reading all this, the bug will catch you in the end!

For the sake of brevity, plus a bit of character-building (and guarding my own edge), I'll hand these refinements over to the reader as an exercise. On to wrapping things up.

[Subject index](INDEX.md) · [Previous source context](ipc.md) · [Following source context](binary-data.md)
