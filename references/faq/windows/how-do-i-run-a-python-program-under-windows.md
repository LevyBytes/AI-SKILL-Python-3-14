# How do I run a Python program under Windows?

# Windows

### Python on Windows FAQ

### How do I run a Python program under Windows?

There is more to this than meets the eye. Anyone who already knows how to launch programs from the Windows command line will find it all self-evident; if you do not, a bit of extra direction may help.

Short of relying on some kind of integrated development environment, you will wind up *typing* Windows commands into what gets called a “Command prompt window”. As a rule, you can spin up such a window from the search bar by looking for `cmd`. The way to tell you have launched one is the appearance of a Windows “command prompt”, which by and large looks like this:

```doscon
C:\>

```

A different letter could show up, and extra text may trail it, so you could just as readily come across something like:

```doscon
D:\YourName\Projects\Python>

```

which varies with your machine's configuration and whatever you have lately been doing on it. As soon as that window is open, you are most of the way toward running Python programs.

Bear in mind that a separate program, the Python *interpreter*, is what has to process your Python scripts. That interpreter takes in your script, turns it into bytecodes, and then runs those bytecodes to carry out your program. So how do you get the interpreter to take charge of your Python?

To begin, confirm that your command window treats the word “py” as a directive to fire up the interpreter. With a command window open, go ahead and type the command `py`, then press return:

```doscon
C:\Users\YourName> py

```

What follows should resemble:

```pycon
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>

```

What you have launched is the interpreter running in “interactive mode”. In other words, you can type Python statements or expressions on the spot and watch them get run or evaluated then and there. It ranks among Python's most powerful capabilities. Try it out by feeding in a handful of expressions you choose and observing what comes back:

```pycon
>>> print("Hello")
Hello
>>> "Hello" * 3
'HelloHelloHello'

```

Plenty of folks treat interactive mode as a handy calculator that also happens to be fully programmable. To wrap up your interactive Python session, invoke the [`exit()`](https://docs.python.org/3.14/library/constants.html#exit) function, or keep the Ctrl key held while pressing Z and then tap “Enter” to return to your Windows command prompt.

It may also turn out that a Start-menu item like Start ‣ Programs ‣ Python 3.x ‣ Python (command line) is present, and choosing it brings up the `>>>` prompt inside a fresh window. Should that be the case, the window vanishes once you invoke the [`exit()`](https://docs.python.org/3.14/library/constants.html#exit) function or type the Ctrl-Z character; what Windows did was run one lone “python” command in that window, and it shuts the window the moment you end the interpreter.

With the `py` command confirmed as recognized, you can now hand your Python script over to it. The script does need either an absolute or a relative path supplied. Suppose your Python script sits on your desktop under the name `hello.py`, and your command prompt happens to be open in your home directory, so what you see resembles:

```none
C:\Users\YourName>

```

At this point you direct the `py` command to pass your script along to Python by entering `py` and then your script path:

```none
C:\Users\YourName> py Desktop\hello.py
hello

```

[Subject index](INDEX.md)
