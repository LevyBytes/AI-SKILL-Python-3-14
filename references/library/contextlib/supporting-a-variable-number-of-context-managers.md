# contextlib — Supporting a variable number of context managers

### Supporting a variable number of context managers

`ExitStack` shines most in the scenario its class documentation highlights: handling an unknown count of context managers plus other teardown work inside one [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. That uncertainty can stem from how many context managers you need depending on user input (opening whatever set of files a user names, say), or from certain context managers being optional:

```python
with ExitStack() as stack:
    for resource in resources:
        stack.enter_context(resource)
    if need_special_resource():
        special = acquire_special_resource()
        stack.callback(release_special_resource, special)
    # Perform operations that use the acquired resources

```

The snippet illustrates how `ExitStack` lets [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statements govern any resource at all, even ones that lack built-in support for the context management protocol.

[Subject index](INDEX.md) · [Previous](examples-and-recipes.md) · [Continue](catching-exceptions-from-enter-methods.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md)
