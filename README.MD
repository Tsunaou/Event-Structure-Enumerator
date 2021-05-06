# Event-Structure-Enumerator
Implementation for the partial order part of paper [A Verified Algorithm Enumerating Event Structures](https://arxiv.org/pdf/1705.07228.pdf)

## Dependency
- python 3.6+
- numpy

## How to use
The main function is `enumeratePo(N)` in `EnumeratePO.py`, which takes one natural number N as an
argument, and returning a list containing, without repetitions, each possible event
structure over a set of N distinct events.

Now, it supports the calculation for 
- preorder
- strict preorder
- strict partial order 
- partial order 

## Examples
The entries for each relation are tuples. 

The result of `enumeratePo(2)` is
```python
[[(0, 0), (1, 1)], [(0, 0), (1, 0), (1, 1)], [(0, 0), (0, 1), (1, 1)]]
```