# tkinter.dnd: `tkinter.dnd.DndHandler`

## tkinter.dnd — Drag and drop support

### `tkinter.dnd` — Drag and drop support

**Source code:** [Lib/tkinter/dnd.py](https://github.com/python/cpython/tree/3.14/Lib/tkinter/dnd.py)

---

Note

This remains experimental and is slated for deprecation once the Tk DND replacement lands.

Drag-and-drop between objects inside one application — within a single window or across windows — is handled by the `tkinter.dnd` module. Making an object draggable means setting up an event binding on it that kicks off the drag-and-drop process. The usual approach binds a ButtonPress event to a callback you supply (see [Bindings and Events](https://docs.python.org/3.14/library/tkinter.html#bindings-and-events)). Inside that function, call `dnd_start()`, where ‘source’ names the object being dragged and ‘event’ is the event that triggered the call (the argument passed to your callback function).

A target object gets selected in the following way:

1.

Top-down scan of the region beneath the mouse for a target widget

>
- The target widget needs a callable *dnd_accept* attribute

- Should *dnd_accept* be absent or return `None`, the search advances to the parent widget

- Where no target widget turns up, the target object becomes `None`

1.

Call to *<old_target>.dnd_leave(source, event)*

2.

Call to *<new_target>.dnd_enter(source, event)*

3.

Call to *&lt;target&gt;.dnd_commit(source, event)* to notify of drop

4.

Call to *<source>.dnd_end(target, event)* to signal end of drag-and-drop

 *class *tkinter.dnd.DndHandler(*source*, *event*)

Drag-and-drop events are managed by the *DndHandler* class, which watches Motion and ButtonRelease events on the root of the event widget.

[Subject index](INDEX.md) · [Continue](drag-handler-cancellation-and-release.md)
