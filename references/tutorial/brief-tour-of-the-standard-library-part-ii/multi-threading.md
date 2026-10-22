# 11.4. Multi-threading

### 11.4. Multi-threading

Threading lets you separate work that has no strict ordering between its parts. One use is to keep an application feeling responsive — accepting user input while other jobs proceed behind the scenes. A close cousin of that pattern is overlapping I/O with computation happening on a separate thread.

The example that follows demonstrates running jobs in the background through the high-level [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module while the primary program keeps executing:

```python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        super().__init__()
        self.infile = infile
        self.outfile = outfile

    def run(self):
        with zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED) as f:
            f.write(self.infile)
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')

```

What makes multi-threaded programs hardest is orchestrating threads that share data or other resources. For exactly that reason, the threading module ships a set of synchronization primitives — among them locks, events, condition variables, and semaphores.

Those facilities are capable, yet even small design slips can produce bugs that are tough to reproduce. The recommended way to coordinate work is therefore to funnel every access to a given resource through one thread, then hand that thread requests from the others by way of the [`queue`](https://docs.python.org/3.14/library/queue.html#module-queue) module. Programs that lean on [`Queue`](https://docs.python.org/3.14/library/queue.html#queue.Queue) objects for communication and coordination between threads turn out easier to construct, more legible, and more dependable.

[Subject index](INDEX.md) · [Previous source section](working-with-binary-data-record-layouts.md) · [Following source section](logging.md)
