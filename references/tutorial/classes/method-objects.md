# 9.3.4. Method Objects

### 9.3.4. Method Objects

A method is generally called immediately after being bound:

```python
x.f()

```

Given `x = MyClass()` as above, this hands back the string `'hello world'`. Calling a method on the spot isn't mandatory, though: `x.f` is a method object, so it can be tucked away and called later on. For example:

```python
xf = x.f
while True:
    print(xf())

```

will go on printing `hello world` for all eternity.

So what actually goes on when a method gets called? You might have observed that `x.f()` above was called with no argument, even though `f()`'s function definition listed an argument. Where did the argument go? Surely Python throws an exception whenever a function demanding an argument is called with none — even when the argument never gets used?

You may in fact already have figured it out: what makes methods special is that the instance object is supplied as the function's first argument. In our example, the call `x.f()` is precisely the same as `MyClass.f(x)`. More broadly, calling a method with a list of *n* arguments amounts to calling the matching function with an argument list formed by slotting the method's instance object in ahead of the first argument.

In general terms, the mechanics run as follows. Referencing a non-data attribute on an instance triggers a search of that instance's class. If the name resolves to a valid class attribute holding a function object, then a method object is built that packs together a reference to the instance object alongside a reference to the function object. Once that method object is invoked with some argument list, a brand-new argument list gets assembled out of the instance object and the original argument list, after which the function object runs with this freshly built list.

[Subject index](INDEX.md) · [Previous source section](instance-objects.md) · [Following source section](class-and-instance-variables.md)
