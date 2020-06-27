Title: Python Cheatsheet
Date: 2020-01-07 11:15
Modified: 2020-01-07 11:15
Category: Programming
Tags: python
Slug: python-cheatsheet
Authors: Sangwoong Yoon
Summary: Python Cheatsheet

# Python Cheatsheet

Useful hacks and tips for Python.


## Concatenating lists in a list

See: https://stackoverflow.com/a/716482/2978409

```python
>>> import itertools
>>> l = [[1, 2], [3]]
>>> list(itertools.chain(*l))
[1, 2, 3]
>>> list(itertools.chain.from_iterable(l))
[1, 2, 3]
```
