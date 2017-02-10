# asciichart
Console ASCII line charts in 50 lines of pure Javascript (for NodeJS and browsers) with no dependencies.

<img width="789" alt="Console ASCII Line charts in pure Javascript (for NodeJS and browsers)" src="https://cloud.githubusercontent.com/assets/1294454/22818709/9f14e1c2-ef7f-11e6-978f-34b5b595fb63.png">

## NodeJS

```javascript
var asciichart = require('./asciichart')
var s0 = new Array (120)
for (var i = 0; i < s0.length; i++)
    s0[i] = 15 * Math.sin (i * ((Math.PI * 4) / s0.length))
console.log (asciichart.plot (s0))
```

## Browsers

```html
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta charset="UTF-8">
        <title>asciichart</title>
        <script src="asciichart.js"></script>
        <script type="text/javascript">
            var s0 = new Array (120)
            for (var i = 0; i < s0.length; i++)
                s0[i] = 15 * Math.sin (i * ((Math.PI * 4) / s0.length))
            console.log (asciichart.plot (s0))
        </script>
    </head>
    <body>
    </body>
</html>
```

## Basic Usage

The width of the chart will alwaays equal the length of data series. The height and range are determined automatically.

```javascript
var s0 = new Array (120)
for (var i = 0; i < s0.length; i++)
    s0[i] = 15 * Math.sin (i * ((Math.PI * 4) / s0.length))
console.log (asciichart.plot (s0))
```

<img width="788" alt="Console ASCII Line charts in pure Javascript (for NodeJS and browsers)" src="https://cloud.githubusercontent.com/assets/1294454/22818807/313cd636-ef80-11e6-9d1a-7a90abdb38c8.png">

The output can be configured by passing a second parameter to the `plot (series, config)` function. The following options are supported:
```
var config = {

    offset:  3,          // axis offset (min 2)
    padding: '       ',  // padding string
    height:  10,         // any height you want

    // the label format function
    format:  function (n) { return (padding + String (n.toFixed (2))).slice (-padding.length) }
}
```

## Rescale To Desired Height

To rescale 
```javascript
var s = []
for (var i = 0; i < 120; i++)
    s[i] = 15 * Math.cos (i * ((Math.PI * 8) / 120))
console.log (asciichart.plot (s, { height: 6 }))
```

<img width="791" alt="Console ASCII Line charts in pure Javascript (for NodeJS and browsers)" src="https://cloud.githubusercontent.com/assets/1294454/22818711/9f166128-ef7f-11e6-9748-b23b151974ed.png">

### Auto-range

```javascript
var s2 = new Array (120)
s2[0] = Math.round (Math.random () * 15)
for (i = 1; i < s2.length; i++)
    s2[i] = s2[i - 1] + Math.round (Math.random () * (Math.random () > 0.5 ? 2 : -2))
console.log (asciichart.plot (s2))
```

<img width="788" alt="Console ASCII Line charts in pure Javascript (for NodeJS and browsers)" src="https://cloud.githubusercontent.com/assets/1294454/22818710/9f157a74-ef7f-11e6-893a-f7494b5abef1.png">









