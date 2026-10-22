# What’s New In Python 3.8 / unittest — unittest, unittest.mock

### unittest

A new [`AsyncMock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.AsyncMock) arrived to provide an asynchronous flavor of [`Mock`](https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock). Suitable fresh assert functions for testing were supplied too. (Contributed by Lisa Roach in [bpo-26467](https://bugs.python.org/issue?@action=redirect&bpo=26467)).

A pair of additions, [`addModuleCleanup()`](https://docs.python.org/3.14/library/unittest.html#unittest.addModuleCleanup) and [`addClassCleanup()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.addClassCleanup), arrived in unittest to allow cleanups for [`setUpModule()`](https://docs.python.org/3.14/library/unittest.html#unittest.setUpModule) and [`setUpClass()`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.setUpClass). (Contributed by Lisa Roach in [bpo-24412](https://bugs.python.org/issue?@action=redirect&bpo=24412).)

Upon failure, several mock assert functions henceforth also print a list of the calls that actually occurred. (Contributed by Petter Strandmark in [bpo-35047](https://bugs.python.org/issue?@action=redirect&bpo=35047).)

The [`unittest`](https://docs.python.org/3.14/library/unittest.html#module-unittest) module picked up support for using coroutines as test cases via [`unittest.IsolatedAsyncioTestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.IsolatedAsyncioTestCase). (Contributed by Andrew Svetlov in [bpo-32972](https://bugs.python.org/issue?@action=redirect&bpo=32972).)

Example:

```python
import unittest

class TestRequest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.connection = await AsyncConnection()

    async def test_get(self):
        response = await self.connection.get("https://example.com")
        self.assertEqual(response.status_code, 200)

    async def asyncTearDown(self):
        await self.connection.close()

if __name__ == "__main__":
    unittest.main()

```

[Subject index](INDEX.md) · [Previous source section](unicodedata.md) · [Next source section](venv.md) · [Release/subject declaration](assignment-expressions.md)
