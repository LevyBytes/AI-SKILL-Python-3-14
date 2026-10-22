# Python 3.14 changes: Asyncio introspection commands and capabilities

### Asyncio introspection capabilities

A fresh command-line interface now lets you examine live Python processes that rely on asynchronous tasks, reachable through `python -m asyncio ps PID` or `python -m asyncio pstree PID`.

Pointed at a given process ID (PID), the `ps` subcommand reports on the asyncio tasks that are presently active. Its output is a task table, namely a flat enumeration of every task, the names they carry, the coroutine stacks behind them, and which tasks happen to be awaiting them.

While gathering identical data, the `pstree` subcommand instead draws a visual async call tree that lays out coroutine relationships hierarchically. Debugging asynchronous programs that hang or run for a long time is exactly where this command shines. Developers can lean on it to pinpoint fast where a program stalls, which tasks remain pending, and the way coroutines link to one another.

Take this code as an illustration:

```python
import asyncio

async def play_track(track):
    await asyncio.sleep(5)
    print(f'🎵 Finished: {track}')

async def play_album(name, tracks):
    async with asyncio.TaskGroup() as tg:
        for track in tracks:
            tg.create_task(play_track(track), name=track)

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(
          play_album('Sundowning', ['TNDNBTG', 'Levitate']),
          name='Sundowning')
        tg.create_task(
          play_album('TMBTE', ['DYWTYLM', 'Aqua Regia']),
          name='TMBTE')

if __name__ == '__main__':
    asyncio.run(main())

```

Pointing the new tool at the live process produces a table along these lines:

```bash
python -m asyncio ps 12345

tid        task id              task name            coroutine stack                                    awaiter chain                                      awaiter name    awaiter id
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1935500    0x7fc930c18050       Task-1               TaskGroup._aexit -> TaskGroup.__aexit__ -> main                                                                       0x0
1935500    0x7fc930c18230       Sundowning           TaskGroup._aexit -> TaskGroup.__aexit__ -> album   TaskGroup._aexit -> TaskGroup.__aexit__ -> main    Task-1          0x7fc930c18050
1935500    0x7fc93173fa50       TMBTE                TaskGroup._aexit -> TaskGroup.__aexit__ -> album   TaskGroup._aexit -> TaskGroup.__aexit__ -> main    Task-1          0x7fc930c18050
1935500    0x7fc93173fdf0       TNDNBTG              sleep -> play                                      TaskGroup._aexit -> TaskGroup.__aexit__ -> album   Sundowning      0x7fc930c18230
1935500    0x7fc930d32510       Levitate             sleep -> play                                      TaskGroup._aexit -> TaskGroup.__aexit__ -> album   Sundowning      0x7fc930c18230
1935500    0x7fc930d32890       DYWTYLM              sleep -> play                                      TaskGroup._aexit -> TaskGroup.__aexit__ -> album   TMBTE           0x7fc93173fa50
1935500    0x7fc93161ec30       Aqua Regia           sleep -> play                                      TaskGroup._aexit -> TaskGroup.__aexit__ -> album   TMBTE           0x7fc93173fa50

```

or a tree resembling this:

[Subject index](INDEX.md) · [Previous source section](pep-784-zstandard-support-in-the-standard-library.md) · [Next source section](asyncio-task-tree-output.md) · [Release/subject declaration](summary-release-highlights.md)
