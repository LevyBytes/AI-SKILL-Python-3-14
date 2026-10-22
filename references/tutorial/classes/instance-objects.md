# 9.3.3. Instance Objects

### 9.3.3. Instance Objects

So what is it we can do with instance objects? The sole operations instance objects comprehend are attribute references. Valid attribute names fall into two categories: data attributes and methods.

*Data attributes* line up with "instance variables" in Smalltalk and with "data members" in C++. You needn't declare data attributes; like local variables, they pop into existence the first moment something assigns to them. As an example, if `x` is the `MyClass` instance built earlier, the following snippet will print the value `16` and leave nothing behind:

```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

```

A *method* makes up the second category of attribute reference on an instance. Think of a method as a function that an object "owns."

Which method names are valid for an instance object hinges on its class. By definition, all of a class's attributes that happen to be function objects supply matching methods on its instances. So in our example, `x.f` is a valid method reference, because `MyClass.f` is a function, while `x.i` is not, because `MyClass.i` isn't one. Yet `x.f` and `MyClass.f` aren't the same thing — `x.f` is a *method object*, not a function object.

[Subject index](INDEX.md) · [Previous source section](class-objects.md) · [Following source section](method-objects.md)
