# secrets — Random numbers

### Random numbers

The most secure source of randomness your operating system offers is what the `secrets` module exposes.

 *class *secrets.SystemRandom

A class that generates random numbers from the highest-quality sources the operating system provides. Consult [`random.SystemRandom`](https://docs.python.org/3.14/library/random.html#random.SystemRandom) for more particulars.

 secrets.choice(*seq*)

Return a randomly chosen element from a non-empty sequence.

 secrets.randbelow(*exclusive_upper_bound*)

Return a random int in the range [0, *exclusive_upper_bound*).

 secrets.randbits(*k*)

Return a non-negative int with *k* random bits.

[Subject index](INDEX.md) · [Previous](secrets-generate-secure-random-numbers-for-managing-secrets.md) · [Continue](secrets-token-bytes-to-secrets-token-urlsafe.md) · [Owning module, declaration or section: secrets](secrets-generate-secure-random-numbers-for-managing-secrets.md)
