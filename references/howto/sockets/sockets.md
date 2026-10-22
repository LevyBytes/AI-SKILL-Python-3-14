# Sockets

### Sockets

My focus here stays on INET (that is, IPv4) sockets, which make up no less than 99% of those actually deployed. Likewise I'll stick to STREAM (in other words, TCP) sockets — barring the case where you genuinely know your way around (and if so, you've outgrown this HOWTO!), a STREAM socket delivers nicer behavior and stronger performance than the alternatives. My aim is to demystify what a socket really is and to offer a few pointers on handling both blocking and non-blocking varieties. Blocking sockets come first, though, since you have to understand them before tackling the non-blocking kind.

A chunk of the confusion here comes down to the word “socket” carrying several faintly distinct meanings according to context. So let's open by separating two senses: a “client” socket, which is one end of a dialogue, from a “server” socket, which behaves more along the lines of a switchboard operator. A client program — your browser, to pick the obvious case — deals only in “client” sockets, whereas the web server on the far side juggles both “server” sockets and “client” sockets.

[Subject index](INDEX.md) · [Previous source context](socket-programming-howto.md) · [Following source context](history.md)
