# Disconnecting

### Disconnecting

By the book, you ought to call `shutdown` on a socket ahead of `close`-ing it. The `shutdown` serves as a notice to the socket sitting at the far end. Depending on which argument goes in, the message it carries is either “Done sending on my end, though I'll keep on listening” or “Listening's over for me, good riddance!”. Most socket libraries, though, have grown so accustomed to programmers skipping this courtesy that as a rule a `close` amounts to `shutdown(); close()`. Hence in the majority of cases there's no call for a `shutdown` written out explicitly.

A productive place to deploy `shutdown` is within an HTTP-style exchange. The client fires its request and follows up with a `shutdown(1)`, which tells the server “No more will arrive from this client, yet it remains able to take in data.” The server picks up on the “EOF” through a receive of 0 bytes and may take it that the request is whole. The server then dispatches a reply, and if that `send` goes through cleanly, sure enough the client was indeed still listening.

Python pushes the automatic shutdown one notch further, declaring that a garbage-collected socket will perform a `close` of its own accord should one be warranted. Leaning on that, however, is a thoroughly bad habit. Let your socket vanish minus a `close` and the far-end socket might hang forever, supposing you've merely turned sluggish. *Please* `close` your sockets when you’re done.

[Subject index](INDEX.md) · [Previous source context](binary-data.md) · [Following source context](when-sockets-die.md)
