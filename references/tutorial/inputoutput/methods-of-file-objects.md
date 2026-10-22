# 7.2.1. Methods of File Objects

### 7.2.1. Methods of File Objects

For the remaining examples throughout this section, take it as given that a file object named `f` is already in hand.

To pull in a file's contents, invoke `f.read(size)`, which grabs some amount of data and hands it back as a string in text mode or a bytes object in binary mode. The numeric argument *size* is optional. Drop *size* or make it negative and the whole file is read and returned; if the file happens to be twice the size of your machine's memory, that's on you. Otherwise no more than *size* characters in text mode, or *size* bytes in binary mode, get read and returned. Where the file's end has already been hit, `f.read()` comes back with an empty string (`''`).

```python
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''

```

`f.readline()` pulls one line from the file; a newline character (`\n`) stays at the string's tail, dropped only on the file's final line when the file doesn't close with a newline. That keeps the return value free of ambiguity: an empty string back from `f.readline()` signals the file's end has been reached, whereas a blank line shows up as `'\n'`, a string holding nothing but one newline.

```python
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''

```

When you want to read a file line by line, you can iterate over the file object directly. That approach is light on memory, quick, and yields tidy code:

```python
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file

```

To gather every line of a file into a list, you have `list(f)` or `f.readlines()` at your disposal as well.

`f.write(string)` puts the contents of *string* into the file and hands back the count of characters it wrote.

```python
>>> f.write('This is a test\n')
15

```

Objects of other types have to be turned first into a string (in text mode) or into a bytes object (in binary mode) before you can write them:

```python
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18

```

`f.tell()` yields an integer that reports the file object's present spot within the file: a byte count from the file's start while in binary mode, and an opaque number while in text mode.

To move the file object's position, call `f.seek(offset, whence)`. The new position is worked out by adding *offset* onto a reference point, and which reference point applies is chosen by the *whence* argument. With *whence* set to 0 the measurement runs from the file's start, 1 takes the current file position, and 2 takes the file's end as the reference point. You may leave *whence* out, in which case it defaults to 0 and the file's start serves as the reference point.

```python
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'

```

With text files (the ones opened without a `b` in the mode string), the only seeks permitted are those measured from the file's start (the lone exception being a seek to the very end of the file via `seek(0, 2)`), and the *offset* values you may legitimately use are those that `f.tell()` returned, or zero. Feed in any other *offset* value and the behaviour is undefined.

A few further methods belong to file objects, among them the less commonly reached-for [`isatty()`](https://docs.python.org/3.14/library/io.html#io.IOBase.isatty) and [`truncate()`](https://docs.python.org/3.14/library/io.html#io.IOBase.truncate); for an exhaustive guide to file objects, turn to the Library Reference.

[Subject index](INDEX.md) · [Previous source section](reading-and-writing-files.md) · [Following source section](saving-structured-data-with-json.md)
