# SPDX-License-Identifier: MIT
# Modifications Copyright (c) Microsoft.
#
# Copyright © 2016 Igor Kroitor
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Module to generate ascii charts.

This module provides a single function `plot` that can be used to generate an
ascii chart from a series of numbers. The chart can be configured via several
options to tune the output.
"""

from __future__ import annotations

from math import ceil, floor, isnan
from typing import Mapping

black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
lightgray = "\033[37m"
default = "\033[39m"
darkgray = "\033[90m"
lightred = "\033[91m"
lightgreen = "\033[92m"
lightyellow = "\033[93m"
lightblue = "\033[94m"
lightmagenta = "\033[95m"
lightcyan = "\033[96m"
white = "\033[97m"
reset = "\033[0m"


__all__ = [
    "plot",
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "lightgray",
    "default",
    "darkgray",
    "lightred",
    "lightgreen",
    "lightyellow",
    "lightblue",
    "lightmagenta",
    "lightcyan",
    "white",
    "reset",
]


# Python 3.2 has math.isfinite, which could have been used, but to support older
# versions, this little helper is shorter than having to keep doing not isnan(),
# plus the double-negative of "not is not a number" is confusing, so this should
# help with readability.
def _isnum(n):
    return not isnan(n)


def colored(char, color):
    if not color:
        return char
    else:
        return color + char + reset


_DEFAULT_SYMBOLS = ("┼", "┤", "╶", "╴", "─", "╰", "╭", "╮", "╯", "│")


def plot(series, bin_edges=None, cfg=None):
    """Generate an ascii chart for a series of numbers.

    `series` should be a list of ints or floats. Missing data values in the
    series can be specified as a NaN. In Python versions less than 3.5, use
    float("nan") to specify an NaN. With 3.5 onwards, use math.nan to specify a
    NaN.

        >>> series = [1,2,3,4,float("nan"),4,3,2,1]
        >>> print(plot(series))
            4.00  ┤  ╭╴╶╮
            3.00  ┤ ╭╯  ╰╮
            2.00  ┤╭╯    ╰╮
            1.00  ┼╯      ╰

    `series` can also be a list of lists to support multiple data series.

        >>> series = [[10,20,30,40,30,20,10], [40,30,20,10,20,30,40]]
        >>> print(plot(series, {'height': 3}))
            40.00  ┤╮ ╭╮ ╭
            30.00  ┤╰╮╯╰╭╯
            20.00  ┤╭╰╮╭╯╮
            10.00  ┼╯ ╰╯ ╰

    `bin_edges` is an optional list of bin edges to display on the x-axis. If
    provided, the x-axis will be labeled with the bin edges. If there are too
    many bin edges to fit on the x-axis, some labels will be dropped and they
    will be spaced out evenly to fit the width of the chart.
    The labels will be formatted using the `x_format` option in `cfg`.

    `cfg` is an optional dictionary of various parameters to tune the appearance
    of the chart. `min` and `max` will clamp the y-axis and all values:

        >>> series = [1,2,3,4,float("nan"),4,3,2,1]
        >>> print(plot(series, {'min': 0}))
            4.00  ┼  ╭╴╶╮
            3.00  ┤ ╭╯  ╰╮
            2.00  ┤╭╯    ╰╮
            1.00  ┼╯      ╰
            0.00  ┤

        >>> print(plot(series, {'min': 2}))
            4.00  ┤  ╭╴╶╮
            3.00  ┤ ╭╯  ╰╮
            2.00  ┼─╯    ╰─

        >>> print(plot(series, {'min': 2, 'max': 3}))
            3.00  ┤ ╭─╴╶─╮
            2.00  ┼─╯    ╰─

    `height` specifies the number of rows the graph should occupy. It can be
    used to scale down a graph with large data values:

        >>> series = [10,20,30,40,50,40,30,20,10]
        >>> print(plot(series, {'height': 4}))
            50.00  ┤   ╭╮
            40.00  ┤  ╭╯╰╮
            30.00  ┤ ╭╯  ╰╮
            20.00  ┤╭╯    ╰╮
            10.00  ┼╯      ╰

    `format` specifies a Python format string used to format the labels on the
    y-axis. The default value is "{:8.2f} ". This can be used to remove the
    decimal point:

        >>> series = [10,20,30,40,50,40,30,20,10]
        >>> print(plot(series, {'height': 4, 'format':'{:8.0f}'}))
            50 ┤   ╭╮
            40 ┤  ╭╯╰╮
            30 ┤ ╭╯  ╰╮
            20 ┤╭╯    ╰╮
            10 ┼╯      ╰
    """
    if len(series) == 0:
        return ""

    if not isinstance(series[0], list):
        if all(isnan(n) for n in series):
            return ""
        else:
            series = [series]

    if cfg is not None and not isinstance(cfg, Mapping):
        raise TypeError("cfg must be a dictionary or None")

    cfg = cfg or {}

    colors = cfg.get("colors", [None])

    minimum = cfg.get("min", min(filter(_isnum, [j for i in series for j in i])))
    maximum = cfg.get("max", max(filter(_isnum, [j for i in series for j in i])))

    symbols = cfg.get("symbols", _DEFAULT_SYMBOLS)

    if minimum > maximum:
        raise ValueError("The min value cannot exceed the max value.")

    interval = maximum - minimum
    offset = cfg.get("offset", 3)
    height = cfg.get("height", interval)
    ratio = height / interval if interval > 0 else 1

    min2 = int(floor(minimum * ratio))
    max2 = int(ceil(maximum * ratio))

    def clamp(n):
        return min(max(n, minimum), maximum)

    def scaled(y):
        return int(round(clamp(y) * ratio) - min2)

    rows = max2 - min2

    width = 0
    for series_i in series:
        width = max(width, len(series_i))
    width += offset

    placeholder = cfg.get("format", "{:8.2f} ")
    x_placeholder = cfg.get("x_format", "{:4.4f}")

    result = [[" "] * width for i in range(rows + 1)]

    # axis and labels
    for y in range(min2, max2 + 1):
        label = placeholder.format(
            maximum - ((y - min2) * interval / (rows if rows else 1))
        )
        result[y - min2][max(offset - len(label), 0)] = label
        result[y - min2][offset - 1] = (
            symbols[0] if y == 0 else symbols[1]
        )  # zero tick mark

    # first value is a tick mark across the y-axis
    d0 = series[0][0]
    if _isnum(d0):
        result[rows - scaled(d0)][offset - 1] = symbols[0]

    for i, series_i in enumerate(series):
        color = colors[i % len(colors)]

        # plot the line
        for x in range(len(series_i) - 1):
            d0 = series_i[x + 0]
            d1 = series_i[x + 1]

            if isnan(d0) and isnan(d1):
                continue

            if isnan(d0) and _isnum(d1):
                result[rows - scaled(d1)][x + offset] = colored(symbols[2], color)
                continue

            if _isnum(d0) and isnan(d1):
                result[rows - scaled(d0)][x + offset] = colored(symbols[3], color)
                continue

            y0 = scaled(d0)
            y1 = scaled(d1)
            if y0 == y1:
                result[rows - y0][x + offset] = colored(symbols[4], color)
                continue

            result[rows - y1][x + offset] = (
                colored(symbols[5], color) if y0 > y1 else colored(symbols[6], color)
            )
            result[rows - y0][x + offset] = (
                colored(symbols[7], color) if y0 > y1 else colored(symbols[8], color)
            )

            start = min(y0, y1) + 1
            end = max(y0, y1)
            for y in range(start, end):
                result[rows - y][x + offset] = colored(symbols[9], color)

    the_plot = "\n".join(["".join(row).rstrip() for row in result])

    if bin_edges is None or len(bin_edges) == 0:
        return the_plot

    # Plot x axis labels
    current_location = 0
    # Compute the amount of leading space for the first x-label using the old label size
    leading_space = offset + len(label)
    # Obtain the first x-label to compute its size
    x_label = x_placeholder.format(bin_edges[0])
    # Initialize the x-label text with the leading space. We allow the first label to
    # recess so that the center of it is aligned with the first tick mark.
    x_label_size = len(x_label)
    x_leading_space = max(0, leading_space - x_label_size)

    x_labels = []
    # This is the amount of space we have to fit the x-labels. It can overflow the width
    # by half of the x-label size
    workable_width = width + x_label_size // 2
    # Compute the spacing between x-labels
    # If we fit labels and space them by 2 characters, we can fit this many labels:
    min_spacing = 2
    num_labels_can_fit = width // (x_label_size + min_spacing)
    labels_count = len(bin_edges)
    # Find out the actual number of labels we need to display
    num_labels_to_display = min(labels_count, num_labels_can_fit)
    num_spaces = num_labels_to_display - 1
    spacing = max(
        min_spacing,
        (workable_width - num_labels_to_display * x_label_size) // num_spaces,
    )
    # Now start placing labels
    while current_location < workable_width:
        # Find the current label that would be suitable for the current location
        bin_index = int((current_location / workable_width) * labels_count)
        x_label = x_placeholder.format(bin_edges[bin_index])
        x_labels.append(x_label)
        # Move to the next location
        current_location += len(x_label) + spacing
    # Create the x-label row
    x_labels_text = " " * x_leading_space + (" " * spacing).join(x_labels)

    return the_plot + "\n" + x_labels_text
