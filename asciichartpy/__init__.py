# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------

from __future__ import division
from math import ceil, floor

# -----------------------------------------------------------------------------

__all__ = ['plot']

# -----------------------------------------------------------------------------

def plot(series, cfg=None):
    """ Possible cfg parameters are 'minimum', 'maximum', 'offset', 'height' and 'format'.
	cfg is a dictionary, thus dictionary syntax has to be used.
	Example: print(plot(series, { 'height' :10 }))
	"""
    cfg = cfg or {}
    minimum = cfg['minimum'] if 'minimum' in cfg else min(series)
    maximum = cfg['maximum'] if 'maximum' in cfg else max(series)
    if minimum > maximum:
        raise ValueError('The minimum value cannot exceed the maximum value.')

    interval = maximum - minimum
    offset = cfg['offset'] if 'offset' in cfg else 3
    height = cfg['height'] if 'height' in cfg else interval
    ratio = height / interval
    min2 = floor(minimum * ratio)
    max2 = ceil(maximum * ratio)

    rows = max2 - min2
    width = len(series) + offset
    placeholder = cfg['format'] if 'format' in cfg else '{:8.2f} '

    result = [[' '] * width for i in range(rows + 1)]

    # axis and labels
    for y in range(min2, max2 + 1):
        label = placeholder.format(maximum - ((y - min2) * interval / rows))
        result[y - min2][max(offset - len(label), 0)] = label
        result[y - min2][offset - 1] = '┼' if y == 0 else '┤'

    y0 = int(series[0] * ratio - min2)
    result[rows - y0][offset - 1] = '┼' # first value

    for x in range(len(series) - 1): # plot the line
        y0 = round(series[x + 0] * ratio) - min2
        y1 = round(series[x + 1] * ratio) - min2
        if y0 == y1:
            result[rows - y0][x + offset] = '─'
        else:
            result[rows - y1][x + offset] = '╰' if y0 > y1 else '╭'
            result[rows - y0][x + offset] = '╮' if y0 > y1 else '╯'
            start = min(y0, y1) + 1
            end = max(y0, y1)
            for y in range(start, end):
                result[rows - y][x + offset] = '│'

    return '\n'.join([''.join(row) for row in result])
