# tkinter - Threading model

### Threading model

Python and Tcl/Tk follow markedly different threading models, a divide that `tkinter` works to bridge. If threads are part of your program, this is something you may need to keep in mind.

A single Python interpreter can have a great many threads attached to it. Within Tcl, you can spin up multiple threads too, but each one is paired with its own separate Tcl interpreter instance. A thread can even create more than one interpreter instance, although any given interpreter instance may be used solely by the one thread that created it.

Each `Tk` object that `tkinter` creates holds a Tcl interpreter. It also remembers which thread brought that interpreter into being. Calls into `tkinter` are permitted from any Python thread. Internally, should a call originate in some thread besides the one responsible for creating the `Tk` object, an event gets queued onto the interpreter’s event queue, and once it runs, the result travels back to the Python thread that made the call.

By their nature, Tcl/Tk applications are usually event-driven: after initialization, the interpreter spins up an event loop (i.e. `Tk.mainloop()`) and reacts to events. Since it is single-threaded, event handlers have to finish quickly, or else they’ll keep other events from getting processed. To sidestep that, any long-running computation ought to stay out of an event handler, instead being chopped into smaller chunks via timers or shifted onto another thread. This stands apart from numerous GUI toolkits in which the GUI runs in a thread fully separate from all application code, event handlers included.

Whenever the Tcl interpreter isn’t running the event loop and processing events, any `tkinter` calls issued from threads other than the one running the Tcl interpreter will fail.

There are several special cases:

- Tcl/Tk libraries may be compiled such that they aren’t thread-aware. When that’s so, `tkinter` invokes the library from the originating Python thread, even if it differs from the thread that created the Tcl interpreter. A global lock makes certain that only a single call happens at any moment.

- Although `tkinter` permits you to create more than one instance of a `Tk` object (each with its own interpreter), every interpreter belonging to the same thread shares one common event queue, and that turns messy in a hurry. As a practical matter, don’t keep more than one `Tk` instance alive at a time. Failing that, you’re best off creating them on separate threads and making sure you’re using a thread-aware Tcl/Tk build.

- Blocking event handlers aren’t the sole means of keeping the Tcl interpreter from re-entering the event loop. You can even run several nested event loops or drop out of the event loop completely. If you’re attempting anything clever with events or threads, stay mindful of these possibilities.

- A handful of select `tkinter` functions currently work only when invoked from the thread that created the Tcl interpreter.

[Subject index](INDEX.md) · [Previous](navigating-the-tcl-tk-reference-manual.md) · [Continue](setting-options.md) · [Owning module, declaration or section: tkinter](tkinter-python-interface-to-tcl-tk.md)
