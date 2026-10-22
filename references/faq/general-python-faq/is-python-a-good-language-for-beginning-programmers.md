# Is Python a good language for beginning programmers?

### Is Python a good language for beginning programmers?

Yes.

Starting students off with a procedural, statically typed language — Pascal, C, or some slice of C++ or Java — remains widespread. Learning Python first may well serve those students better. Its syntax is very simple and consistent, its standard library is large, and — above all — using it in an introductory programming course frees students to focus on essential skills like breaking down problems and designing data types. Python lets students meet basic ideas such as loops and procedures right away. Quite likely they can even handle user-defined objects in that very first course.

For someone who has never written code, a statically typed language feels unnatural. It adds complexity the student has to conquer and drags down the course's tempo. Students are already busy learning to think like a computer, to break problems apart, to design coherent interfaces, and to wrap up data. Grasping a statically typed language matters down the road, yet it isn't necessarily the ideal subject for a student's opening programming course.

Numerous further qualities make Python a fine first language. As with Java, Python ships a large standard library, so students can be handed programming projects very early in the term that *do* something. Such assignments need not stay confined to the usual four-function calculator and checkbook-balancing programs. Drawing on the standard library, students get the gratification of building realistic applications while they pick up programming basics. Leaning on the standard library also schools students in code reuse. Third-party modules like PyGame further widen the students' horizons.

Thanks to Python's interactive interpreter, students can try out language features as they program. They can hold one window open with the interpreter running while typing their program's source into another. Should they forget which methods a list offers, they might run something along these lines:

```python
>>> L = []
>>> dir(L)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
'__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__',
'__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__',
'__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__',
'__sizeof__', '__str__', '__subclasshook__', 'append', 'clear',
'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
'reverse', 'sort']
>>> [d for d in dir(L) if '__' not in d]
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

>>> help(L.append)
Help on built-in function append:

append(...)
    L.append(object) -> None -- append object to end

>>> L.append(1)
>>> L
[1]

```

With the interpreter at hand, documentation is always close by while the student programs.

Good IDEs for Python are available as well. IDLE, a cross-platform Python IDE, is itself written in Python with Tkinter. Emacs devotees will be glad that a very capable Python mode exists for Emacs. Every one of these programming environments delivers syntax highlighting, auto-indenting, and access to the interactive interpreter as you code. For a complete roster of Python editing environments, consult [the Python wiki](https://wiki.python.org/moin/PythonEditors).

Should you wish to talk over Python's role in education, joining [the edu-sig mailing list](https://www.python.org/community/sigs/current/edu-sig) might appeal to you.

[Subject index](INDEX.md)
