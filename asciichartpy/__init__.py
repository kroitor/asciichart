# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------

from math import cos
from math import sin
from math import pi
from math import floor
from math import ceil

# -----------------------------------------------------------------------------

__all__ = ['plot']

# -----------------------------------------------------------------------------

def plot(series, cfg={}):

    minimum = min(series)
    maximum = max(series)

    interval = abs(float(maximum) - float(minimum))
    offset = cfg['offset'] if 'offset' in cfg else 3
    padding = cfg['padding'] if 'padding' in cfg else '           '
    height = cfg['height'] if 'height' in cfg else interval
    ratio = height / interval
    intmin = floor(float(minimum) * ratio)
    intmax = ceil(float(maximum) * ratio)

    rows = abs(intmax - intmin)
    width = len(series) + offset
    placeholder = cfg['format'] if 'format' in cfg else '{:8.2f} '

    result = [[' '] * width for i in range(rows + 1)]

    # axis and labels
    for y in range(intmin, intmax + 1):
        label = placeholder.format(float(maximum) - ((y - intmin) * interval / rows))
        result[y - intmin][max(offset - len(label), 0)] = label
        result[y - intmin][offset - 1] = '┼' if y == 0 else '┤'

    y0 = int(series[0] * ratio - intmin)
    result[rows - y0][offset - 1] = '┼' # first value

    for x in range(0, len(series) - 1): # plot the line
        y0 = int(round(series[x + 0] * ratio) - intmin)
        y1 = int(round(series[x + 1] * ratio) - intmin)
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
