# contextlib — Cleaning up in an `__enter__` implementation

### Cleaning up in an `__enter__` implementation

The `ExitStack.push()` documentation points out that this method helps tidy up a resource you've already allocated when subsequent stages of the [`__enter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__enter__) body go wrong.

The example below applies that idea to a context manager which takes resource acquisition and release callables, plus an optional validation callable, and wires them into the context management protocol:

```python
from contextlib import contextmanager, AbstractContextManager, ExitStack

class ResourceManager(AbstractContextManager):

    def __init__(self, acquire_resource, release_resource, check_resource_ok=None):
        self.acquire_resource = acquire_resource
        self.release_resource = release_resource
        if check_resource_ok is None:
            def check_resource_ok(resource):
                return True
        self.check_resource_ok = check_resource_ok

    @contextmanager
    def _cleanup_on_error(self):
        with ExitStack() as stack:
            stack.push(self)
            yield
            # The validation check passed and didn't raise an exception
            # Accordingly, we want to keep the resource, and pass it
            # back to our caller
            stack.pop_all()

    def __enter__(self):
        resource = self.acquire_resource()
        with self._cleanup_on_error():
            if not self.check_resource_ok(resource):
                msg = "Failed validation for {!r}"
                raise RuntimeError(msg.format(resource))
        return resource

    def __exit__(self, *exc_details):
        # We don't need to duplicate any of our resource release logic
        self.release_resource()

```

[Subject index](INDEX.md) · [Previous](catching-exceptions-from-enter-methods.md) · [Continue](replacing-any-use-of-try-finally-and-flag-variables.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md)
