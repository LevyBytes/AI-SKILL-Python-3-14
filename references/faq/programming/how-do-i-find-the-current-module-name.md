# How do I find the current module name?

### How do I find the current module name?

A module can discover its own name by inspecting the predefined global variable `__name__`. When that variable holds `'__main__'`, the file is being run directly as a script. Plenty of modules normally consumed via import also ship a command-line interface or a self-test, gating that code behind a check on `__name__`:

```python
def main():
    print('Running test...')
    ...

if __name__ == '__main__':
    main()

```

[Subject index](INDEX.md)
