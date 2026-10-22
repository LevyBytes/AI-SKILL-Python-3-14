# Asynchronous functions and coroutines

### Asynchronous functions and coroutines

Here is a plain, unexciting Python function:

```python
def hello_printer():
    print(
        "Hi, I am a lowly, simple printer, though I have all I "
        "need in life -- \nfresh paper and my dearly beloved octopus "
        "partner in crime."
    )

```

When you call an ordinary function, its body or logic runs:

```python
>>> hello_printer()
Hi, I am a lowly, simple printer, though I have all I need in life --
fresh paper and my dearly beloved octopus partner in crime.

```

Using [async def](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) rather than a bare `def` turns this into an asynchronous function (or ?coroutine function?). When called, it builds and hands back a [coroutine](https://docs.python.org/3.14/library/asyncio-task.html#coroutine) object.

```python
async def loudmouth_penguin(magic_number: int):
    print(
     "I am a super special talking penguin. Far cooler than that printer. "
     f"By the way, my lucky number is: {magic_number}."
    )

```

Invoking the async function `loudmouth_penguin` will not run the print statement; what it does instead is produce a coroutine object:

```python
>>> loudmouth_penguin(magic_number=3)
<coroutine object loudmouth_penguin at 0x104ed2740>

```

People frequently blur ?coroutine function? and ?coroutine object? together into coroutine. That tends to cause confusion! Throughout this article, coroutine means specifically a coroutine object, or to be exact, an instance of [`types.CoroutineType`](https://docs.python.org/3.14/library/types.html#types.CoroutineType) (native coroutine). Keep in mind that coroutines may also turn up as instances of [`collections.abc.Coroutine`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Coroutine) ? a difference that becomes relevant for type checking.

A coroutine stands in for the logic or body of the function. Starting a coroutine has to be done deliberately; once more, simply building the coroutine will not start it. Importantly, a coroutine can halt and pick back up at multiple spots inside the function's body. It is exactly that ability to halt and resume that enables asynchronous behavior!

Coroutines together with coroutine functions were constructed on top of the machinery behind [generators](https://docs.python.org/3.14/glossary.html#term-generator-iterator) and [generator functions](https://docs.python.org/3.14/glossary.html#term-generator). Remember that a generator function is one that [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield)s, such as the following:

```python
def get_random_number():
    # This would be a bad random number generator!
    print("Hi")
    yield 1
    print("Hello")
    yield 7
    print("Howdy")
    yield 4
    ...

```

Just like a coroutine function, invoking a generator function does not execute it. What you get back instead is a generator object:

```python
>>> get_random_number()
<generator object get_random_number at 0x1048671c0>

```

To advance to a generator's next `yield`, reach for the built-in function [`next()`](https://docs.python.org/3.14/library/functions.html#next). Said differently, the generator executes and then halts. Here is an example:

```python
>>> generator = get_random_number()
>>> next(generator)
Hi
1
>>> next(generator)
Hello
7

```

[Subject index](INDEX.md) · [Previous source context](event-loop.md) · [Following source context](tasks.md)
