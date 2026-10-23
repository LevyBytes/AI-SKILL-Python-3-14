# concurrent.interpreters - Communication Between Interpreters

### Communication Between Interpreters

Realistically, several interpreters earn their keep only when there’s some channel for them to talk to one another. Typically that means a form of message passing, though it can even stretch to sharing data in a carefully governed manner.

For that reason the `concurrent.interpreters` module ships a [`queue.Queue`](https://docs.python.org/3.14/library/queue.html#queue.Queue) implementation, reachable via `create_queue()`.

[Subject index](INDEX.md) · [Previous](concurrency-and-parallelism.md) · [Continue](sharing-objects.md) · [Owning module, declaration or section: concurrent.interpreters](multiple-interpreters-overview.md)
