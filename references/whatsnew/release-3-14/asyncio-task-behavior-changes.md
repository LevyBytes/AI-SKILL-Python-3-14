# What's new in Python 3.14 / asyncio — asyncio-eventloop, asyncio-graph, asyncio-task

### asyncio

- The function plus the methods called `create_task()` accept any list of keyword arguments now. Every such keyword argument is forwarded to the [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) constructor or onto the custom task factory. (Consult [`set_task_factory()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.set_task_factory) for specifics.) Neither `name` nor `context` keyword arguments stay special anymore; the name ought now to be supplied through the factory's `name` keyword argument, while `context` is permitted to be `None`.

The function plus methods touched here are: [`asyncio.create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.create_task), [`asyncio.loop.create_task()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.create_task), [`asyncio.TaskGroup.create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup.create_task).

(Contributed by Thomas Grainger in [gh-128307](https://github.com/python/cpython/issues/128307).)

- A pair of fresh utility functions can introspect and print the call graph of a program: [`capture_call_graph()`](https://docs.python.org/3.14/library/asyncio-graph.html#asyncio.capture_call_graph) and [`print_call_graph()`](https://docs.python.org/3.14/library/asyncio-graph.html#asyncio.print_call_graph). Consult Asyncio introspection capabilities for further specifics. (Contributed by Yury Selivanov, Pablo Galindo Salgado, and ??ukasz Langa in [gh-91048](https://github.com/python/cpython/issues/91048).)

[Subject index](INDEX.md) · [Previous source section](ast.md) · [Next source section](calendar.md) · [Release/subject declaration](summary-release-highlights.md)
