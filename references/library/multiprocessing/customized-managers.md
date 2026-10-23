# multiprocessing - Customized managers

#### Customized managers

To roll your own manager, write a subclass of `BaseManager` and call the `register()` classmethod to register new types or callables with the manager class. To illustrate:

```python
from multiprocessing.managers import BaseManager

class MathsClass:
    def add(self, x, y):
        return x + y
    def mul(self, x, y):
        return x * y

class MyManager(BaseManager):
    pass

MyManager.register('Maths', MathsClass)

if __name__ == '__main__':
    with MyManager() as manager:
        maths = manager.Maths()
        print(maths.add(4, 3))         # prints 7
        print(maths.mul(7, 8))         # prints 56

```

[Subject index](INDEX.md) · [Previous](multiprocessing-managers-namespace-class.md) · [Continue](using-a-remote-manager.md) · [Owning module, declaration or section: multiprocessing](multiprocessing-process-based-parallelism.md)
