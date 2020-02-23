# -*- coding: utf-8 -*-
"""Module to generate ascii charts.

This module provides a single function `plot` that can be used to generate an
ascii chart from a series of numbers. The chart can be configured via several
options to tune the output.
"""

from __future__ import division
from math import ceil, floor, isnan

__all__ = ['plot']

# Python 3.2 has math.isfinite, which could have been used, but to support older
# versions, this little helper is shorter than having to keep doing not isnan(),
# plus the double-negative of "not is not a number" is confusing, so this should
# help with readability.
def _isnum(n):
    return not isnan(n)

def plot(series, cfg=None):
    """Generate an ascii chart for a series of numbers.

    `series` should be a list of ints or floats. Missing data values in the
    series can be specified as a NaN. In Python versions less than 3.5, use
    float("nan") to specify an NaN. With 3.5 onwards, use math.nan to specify a
    NaN.

        >>> series = [1,2,3,4,float("nan"),4,3,2,1]
        >>> print(asciichartpy.plot(series))
        4.00  ┤  ╭╴╶╮   
        3.00  ┤ ╭╯  ╰╮  
        2.00  ┤╭╯    ╰╮ 
        1.00  ┼╯      ╰ 
    
    `cfg` is an optional dictionary of various parameters to tune the appearance
    of the chart. `minimum` and `maximum` will clamp the y-axis and all values:

        >>> series = [1,2,3,4,float("nan"),4,3,2,1]
        >>> print(asciichartpy.plot(series, {'minimum': 0}))
        4.00  ┼  ╭╴╶╮   
        3.00  ┤ ╭╯  ╰╮  
        2.00  ┤╭╯    ╰╮ 
        1.00  ┼╯      ╰ 
        0.00  ┤         

        >>> print(asciichartpy.plot(series, {'minimum': 2}))
        4.00  ┤  ╭╴╶╮   
        3.00  ┤ ╭╯  ╰╮  
        2.00  ┼─╯    ╰─ 

        >>> print(asciichartpy.plot(series, {'minimum': 2, 'maximum': 3}))
        3.00  ┤ ╭─╴╶─╮  
        2.00  ┼─╯    ╰─ 

    `height` specifies the number of rows the graph should occupy. It can be
    used to scale down a graph with large data values:

        >>> series = [10,20,30,40,50,40,30,20,10]
        >>> print(asciichartpy.plot(series, {'height': 4}))
        50.00  ┤   ╭╮    
        40.00  ┤  ╭╯╰╮   
        30.00  ┤ ╭╯  ╰╮  
        20.00  ┤╭╯    ╰╮ 
        10.00  ┼╯      ╰ 

    `format` specifies a Python format string used to format the labels on the
    y-axis. The default value is "{:8.2f} ". This can be used to remove the
    decimal point:

        >>> series = [10,20,30,40,50,40,30,20,10]
        >>> print(asciichartpy.plot(series, {'height': 4, 'format':'{:8.0f} '}))
        40  ┼  ╭╮  
        30  ┤  │╰╮ 
        20  ┤ ╭╯ │ 
        10  ┼╮│  ╰ 
         0  ┤╰╯    
        >>> 
	"""
    if not series or all(isnan(n) for n in series):
        return ''

    cfg = cfg or {}
    minimum = cfg['minimum'] if 'minimum' in cfg else min(filter(_isnum, series))
    maximum = cfg['maximum'] if 'maximum' in cfg else max(filter(_isnum, series))

    if minimum > maximum:
        raise ValueError('The minimum value cannot exceed the maximum value.')

    interval = maximum - minimum
    offset = cfg['offset'] if 'offset' in cfg else 3
    height = cfg['height'] if 'height' in cfg else interval
    ratio = height / interval

    min2 = floor(minimum * ratio)
    max2 = ceil(maximum * ratio)

    def clamp(n):
        return min(max(n, minimum), maximum)

    def scaled(y):
        return round(clamp(y) * ratio) - min2

    rows = max2 - min2
    width = len(series) + offset
    placeholder = cfg['format'] if 'format' in cfg else '{:8.2f} '

    result = [[' '] * width for i in range(rows + 1)]

    # axis and labels
    for y in range(min2, max2 + 1):
        label = placeholder.format(maximum - ((y - min2) * interval / rows))
        result[y - min2][max(offset - len(label), 0)] = label
        result[y - min2][offset - 1] = '┼' if y == 0 else '┤'

    # first value is a tick mark across the y-axis
    d0 = series[0]
    if _isnum(d0):
        result[rows - scaled(d0)][offset - 1] = '┼'

    # plot the line
    for x in range(len(series) - 1):
        d0 = series[x + 0]
        d1 = series[x + 1]

        if isnan(d0) and isnan(d1):
            continue

        if isnan(d0) and _isnum(d1):
            result[rows - scaled(d1)][x + offset] = '╶'
            continue

        if _isnum(d0) and isnan(d1):
            result[rows - scaled(d0)][x + offset] = '╴'
            continue

        y0 = scaled(d0)
        y1 = scaled(d1)
        if y0 == y1:
            result[rows - y0][x + offset] = '─'
            continue

        result[rows - y1][x + offset] = '╰' if y0 > y1 else '╭'
        result[rows - y0][x + offset] = '╮' if y0 > y1 else '╯'

        start = min(y0, y1) + 1
        end = max(y0, y1)
        for y in range(start, end):
            result[rows - y][x + offset] = '│'

    return '\n'.join([''.join(row) for row in result])
