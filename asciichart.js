"use strict";

(function (exports) {

    // your code goes here

    exports.plot = function (series, cfg) {

        var min = series[0]
        var max = series[0]

        for (var i = 1; i < series.length; i++) {
            min = Math.min (min, series[i])
            max = Math.max (max, series[i])
        }

        var range   = Math.abs (max - min)
        var cfg     = (typeof cfg !== 'undefined') ? cfg : {}
        var offset  = (typeof cfg.offset  !== 'undefined') ? cfg.offset  : 3
        var padding = (typeof cfg.padding !== 'undefined') ? cfg.padding : '       '
        var height  = (typeof cfg.height  !== 'undefined') ? cfg.height  : range
        var ratio   = height / range
        var min2    = Math.round (min * ratio)
        var max2    = Math.round (max * ratio)
        var rows    = Math.abs (max2 - min2)
        var width   = series.length + offset
        var format  = (typeof cfg.format != 'undefined') ? cfg.format : function (n) {
            return (padding + String (n.toFixed (2))).slice (-padding.length)
        }

        var result = new Array (rows + 1) // empty space
        for (var i = 0; i <= rows; i++) {
            result[i] = new Array (width)
            for (var j = 0; j < width; j++)
                result[i][j] = ' '
        }

        for (var y = min2; y <= max2; ++y) { // axis + labels
            var label = max - (y - min2) * range / rows
            var labelString = format (label)
            result[y - min2][Math.max (offset - labelString.length, 0)] = labelString
            result[y - min2][offset - 1] = (y == 0) ? '┼' : '┤' 
        }

        var y0 = Math.round (series[0] * ratio) - min2
        result[rows - y0][offset - 1] = '┼' // first value

        for (var x = 0; x < series.length - 1; x++) { // plot the line
            var y0 = Math.round (series[x + 0] * ratio) - min2
            var y1 = Math.round (series[x + 1] * ratio) - min2
            if (y0 == y1)
                result[rows - y0][x + offset] = '─'
            else {                        
                result[rows - y1][x + offset] = (y0 > y1) ? '╰' : '╭'
                result[rows - y0][x + offset] = (y0 > y1) ? '╮' : '╯'
                var from = Math.min (y0, y1)
                var to = Math.max (y0, y1)
                for (var y = from + 1; y < to; y++)
                    result[rows - y][x + offset] = '│'
            }
        }

        return result.map (function (x) { return x.join ('') }).join ('\n')
    }  

}) (typeof exports === 'undefined' ? this['asciichart'] = {} : exports);