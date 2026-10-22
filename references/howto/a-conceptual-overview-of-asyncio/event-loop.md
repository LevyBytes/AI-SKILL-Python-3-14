# Event Loop

### Event Loop

Within `asyncio`, every action takes place in relation to the event loop. It is the centerpiece of the whole system. Picture it as the conductor of an orchestra. From offstage, it oversees resources. A portion of its authority is handed to it outright, yet much of what it accomplishes stems from the deference and teamwork of its worker bees.

Put more technically, the event loop holds a set of jobs awaiting execution. Certain jobs you place there yourself, while others land there indirectly through `asyncio`. The event loop pulls a job out of its pending workload and runs it (or ?gives it control?), much as you would call a function, after which that job executes. As soon as it stops or wraps up, control passes back to the event loop. Next, the event loop picks a different job from its pool and runs that one. You can *roughly* picture the set of jobs as a queue: items get added and then handled one by one, usually (though not invariably) in sequence. The cycle keeps repeating without end, the event loop spinning along forever. Whenever no jobs remain to be executed, the event loop has the sense to idle rather than burn CPU cycles for nothing, returning once there is additional work to handle.

Smooth execution depends on jobs taking turns nicely and working together; a selfish job might cling to control and starve everything else, which would make the whole event loop scheme fairly pointless.

```python
import asyncio

# This creates an event loop and indefinitely cycles through
# its collection of jobs.
event_loop = asyncio.new_event_loop()
event_loop.run_forever()

```

[Subject index](INDEX.md) · [Previous source context](a-conceptual-overview-part-1-the-high-level.md) · [Following source context](asynchronous-functions-and-coroutines.md)
