# concurrent.futures: `concurrent.futures.Future`

### Future Objects

A callable's asynchronous execution is wrapped up by the `Future` class. You obtain `Future` instances from `Executor.submit()`.

 *class *concurrent.futures.Future

Wraps up the asynchronous execution of a callable. You get `Future` instances from `Executor.submit()`, and outside of testing you shouldn't construct them directly.

[Subject index](INDEX.md) · [Previous](processpoolexecutor-example.md) · [Continue](future-cancellation-results-and-running-state.md)
