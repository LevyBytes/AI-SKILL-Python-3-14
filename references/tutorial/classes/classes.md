# 9. Classes

### 9. Classes

By using classes you can package data together with the behavior that operates on it. Defining a new class brings a new *type* of object into being, and from that type you can produce fresh *instances*. Every instance of a class is able to carry attributes that record its own state, and it can also expose methods — supplied by its class — that change that state.

Relative to many other languages, the class facility in Python introduces classes while requiring very little additional syntax or semantics. The design borrows from both the C++ and Modula-3 class systems. Every conventional Object Oriented Programming capability is present in Python classes: inheritance permits more than one base class, a derived class is free to override any of the methods belonging to its base classes, and a method is able to invoke a same-named method defined on a base class. The data an object holds may be of any quantity and of any kind. Just as modules do, classes share Python's dynamic character: they come into existence while the program runs, and you may keep altering them even after they exist.

Speaking in C++ terms, class members — data members included — are ordinarily *public* (with the exception noted later under Private Variables), and member functions are all *virtual*. Following Modula-3, Python offers no abbreviation for accessing the object's members from inside its methods: each method function lists an explicit first parameter that stands for the object, and the call supplies it automatically. Following Smalltalk, classes are themselves objects. That gives meaning to importing them and to renaming them. In contrast to C++ and Modula-3, a user can take built-in types and extend them by using them as base classes. And, as C++ permits, the majority of built-in operators carrying special syntax (arithmetic operators, subscripting, and so on) can be given new definitions for instances of a class.

(Because no single agreed-upon vocabulary exists for discussing classes, I will now and then borrow Smalltalk and C++ wording. Modula-3 terms would suit better, given that its object-oriented semantics sit nearer to Python's than C++'s do, yet I assume hardly any readers know that language.)

[Subject index](INDEX.md) · [Following source section](a-word-about-names-and-objects.md)
