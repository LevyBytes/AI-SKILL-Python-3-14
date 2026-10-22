# What's New In Python 3.13 / An experimental just-in-time (JIT) compiler

### An experimental just-in-time (JIT) compiler

If CPython is configured and compiled with the `--enable-experimental-jit` option, a just-in-time (JIT) compiler is included that can accelerate certain Python programs. On Windows, run `PCbuild/build.bat --experimental-jit` to switch on the JIT, or `--experimental-jit-interpreter` to switch on the Tier 2 interpreter. The build prerequisites and additional background [are contained at](https://github.com/python/cpython/blob/main/Tools/jit/README.md) `Tools/jit/README.md`.

The `--enable-experimental-jit` option accepts these (optional) values, falling back to `yes` whenever `--enable-experimental-jit` appears without the optional value.

- `no`: Switch off the whole Tier 2 plus JIT pipeline.

- `yes`: Switch on the JIT. To turn the JIT off while running, supply the environment variable `PYTHON_JIT=0`.

- `yes-off`: Compile the JIT yet leave it off by default. To turn it on while running, supply the environment variable `PYTHON_JIT=1`.

- `interpreter`: Switch on the Tier 2 interpreter yet leave the JIT off. That interpreter can be shut off by launching with `PYTHON_JIT=0`.

Roughly speaking, the internal design works like this:

- We begin with specialized *Tier 1 bytecode*. Consult [What's new in 3.11](https://docs.python.org/3.14/whatsnew/3.11.html#whatsnew311-pep659) for the particulars.

- Once the Tier 1 bytecode becomes sufficiently hot, it is converted into a brand-new, entirely internal intermediate representation (IR) named the *Tier 2 IR*, occasionally called micro-ops (?uops?).

- The Tier 2 IR runs on the same stack-based virtual machine as Tier 1, yet its instruction layout lends itself better to producing machine code.

- Several optimization passes operate over the Tier 2 IR, running before it is either interpreted or turned into machine code.

- A Tier 2 interpreter exists, though it mostly serves to debug the earlier phases of the optimization pipeline. You can switch the Tier 2 interpreter on by configuring Python with `--enable-experimental-jit=interpreter`.

- With the JIT switched on, the optimized Tier 2 IR is turned into machine code, which then runs.

- Producing the machine code relies on a method known as *copy-and-patch*. It carries no runtime dependencies, though a fresh build-time dependency on LLVM is introduced.

See also

[**PEP 744**](https://peps.python.org/pep-0744/)

[Subject index](INDEX.md) · [Previous source section](free-threaded-cpython.md) · [Next source section](defined-mutation-semantics-for-locals.md) · [Release/subject declaration](summary-release-highlights.md)
