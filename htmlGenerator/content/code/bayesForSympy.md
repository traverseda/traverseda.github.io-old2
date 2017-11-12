```yaml
created: '2017-11-12T16:20:54.593134+00:00'
published: true
tags: [home, code]
updated: '2017-11-12T16:20:54.593150+00:00'

```
---
#Bayes-theorem probability object for sympy

This is a quick hack I did to support adding probabilities together using sympy,
which is symbolic mathematics for python. Since the objects represent an
equation, you can represent things like `p(1/3)+p(1/4)` without floating point
errors. When not interacting with another probability, they're treated as
ordinary sympy numbers.

```python
from sympy import S
from wrapt import ObjectProxy

"""
A class for quickly doing math on percentages,
using bayes theorum.

We use object proxying because we don't know what type
of number the underlying probability is. Although
probably we could just treat it as a rational number.

Still, as an object proxy we can use PI as a probability,
or inifinity, or whatever. Any type of number can
be treated like a probability.

It's surprisngly performant, but if you get performance
issues you might try replacing `ObjectProxy` with `S.rational`
and removing the init method.
"""

one = S(1)

class Probability(ObjectProxy):
    """
    A percentage object, you can use it to properly
    add or subtract percentage from one another.
    When used with a regular number, acts like
    a regular number.
    """
    def __init__(self,wrapped):
        super().__init__(S(wrapped))

    def __add__(self,other):
        if isinstance(other, Probability):
            return Probability(self+(one-self)*other)
        return super().__add__(other)
    def __sub__(self,other):
        if isinstance(other, Probability):
            return Probability(self-self*other)
        return super().__sub__(other)

p = Probability

print(float(p("1/3")+p("1/4")+p(0.5))) #0.75
```
