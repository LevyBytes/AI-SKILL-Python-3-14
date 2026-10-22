# Python 3.9.0 alpha 1 / library / exceptions

[bpo-35922](https://bugs.python.org/issue?@action=redirect&bpo=35922): Adjusted `RobotFileParser.crawl_delay()` and `RobotFileParser.request_rate()` so they hand back `None` instead of raising [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) when the robots.txt file defines no matching rule. Rémi Lapeyre wrote the patch.

[bpo-36607](https://bugs.python.org/issue?@action=redirect&bpo=36607): Removed the [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) that [`asyncio.all_tasks()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.all_tasks) could raise whenever a separate thread mutated the internal weak set of tasks mid-iteration.

[bpo-38332](https://bugs.python.org/issue?@action=redirect&bpo=38332): A [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError) raised by `_encoded_words.decode()`, triggered by an encoded-word whose content-type encoding is invalid, is now stopped from bubbling up the whole way to `email.message.get()`.

[bpo-38807](https://bugs.python.org/issue?@action=redirect&bpo=38807): Revised the [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) messages from [`os.path.join()`](https://docs.python.org/3.14/library/os.path.html#os.path.join) so they list [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike) objects among the acceptable input types.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
