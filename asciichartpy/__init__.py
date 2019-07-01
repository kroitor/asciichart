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
    height = cfg['height'] if 'height' in cfg else ceil(interval)
    ratio = interval / (height - 1)
    width = len(series) + offset
    placeholder = cfg['format'] if 'format' in cfg else '{:8.2f} '

    result = [[' '] * width for i in range(height)]

    # axis and labels
    for i in range(height):
        label = placeholder.format(minimum + i * ratio)
        result[i][max(offset - len(label), 0)] = label
        result[i][offset - 1] = '┼' if i == 0 else '┤'

    y0 = int((series[0] - minimum) / ratio)
    result[y0][offset - 1] = '┼' # first value

    for i in range(len(series) - 1): # plot the line
        y0 = round((series[i] - minimum) / ratio)
        y1 = round((series[i + 1] - minimum) / ratio)
        if y0 == y1:
            result[y0][i + offset] = '─'
        else:
            result[y1][i + offset] = '╰' if y0 > y1 else '╭'
            result[y0][i + offset] = '╮' if y0 > y1 else '╯'
            start = min(y0, y1) + 1
            end = max(y0, y1)
            for y in range(start, end):
                result[y][i + offset] = '│'

    return '\n'.join([''.join(row) for row in result[::-1]])
