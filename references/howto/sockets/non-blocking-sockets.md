# Non-blocking Sockets

### Non-blocking Sockets

If the foregoing has sunk in, you've already got a handle on nearly all the mechanics of working with sockets. The calls stay the same, used in much the same fashion. The catch is that done correctly, your app ends up turned nearly inside-out.

Within Python, `socket.setblocking(False)` is how you flip a socket to non-blocking. The C route runs thornier — for starters you'll pick between the BSD flavor `O_NONBLOCK` and its near-twin POSIX flavor `O_NDELAY`, which has nothing to do with `TCP_NODELAY` — but the underlying notion is identical. Do this once the socket is created and before you put it to use. (If you're truly out of your mind, you can even toggle it back and forth.)

The chief mechanical shift is that `send`, `recv`, `connect`, and `accept` are all free to return having accomplished nothing. Naturally you face a few options. You could pore over return values and error codes and steadily lose your sanity. Doubt me? Give it a whirl sometime. Your app balloons, breeds bugs, and devours CPU. So let's bypass the brain-dead routes and do this properly.

Use `select`.

Writing `select` in C is rather involved. Over in Python it's trivial, yet it tracks the C form closely enough that a grasp of `select` in Python carries over with barely any friction to C:

```python
ready_to_read, ready_to_write, in_error = \
               select.select(
                  potential_readers,
                  potential_writers,
                  potential_errs,
                  timeout)

```

You hand `select` three lists: the first holding every socket you might attempt to read, the second every socket you might attempt to write to, and the third (usually empty) those you'd like checked for errors. Bear in mind a single socket can sit in more than one of them. The `select` call blocks, though you're free to attach a timeout — generally the wise move, so set a comfortably long one (a minute, perhaps) absent some solid reason not to.

Back come three lists, carrying the sockets that genuinely are readable, writable, or in error. Every one of these is a subset — possibly empty — of the list you originally supplied.

When a socket lands in the readable output list, you're about as sure as this trade ever lets you be that a `recv` on it will hand back *something*. The writable list works the same way: you'll manage to send *something* — maybe short of everything you'd like, but *something* tops nothing. (In truth, any socket in decent shape reports as writable; that merely signals there's room in the outbound network buffer.)

Holding a “server” socket? Drop it into the potential_readers list. Should it surface in the readable list, your `accept` will, near enough, succeed. Have you spun up a fresh socket to `connect` somewhere? Then place it in the potential_writers list, and its appearance in the writable list gives you fair odds the connection went through.

As it happens, `select` proves useful with blocking sockets too. It's a means of telling whether you're about to block — a socket reads as readable once the buffers hold something. Even so, it offers no help with the riddle of whether the far end has finished or is simply tied up elsewhere.

**Portability alert**: Under Unix, `select` copes with both sockets and files. Don't attempt that on Windows, where `select` deals in sockets alone. Note as well that in C a good many of the fancier socket options behave differently on Windows. Frankly, on Windows I tend to pair threads — which serve me extremely well — with my sockets.

[Subject index](INDEX.md) · [Previous source context](when-sockets-die.md)
