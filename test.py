# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------

from math import cos, nan, pi

# ------------------------------------------------------------------------------

from asciichartpy import plot

# ------------------------------------------------------------------------------

width = 90
series = [7 * round(cos(i * ((pi * 4) / width)), 2) for i in range(width)]

print(plot(series))

series = [2.0] * width

print()
print(plot(series))
print()
print(plot(series, {'height':5}))

series = [0.0] * width

print()
print(plot(series))
print()
print(plot(series, {'height':5}))

print()
graph = plot([-1, 0, 2])
print(graph)
assert ' 1.00  ┼' not in graph
assert ' 0.00  ┼' in graph

print()
graph = plot([nan, 2, 3])
print(graph)
assert '┼' not in graph
