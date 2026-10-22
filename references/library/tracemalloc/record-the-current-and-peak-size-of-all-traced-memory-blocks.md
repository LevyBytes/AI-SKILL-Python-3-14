# tracemalloc — Record the current and peak size of all traced memory blocks

#### Record the current and peak size of all traced memory blocks

The snippet below adds up two series such as `0 + 1 + 2 + ...` in a wasteful way: it materializes a list of the integers first. That list briefly eats a large amount of memory. By calling `get_traced_memory()` along with `reset_peak()`, we can watch both the modest footprint left once the sum finishes and the peak reached while the work was underway:

```python
import tracemalloc

tracemalloc.start()

# Example code: compute a sum with a large temporary list
large_sum = sum(list(range(100000)))

first_size, first_peak = tracemalloc.get_traced_memory()

tracemalloc.reset_peak()

# Example code: compute a sum with a small temporary list
small_sum = sum(list(range(1000)))

second_size, second_peak = tracemalloc.get_traced_memory()

print(f"{first_size=}, {first_peak=}")
print(f"{second_size=}, {second_peak=}")

```

Output:

```python
first_size=664, first_peak=3592984
second_size=804, second_peak=29704

```

Thanks to `reset_peak()`, the peak reached during the `small_sum` computation was recorded faithfully, despite being far below the largest peak observed since the `start()` call. Had `reset_peak()` not been invoked, `second_peak` would have remained the peak left over from the `large_sum` computation (in other words, identical to `first_peak`). Both peaks here sit well above the final memory footprint, hinting that optimisation is possible (drop the needless [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) call and write `sum(range(...))` instead).

[Subject index](INDEX.md) · [Previous](pretty-top.md) · [Continue](tracemalloc-clear-traces-to-tracemalloc-take-snapshot.md) · [Owning module, declaration or section: tracemalloc](tracemalloc-trace-memory-allocations.md)
