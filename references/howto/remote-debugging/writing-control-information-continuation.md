# Writing control information continuation

The script runs asynchronously, so you cannot remove the script file the moment it has been injected. Before deleting it, the debugger ought to hold off until the injected script causes some effect it can observe. Exactly which effect that is hinges on the script's purpose. A debugger might, say, hang back until the remote process reconnects to a socket before it clears the script away. As soon as such a sign appears, the file can safely be regarded as obsolete.

[Subject index](INDEX.md) · [Previous source owning section](writing-control-information.md) · [Following source context](summary.md)
