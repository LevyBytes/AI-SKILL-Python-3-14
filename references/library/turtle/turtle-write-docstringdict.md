# Translation of docstrings into different languages

### Translation of docstrings into different languages

A utility exists for building a dictionary whose keys are the method names and whose values are the docstrings of the public methods belonging to the Screen and Turtle classes.

 turtle.write_docstringdict(*filename='turtle_docstringdict'*)

Parameters:

**filename** – a string, used as filename

Build and save a docstring-dictionary into a Python script under the supplied filename. You must invoke this function on purpose (the turtle graphics classes never call it themselves). The docstring dictionary lands in the Python script `*filename*.py`. Its purpose is to act as a template for translating the docstrings into other languages.

Should you (or your students) wish to use `turtle` with online help in your own language, translate the docstrings and store the result as, for instance, `turtle_docstringdict_german.py`.

Given a suitable entry in your `turtle.cfg` file, this dictionary gets loaded at import time and supplants the original English docstrings.

As of this writing, docstring dictionaries exist in German and Italian. (Send requests to [glingl@aon.at](mailto:glingl%40aon.at).)

[Subject index](INDEX.md) · [Previous](how-to-use-help.md) · [Continue](how-to-configure-screen-and-turtles.md)
