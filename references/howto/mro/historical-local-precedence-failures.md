# Historical local-precedence failures

### Bad Method Resolution Orders

A MRO qualifies as *bad* once it violates bedrock properties like local precedence ordering and monotonicity. Over this section I'll demonstrate that the MRO for classic classes and the MRO for new style classes under Python 2.2 are both bad.

Beginning with local precedence ordering is the simpler route. Take the following example:

```python
>>> F=type('Food',(),{'remember2buy':'spam'})
>>> E=type('Eggs',(F,),{'remember2buy':'eggs'})
>>> G=type('GoodFood',(F,E),{}) # under Python 2.3 this is an error!

```

with inheritance diagram

>

```text
             O
             |
(buy spam)   F
             | \
             | E   (buy eggs)
             | /
             G

      (buy eggs or spam ?)

```

Notice that class G derives from F and E, listing F *before* E: on that basis we'd anticipate the attribute *G.remember2buy* picking up its value from *F.remember2buy* rather than from *E.remember2buy* — and yet Python 2.2 produces

```python
>>> G.remember2buy
'eggs'

```

That amounts to a violation of local precedence ordering, because the sequence in the local precedence list — namely G's list of parents — isn't carried over into the Python 2.2 linearization of G:

```python
L[G,P22]= G E F object   # F *follows* E

```

You might contend that F trails E in the Python 2.2 linearization because F is the less specialized of the two, being E's superclass; even so, this violation of local precedence ordering is decidedly counterintuitive and prone to error. That holds all the more given how it diverges from old style classes:

```python
>>> class F: remember2buy='spam'
>>> class E(F): remember2buy='eggs'
>>> class G(F,E): pass
>>> G.remember2buy
'spam'

```

Here the MRO comes out as GFEF and local precedence ordering is kept intact.

As a rule of thumb, hierarchies of the sort just shown are best steered clear of, since whether F ought to override E or the reverse is unclear. Python 2.3 resolves the ambiguity by throwing an exception while class G is being created, which in effect prevents the programmer from producing ambiguous hierarchies. The cause is that the C3 algorithm breaks down once the merge:

```python
merge(FO,EFO,FE)

```

can't be worked out, since F resides in the tail of EFO and E resides in the tail of FE.

[Subject index](INDEX.md) · [Unambiguous hierarchy and duplicate-base rejection](unambiguous-hierarchy-and-duplicate-base-rejection.md) · [Classic and Python 2.2 monotonicity failures](classic-and-python-2-2-monotonicity-failures.md) · [Previous source context](conflicting-base-orders-cannot-be-merged.md) · [Following source context](unambiguous-hierarchy-and-duplicate-base-rejection.md)
