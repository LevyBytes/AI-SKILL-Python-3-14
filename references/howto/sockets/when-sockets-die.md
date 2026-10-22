# When Sockets Die

### When Sockets Die

Quite possibly the nastiest aspect of blocking sockets is what unfolds when the opposite end crashes out abruptly, skipping any `close`. Odds are your socket hangs. TCP being a reliable protocol, it holds on for an awfully long stretch before it abandons a connection. Should you be running threads, that whole thread is for all practical purposes dead, and little remedy exists. So long as you steer clear of foolishness — clutching a lock through a blocking read, for one — the thread isn't actually burning many resources. Resist *any* urge to kill the thread: part of what makes threads leaner than processes is that they dodge the cost of automatically reclaiming resources. To say it plainly, succeed in killing the thread and you'll likely wreck your entire process.

[Subject index](INDEX.md) · [Previous source context](disconnecting.md) · [Following source context](non-blocking-sockets.md)
