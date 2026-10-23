# turtledemo`turtledemo` - Demo scripts

### `turtledemo` - Demo scripts

A collection of demo scripts ships inside the `turtledemo` package. You can run and view these scripts through the bundled demo viewer like so:

```python
python -m turtledemo

```

You can instead run the demo scripts one by one. For instance,

```python
python -m turtledemo.bytedesign

```

Inside the `turtledemo` package directory you will find:

- A demo viewer `__main__.py` that lets you read the sourcecode of the scripts and run them simultaneously.

- Several scripts that each showcase a distinct capability of the `turtle` module. The Examples menu provides access to them, and they will run standalone as well.

- A `turtle.cfg` file that stands as an example of how such files should be written and used.

The demo scripts are:

| Name | Description | Features |
| --- | --- | --- |
| `bytedesign` | complex classical turtle graphics pattern | `tracer()`, `delay()`, `update()` |
| `chaos` | plots Verhulst dynamics, illustrating how a computer’s calculations may at times yield outcomes that defy common sense | world coordinates |
| `clock` | analog clock showing time of your computer | turtles as clock’s hands, `ontimer()` |
| `colormixer` | experiment with r, g, b | `ondrag()` |
| `forest` | 3 breadth-first trees | randomization |
| `fractalcurves` | Hilbert & Koch curves | recursion |
| `lindenmayer` | ethnomathematics (indian kolams) | L-System |
| `minimal_hanoi` | Towers of Hanoi | Rectangular Turtles as Hanoi discs (`shape()`, `shapesize()`) |
| `nim` | take on the computer at the classic nim game using three heaps of sticks. | turtles as nimsticks, event driven (mouse, keyboard) |
| `paint` | super minimalistic drawing program | `onclick()` |
| `peace` | elementary | turtle: appearance and animation |
| `penrose` | aperiodic tiling with kites and darts | `stamp()` |
| `planet_and_moon` | simulation of gravitational system | compound shapes, `Vec2D` |
| `rosette` | a pattern from the wikipedia article on turtle graphics | `clone()`, `undo()` |
| `round_dance` | dancing turtles rotating pairwise in opposite direction | compound shapes, `clone()` `shapesize()`, `tilt()`, `get_shapepoly()`, `update()` |
| `sorting_animate` | visual demonstration of different sorting methods | simple alignment, randomization |
| `tree` | a (graphical) breadth first tree (using generators) | `clone()` |
| `two_canvases` | simple design | turtles on two canvases |
| `yinyang` | another elementary example | `circle()` |

Have fun!

[Subject index](INDEX.md) · [Previous](../turtle/how-to-configure-screen-and-turtles.md) · [Continue](changes-since-python-2-6.md)
