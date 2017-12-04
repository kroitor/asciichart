"use strict";

var asciichart = require ('./asciichart')

var width = 60
var line = "\n" + '='.repeat (width + 9) + "\n"

console.log ("\nbasic\n")

var s0 = new Array (width)
for (var i = 0; i < s0.length; i++)
    s0[i] = 15 * Math.sin (i * ((Math.PI * 4) / s0.length))
console.log (asciichart.plot (s0))

console.log (line)
console.log ("configuring / scale to desired height\n")

var config = {
    offset:  3,  // axis offset from the left (min 2)
    height:  10, // any height you want
    format: function (x, i) {
        return ('       ' + x.toFixed (2)).slice (-'       '.length)
    }
}

var s = []
for (var i = 0; i < width; i++)
    s[i] = 15 * Math.cos (i * ((Math.PI * 8) / width)) // values range from -15 to +15
console.log (asciichart.plot (s, config))     // this rescales the graph to ±3 lines

console.log (line)
console.log ("auto-range\n")

var s2 = new Array (width)
s2[0] = Math.round (Math.random () * 15)
for (i = 1; i < s2.length; i++)
    s2[i] = s2[i - 1] + Math.round (Math.random () * (Math.random () > 0.5 ? 2 : -2))
console.log (asciichart.plot (s2) + "\n")

console.log (line)
console.log ("\ncorrect padding for widely varying label lengths\n")

console.log ("\nrange 8000 - 12000\n")
var s3 = []
for (var i = 0; i < width; i++)
    s3[i] = (2000 * Math.cos (i * ((Math.PI * 8) / width))) + 10000 // values range from 9000 to 11000
console.log (asciichart.plot (s3, { height: 10, width: 60 }))

console.log ("\nrange 0.000080 - 0.00012\n")
s3 = s3.map(x => { return x / 100000000 })
console.log (asciichart.plot (s3, { height: 10, width: 60 }))