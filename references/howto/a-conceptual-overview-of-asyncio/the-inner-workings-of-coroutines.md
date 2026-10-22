# The inner workings of coroutines

### The inner workings of coroutines

To pass control around, `asyncio` makes use of four components.

[`coroutine.send(arg)`](https://docs.python.org/3.14/reference/expressions.html#generator.send) is the method that starts or resumes a coroutine. When the coroutine had been paused and is now resuming, the `arg` argument arrives as the return value of the `yield` statement that paused it in the first place. When the coroutine is being run for the first time (rather than resumed), `arg` has to be `None`.

```python
 1class Rock:
 2    def __await__(self):
 3        value_sent_in = yield 7
 4        print(f"Rock.__await__ resuming with value: {value_sent_in}.")
 5        return value_sent_in
 6
 7async def main():
 8    print("Beginning coroutine main().")
 9    rock = Rock()
10    print("Awaiting rock...")
11    value_from_rock = await rock
12    print(f"Coroutine received value: {value_from_rock} from rock.")
13    return 23
14
15coroutine = main()
16intermediate_result = coroutine.send(None)
17print(f"Coroutine paused and returned intermediate value: {intermediate_result}.")
18
19print(f"Resuming coroutine and sending in value: 42.")
20try:
21    coroutine.send(42)
22except StopIteration as e:
23    returned_value = e.value
24print(f"Coroutine main() finished and provided value: {returned_value}.")

```

[yield](https://docs.python.org/3.14/reference/expressions.html#yieldexpr), as it normally does, halts execution and returns control to the caller. Within the example above, the `yield` on line 3 is triggered by `... = await rock` on line 11. More generally, `await` invokes the [`__await__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__await__) method of the object given to it. `await` does one further special thing too: it propagates (or ?passes along?) whatever `yield`s it gets up the call chain. Here, that means back to `... = coroutine.send(None)` on line 16.

Resuming the coroutine happens through the `coroutine.send(42)` call on line 21. The coroutine continues from the point where it `yield`ed (or paused) on line 3 and runs the rest of the statements in its body. Upon finishing, a coroutine raises a [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception, carrying the return value within the [`value`](https://docs.python.org/3.14/library/exceptions.html#StopIteration.value) attribute.

That snippet yields the following output:

```none
Beginning coroutine main().
Awaiting rock...
Coroutine paused and returned intermediate value: 7.
Resuming coroutine and sending in value: 42.
Rock.__await__ resuming with value: 42.
Coroutine received value: 42 from rock.
Coroutine main() finished and provided value: 23.

```

It is worthwhile to stop here briefly and confirm you tracked the assorted paths along which control flow and values traveled. Many important concepts were addressed, and it pays to make certain your grasp is solid.

The sole way to yield (or in effect cede control) out of a coroutine is to `await` an object whose `__await__` method `yield`s. That may strike you as strange. Perhaps you are wondering:

>

1. What about a `yield` placed directly inside the coroutine function? That turns the coroutine function into an [async generator function](https://docs.python.org/3.14/reference/expressions.html#asynchronous-generator-functions), an altogether different creature.

2. What about a [yield from](https://docs.python.org/3.14/reference/expressions.html#yieldexpr) within the coroutine function pointing to a (plain) generator? That triggers the error: `SyntaxError: yield from not allowed in a coroutine.` This was deliberately set up for the sake of simplicity ? enforcing a single way to use coroutines. At first `yield` was forbidden too, but it was brought back to permit async generators. Even so, `yield from` and `await` accomplish effectively the same thing.

[Subject index](INDEX.md) · [Previous source context](a-conceptual-overview-part-2-the-nuts-and-bolts.md) · [Following source context](futures.md)
