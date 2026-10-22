# Custom Policies

### Custom Policies

When you want to implement a fresh event loop policy, the suggested route is to subclass `DefaultEventLoopPolicy` and override whichever methods need custom behavior, for instance:

```python
class MyEventLoopPolicy(asyncio.DefaultEventLoopPolicy):

    def get_event_loop(self):
        """Get the event loop.

        This may be None or an instance of EventLoop.
        """
        loop = super().get_event_loop()
        # Do something with loop ...
        return loop

asyncio.set_event_loop_policy(MyEventLoopPolicy())

```

[Subject index](INDEX.md) · [Previous](asyncio-windowsproactoreventlooppolicy-class.md)
