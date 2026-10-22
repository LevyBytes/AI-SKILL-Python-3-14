# 8.8. Predefined Clean-up Actions

### 8.8. Predefined Clean-up Actions

Certain objects come with standard clean-up actions meant to run once the object is no longer wanted, irrespective of whether the operation that used the object worked or fell over. Take the example below, which attempts to open a file and display its contents on screen.

```python
for line in open("myfile.txt"):
    print(line, end="")

```

What's wrong with this code is that it keeps the file open for an unpredictable stretch of time after this stretch of code wraps up running. That's harmless in tiny scripts, yet it can become a headache in bigger applications. The [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement lets objects such as files be employed in a manner that guarantees they're always tidied up swiftly and correctly.

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

```

Once the statement has run, the file *f* always ends up closed, even when something went wrong as the lines were being processed. Objects that, like files, come with predefined clean-up actions will note as much in their documentation.

[Subject index](INDEX.md) · [Previous source section](defining-clean-up-actions.md) · [Following source section](constructing-and-catching-exceptiongroup.md)
