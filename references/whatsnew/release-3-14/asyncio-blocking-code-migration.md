# What's new in Python 3.14 / asyncio

```python
async def operation_one(): ...
def blocking_code(): ...
async def operation_two(): ...

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(operation_one())
    blocking_code()
    loop.run_until_complete(operation_two())
finally:
    loop.close()

```

After:

```python
async def operation_one(): ...
def blocking_code(): ...
async def operation_two(): ...

with asyncio.Runner() as runner:
    runner.run(operation_one())
    blocking_code()
    runner.run(operation_two())

```

[Subject index](INDEX.md) · [Next source section](email.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](asyncio-main-and-main.md) · [Preceding release/subject continuation](asyncio-runner-migration.md)
