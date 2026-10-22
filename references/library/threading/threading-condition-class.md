# threading: `threading.Condition`

### Condition objects

Every condition variable goes hand in hand with some kind of lock; you can supply one or let a default be made for you. Supplying one helps when multiple condition variables have to share a single lock. Since the lock forms part of the condition object, you need not keep tabs on it on your own.

A condition variable follows the context management protocol: a `with` statement takes the linked lock for the span of the wrapped block. Its `acquire()` and `release()` methods likewise invoke the matching methods on the linked lock.

The other methods have to be invoked while holding the linked lock. The `wait()` method frees the lock, then blocks until a different thread rouses it with a `notify()` or `notify_all()` call. After being roused, `wait()` takes the lock again and returns. Supplying a timeout is also an option.

The `notify()` method rouses one of the threads waiting on the condition variable, when any are waiting. The `notify_all()` method rouses every thread waiting on the condition variable.

Note: neither the `notify()` nor the `notify_all()` method frees the lock; this means the roused thread or threads do not return from their `wait()` call right away, but only after the thread that issued `notify()` or `notify_all()` at last gives up the lock.

The standard programming approach with condition variables leans on the lock to coordinate access to some shared state; threads concerned with a specific state change invoke `wait()` over and over until the state they want appears, while threads that alter the state invoke `notify()` or `notify_all()` whenever they change it in a way that might match what one of the waiters seeks. As an illustration, the code below is a generic producer-consumer scenario with unbounded buffer capacity:

```python
# Consume one item
with cv:
    while not an_item_is_available():
        cv.wait()
    get_an_available_item()

# Produce one item
with cv:
    make_an_item_available()
    cv.notify()

```

The `while` loop verifying the application's condition is required because `wait()` may come back after an arbitrarily long delay, and the condition that triggered the `notify()` call might no longer hold. That is intrinsic to multi-threaded programming. The `wait_for()` method handles the condition checking automatically and simplifies working out timeouts:

```python
# Consume an item
with cv:
    cv.wait_for(an_item_is_available)
    get_an_available_item()

```

When deciding between `notify()` and `notify_all()`, weigh whether a single state change could matter to just one waiting thread or to several. For instance, in the usual producer-consumer scenario, putting one item into the buffer only requires rousing a single consumer thread.

 *class *threading.Condition(*lock=None*)

This class provides condition variable objects. A condition variable lets one or more threads hold until another thread notifies them.

When the *lock* argument is supplied and is not `None`, it has to be a `Lock` or `RLock` object, and it serves as the underlying lock. If not, a fresh `RLock` object is built and serves as the underlying lock.

Changed in version 3.3: was previously a factory function, and is now a class.

[Subject index](INDEX.md) · [Previous](threading-rlock-acquire-to-threading-rlock-locked.md) · [Continue](threading-condition-acquire-to-threading-condition-notify-all.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md)
