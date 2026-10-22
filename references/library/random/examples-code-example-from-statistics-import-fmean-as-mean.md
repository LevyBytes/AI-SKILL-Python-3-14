# random — Examples — Code example: from statistics import fmean as mean

```python
# Example from "Statistics is Easy" by Dennis Shasha and Manda Wilson
from statistics import fmean as mean
from random import shuffle

drug = [54, 73, 53, 70, 73, 68, 52, 65, 65]
placebo = [54, 51, 58, 44, 55, 52, 42, 47, 58, 46]
observed_diff = mean(drug) - mean(placebo)

n = 10_000
count = 0
combined = drug + placebo
for i in range(n):
    shuffle(combined)
    new_diff = mean(combined[:len(drug)]) - mean(combined[len(drug):])
    count += (new_diff >= observed_diff)

print(f'{n} label reshufflings produced only {count} instances with a difference')
print(f'at least as extreme as the observed difference of {observed_diff:.1f}.')
print(f'The one-sided p-value of {count / n:.4f} leads us to reject the null')
print(f'hypothesis that there is no difference between the drug and the placebo.')

```

Simulation of arrival times and service deliveries for a multiserver queue:

```python
from heapq import heapify, heapreplace
from random import expovariate, gauss
from statistics import mean, quantiles

average_arrival_interval = 5.6
average_service_time = 15.0
stdev_service_time = 3.5
num_servers = 3

waits = []
arrival_time = 0.0
servers = [0.0] * num_servers  # time when each server becomes available
heapify(servers)
for i in range(1_000_000):
    arrival_time += expovariate(1.0 / average_arrival_interval)
    next_server_available = servers[0]
    wait = max(0.0, next_server_available - arrival_time)
    waits.append(wait)
    service_duration = max(0.0, gauss(average_service_time, stdev_service_time))
    service_completed = arrival_time + wait + service_duration
    heapreplace(servers, service_completed)

print(f'Mean wait: {mean(waits):.1f}   Max wait: {max(waits):.1f}')
print('Quartiles:', [round(q, 1) for q in quantiles(waits)])

```

See also

[Statistics for Hackers](https://www.youtube.com/watch?v=Iq9DzN6mvYA), a video walkthrough by [Jake Vanderplas](https://us.pycon.org/2016/speaker/profile/295/), tackles statistical analysis with only a handful of core ideas: simulation, sampling, shuffling, and cross-validation.

[Economics Simulation](https://nbviewer.org/url/norvig.com/ipython/Economics.ipynb), a marketplace model by [Peter Norvig](https://norvig.com/bio.html), demonstrates putting many of this module's tools and distributions to good use (gauss, uniform, sample, betavariate, choice, triangular, and randrange).

[A Concrete Introduction to Probability (using Python)](https://nbviewer.org/url/norvig.com/ipython/Probability.ipynb), a tutorial from [Peter Norvig](https://norvig.com/bio.html), walks through the fundamentals of probability theory, writing simulations, and carrying out data analysis in Python.

[Subject index](INDEX.md) · [Previous](examples-section-introduction-and-initial-examples.md) · [Continue](recipes.md) · [Owning module, declaration or section: random](random-generate-pseudo-random-numbers.md) · [Owning module, declaration or section: Examples](examples-section-introduction-and-initial-examples.md)
