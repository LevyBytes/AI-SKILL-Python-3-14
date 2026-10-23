# statistics - Naive bayesian classifier

### Naive bayesian classifier

Machine learning problems frequently feature normal distributions.

Wikipedia offers a [nice example of a Naive Bayesian Classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Person_classification). The task there is to infer someone's gender from measurements of normally distributed traits such as height, weight, and foot size.

Our training set provides measurements for eight individuals. Treating those measurements as normally distributed, we condense the data using `NormalDist`:

```pycon
>>> height_male = NormalDist.from_samples([6, 5.92, 5.58, 5.92])
>>> height_female = NormalDist.from_samples([5, 5.5, 5.42, 5.75])
>>> weight_male = NormalDist.from_samples([180, 190, 170, 165])
>>> weight_female = NormalDist.from_samples([100, 150, 130, 150])
>>> foot_size_male = NormalDist.from_samples([12, 11, 12, 10])
>>> foot_size_female = NormalDist.from_samples([6, 8, 7, 9])

```

Now along comes another individual whose trait measurements we have, though their gender remains unknown:

```pycon
>>> ht = 6.0        # height
>>> wt = 130        # weight
>>> fs = 8          # foot size

```

Beginning from a 50% [prior probability](https://en.wikipedia.org/wiki/Prior_probability) for either gender, we form the posterior by multiplying that prior with the combined likelihoods of the trait measurements under each gender:

```pycon
>>> prior_male = 0.5
>>> prior_female = 0.5
>>> posterior_male = (prior_male * height_male.pdf(ht) *
...                   weight_male.pdf(wt) * foot_size_male.pdf(fs))

>>> posterior_female = (prior_female * height_female.pdf(ht) *
...                     weight_female.pdf(wt) * foot_size_female.pdf(fs))

```

Whichever posterior turns out largest decides the prediction. People call this the [maximum a posteriori](https://en.wikipedia.org/wiki/Maximum_a_posteriori_estimation), or MAP:

```pycon
>>> 'male' if posterior_male > posterior_female else 'female'
'female'

```

[Subject index](INDEX.md) · [Previous](approximating-binomial-distributions.md) · [Owning module, declaration or section: statistics](statistics-mathematical-statistics-functions.md)
