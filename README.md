# asciichart

[![npm](https://img.shields.io/npm/v/asciichart.svg)](https://npmjs.com/package/asciichart) [![PyPI](https://img.shields.io/pypi/v/asciichartpy.svg)](https://pypi.python.org/pypi/asciichartpy) [![Coverage Status](https://coveralls.io/repos/github/kroitor/asciichart/badge.svg?branch=master)](https://coveralls.io/github/kroitor/asciichart?branch=master) [![license](https://img.shields.io/github/license/kroitor/asciichart.svg)](https://github.com/kroitor/asciichart/blob/master/LICENSE.txt)

Console ASCII line charts in pure Javascript (for NodeJS and browsers) with no dependencies.

<img width="789" alt="Console ASCII Line charts in pure Javascript (for NodeJS and browsers)" src="https://cloud.githubusercontent.com/assets/1294454/22818709/9f14e1c2-ef7f-11e6-978f-34b5b595fb63.png">

## Usage

### NodeJS

```sh
npm install asciichart
```

```javascript
var asciichart = require ('asciichart')
var s0 = new Array (120)
for (var i = 0; i < s0.length; i++)
    s0[i] = 15 * Math.sin (i * ((Math.PI * 4) / s0.length))
console.log (asciichart.plot (s0))
```

### Browsers

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

### Options

The width of the chart will always equal the length of data series. The height and range are determined automatically.

```javascript
var s0 = new Array (120)
for (var i = 0; i < s0.length; i++)
    s0[i] = 15 * Math.sin (i * ((Math.PI * 4) / s0.length))
console.log (asciichart.plot (s0))
```

<img width="788" alt="Console ASCII Line charts in pure Javascript (for NodeJS and browsers)" src="https://cloud.githubusercontent.com/assets/1294454/22818807/313cd636-ef80-11e6-9d1a-7a90abdb38c8.png">

The output can be configured by passing a second parameter to the `plot (series, config)` function. The following options are supported:
```javascript
var config = {

    offset:  3,          // axis offset from the left (min 2)
    padding: '       ',  // padding string for label formatting (can be overridden)
    height:  10,         // any height you want

    // the label format function applies default padding
    format:  function (x, i) { return (padding + x.toFixed (2)).slice (-padding.length) }
}
```

### Scale To Desired Height

<img width="791" alt="Console ASCII Line charts in pure Javascript (for NodeJS and browsers)" src="https://cloud.githubusercontent.com/assets/1294454/22818711/9f166128-ef7f-11e6-9748-b23b151974ed.png">

```javascript
var s = []
for (var i = 0; i < 120; i++)
    s[i] = 15 * Math.cos (i * ((Math.PI * 8) / 120)) // values range from -15 to +15
console.log (asciichart.plot (s, { height: 6 }))     // this rescales the graph to ±3 lines
```

<img width="787" alt="Console ASCII Line charts in pure Javascript (for NodeJS and browsers)" src="https://cloud.githubusercontent.com/assets/1294454/22825525/dd295294-ef9e-11e6-93d1-0beb80b93133.png">

### Auto-range

```javascript
var s2 = new Array (120)
s2[0] = Math.round (Math.random () * 15)
for (i = 1; i < s2.length; i++)
    s2[i] = s2[i - 1] + Math.round (Math.random () * (Math.random () > 0.5 ? 2 : -2))
console.log (asciichart.plot (s2))
```

<img width="788" alt="Console ASCII Line charts in pure Javascript (for NodeJS and browsers)" src="https://cloud.githubusercontent.com/assets/1294454/22818710/9f157a74-ef7f-11e6-893a-f7494b5abef1.png">

### Multiple Series

```javascript
var s2 = new Array (120)
s2[0] = Math.round (Math.random () * 15)
for (i = 1; i < s2.length; i++)
    s2[i] = s2[i - 1] + Math.round (Math.random () * (Math.random () > 0.5 ? 2 : -2))

var s3 = new Array (120)
s3[0] = Math.round (Math.random () * 15)
for (i = 1; i < s3.length; i++)
    s3[i] = s3[i - 1] + Math.round (Math.random () * (Math.random () > 0.5 ? 2 : -2))

console.log (asciichart.plot ([ s2, s3 ]))
```

<img width="788" alt="Console ASCII Line charts in pure Javascript (for NodeJS and browsers)" src="https://user-images.githubusercontent.com/27967284/79398277-5322da80-7f91-11ea-8da8-e47976b76c12.png">

### Colors

```javascript
var arr1 = new Array (120)
arr1[0] = Math.round (Math.random () * 15)
for (i = 1; i < arr1.length; i++)
    arr1[i] = arr1[i - 1] + Math.round (Math.random () * (Math.random () > 0.5 ? 2 : -2))

var arr2 = new Array (120)
arr2[0] = Math.round (Math.random () * 15)
for (i = 1; i < arr2.length; i++)
    arr2[i] = arr2[i - 1] + Math.round (Math.random () * (Math.random () > 0.5 ? 2 : -2))

var arr3 = new Array (120)
arr3[0] = Math.round (Math.random () * 15)
for (i = 1; i < arr3.length; i++)
    arr3[i] = arr3[i - 1] + Math.round (Math.random () * (Math.random () > 0.5 ? 2 : -2))

var arr4 = new Array (120)
arr4[0] = Math.round (Math.random () * 15)
for (i = 1; i < arr4.length; i++)
    arr4[i] = arr4[i - 1] + Math.round (Math.random () * (Math.random () > 0.5 ? 2 : -2))

var config = {
    colors: [
        asciichart.blue,
        asciichart.green,
        asciichart.default, // default color
        undefined, // equivalent to default
    ]
}

console.log (asciichart.plot([ arr1, arr2, arr3, arr4 ], config))
```

<img width="788" alt="Console ASCII Line charts in pure Javascript (for NodeJS and browsers)" src="https://user-images.githubusercontent.com/27967284/79398700-51a5e200-7f92-11ea-9048-8dbdeeb60830.png">

### See Also

A util by [madnight](https://github.com/madnight) for drawing Bitcoin/Ether/altcoin charts in command-line console: [bitcoin-chart-cli](https://github.com/madnight/bitcoin-chart-cli).

![bitcoin-chart-cli](https://camo.githubusercontent.com/494806efd925c4cd56d8370c1d4e8b751812030a/68747470733a2f2f692e696d6775722e636f6d2f635474467879362e706e67)

### Ports

Special thx to all who helped port it to other languages, great stuff!

- [Python port](https://pypi.org/project/asciichartpy) included!
- Java: [ASCIIGraph](https://github.com/MitchTalmadge/ASCIIGraph), ported by [MitchTalmadge](https://github.com/MitchTalmadge). If you're a Java-person, check it out!
- Go: [asciigraph](https://github.com/guptarohit/asciigraph), ported by [guptarohit](https://github.com/guptarohit), Go people! )
- Haskell: [asciichart](https://github.com/madnight/asciichart), ported by [madnight](https://github.com/madnight) to Haskell world!
- Ruby: [ascii_chart](https://github.com/zhustec/ascii_chart), ported by [zhustec](https://github.com/zhustec)!
- Elixir: [asciichart](https://github.com/sndnv/asciichart), ported by [sndv](https://github.com/sndnv)!
- Perl: [App::AsciiChart](https://github.com/vti/app-asciichart), ported by [vti](https://github.com/vti)!
- C: [plot](https://github.com/annacrombie/plot), ported by [annacrombie](https://github.com/annacrombie)!
- C++: [asciichart](https://github.com/Civitasv/asciichart), ported by [Civitasv](https://github.com/Civitasv)!
- R: [asciichartr](https://github.com/blmayer/asciichartr), ported by [blmayer](https://github.com/blmayer)!
- Rust: [rasciigraph](https://github.com/orhanbalci/rasciigraph), ported by [orhanbalci](https://github.com/orhanbalci)!
- PHP: [PHP-colored-ascii-linechart](https://github.com/noximo/PHP-colored-ascii-linechart), ported by [noximo](https://github.com/noximo)!
- C#: [asciichart-sharp](https://github.com/NathanBaulch/asciichart-sharp), ported by [samcarton](https://github.com/samcarton), maintained by [NathanBaulch](https://github.com/NathanBaulch)!
- Deno: [chart](https://github.com/maximousblk/chart), ported by [maximousblk](https://github.com/maximousblk)!
- Lua: [lua-asciichart](https://github.com/wuyudi/lua-asciichart), ported by [wuyudi](https://github.com/wuyudi)!
- Dart: [ascii_chart](https://github.com/rave98/ascii_chart), ported by [Rave98](https://github.com/rave98)!
- Mojo: [mojo-asciichart](https://github.com/DataBooth/mojo-asciichart), ported by [Mjboothaus](https://github.com/Mjboothaus)!

### Future work (coming soon, hopefully)

- levels and points on the graph!
- even better value formatting and auto-scaling!

![preview](https://user-images.githubusercontent.com/1294454/31798504-ca2af4cc-b53c-11e7-946c-620d744f6d16.gif)



## 🌐 Web Resources & Interactive Index
- [CROWD BATTLE GUN RUSH](https://ilearnworldpt.pages.dev/crowd-battle-gun-rush.html)
- [CATEGORY CARE](https://themindzone.pages.dev/category-care.html)
- [SLENDERMAN BACK TO SCHOOL](https://learnquester.github.io/slenderman-back-to-school.html)
- [BUBBLE SORTING INFINITE REMASTERED](https://themindplays.pages.dev/bubble-sorting-infinite-remastered.html)
- [DOGS VS ALIENS](https://learnquester.github.io/dogs-vs-aliens.html)
- [CATEGORY JUMPING147](https://thelearnquester.web.app/category-jumping147.html)
- [ASYLUM BALDI GRANNY SLENDER](https://learnquester.github.io/asylum-baldi-granny-slender.html)
- [CANDY MATCH PUZZLE](https://learnquester.github.io/candy-match-puzzle.html)
- [INDEX11](https://thelearnquester.web.app/index11.html)
- [WOODLAND SLIDE](https://learnquester.github.io/woodland-slide.html)
- [DOWNHILL CAR RIDE CRASH TEST](https://themindzone.pages.dev/downhill-car-ride-crash-test.html)
- [CATEGORY MAHJONG 3](https://themindplays.pages.dev/category-mahjong-3.html)
- [TRAFFIC COP 3D](https://thelearnquester.web.app/traffic-cop-3d.html)
- [CATEGORY CARE](https://learnquester.pages.dev/category-care.html)
- [SCP 173 ESCAPE](https://themindplay.github.io/scp-173-escape.html)
- [BUBBLE SHOOTER NEON](https://themindplay.pages.dev/bubble-shooter-neon.html)
- [POP STAR](https://themindplay.github.io/pop-star.html)
- [SWEET MATCH](https://themindplaying.web.app/sweet-match.html)
- [SPRUNKI 3D ESCAPE](https://themindplaying.web.app/sprunki-3d-escape.html)
- [CREEPY DRESS UP](https://themindplay.github.io/creepy-dress-up.html)
- [3D SUPER ROLLING BALL RACE](https://thelearnquester.web.app/3d-super-rolling-ball-race.html)
- [BUBBLE BLITZ GALAXY](https://thequizzone.pages.dev/bubble-blitz-galaxy.html)
- [POPPING SUSHI](https://themindplay.pages.dev/popping-sushi.html)
- [PARK ME DRAW PATH](https://themindplay.pages.dev/park-me-draw-path.html)
- [BOMB HEAD HOT POTATO](https://themindzone.pages.dev/bomb-head-hot-potato.html)
- [CATEGORY STICKMAN](https://thequizzone.pages.dev/category-stickman.html)
- [STICKMAN RAGDOLL PLAYGROUND](https://thelearnquesters.pages.dev/stickman-ragdoll-playground.html)
- [HORROR ESCAPE GRANNY ROOM](https://themindzone.pages.dev/horror-escape-granny-room.html)
- [CANNON SHOOTER](https://themindplay.pages.dev/cannon-shooter.html)
- [BLACK PINK STPATRICKS DAY CONCERT](https://themindplay.pages.dev/black-pink-stpatricks-day-concert.html)
- [COLLEGE GIRL COLORING DRESS UP](https://theskillquest.pages.dev/college-girl-coloring-dress-up.html)
- [HEROIC KNIGHT](https://themindplay.pages.dev/heroic-knight.html)
- [CATEGORY BIKE 3](https://themindplays.pages.dev/category-bike-3.html)
- [PORT SHIPPING TYCOON](https://theskillquest.pages.dev/port-shipping-tycoon.html)
- [DISASSEMBLE THE PICTURE PUZZLE](https://themindplay.pages.dev/disassemble-the-picture-puzzle.html)
- [LUCKY BRAINROT BLOCKS ONLINE](https://learnquester.github.io/lucky-brainrot-blocks-online.html)
- [SOLITAIRE EMPEROR SECRETS OF FATE](https://learnquester.github.io/solitaire-emperor-secrets-of-fate.html)
- [URBAN ASSAULT FORCE](https://learnquester.github.io/urban-assault-force.html)
- [MEMORY WARS](https://thelearnquester.web.app/memory-wars.html)
- [SUMMER AESTHETICS](https://thelearnquester.web.app/summer-aesthetics.html)
- [RAGDOLL SOCCER 2 PLAYERS](https://thelearnquester.web.app/ragdoll-soccer-2-players.html)
- [FALLING MAN](https://thelearnquesters.pages.dev/falling-man.html)
- [BATTLE TANKS FIRESTORM](https://learnquester.github.io/battle-tanks-firestorm.html)
- [GOOD YARD](https://themindplay.github.io/good-yard.html)
- [ASMR PET TREATMENT](https://learnquester.github.io/asmr-pet-treatment.html)
- [EMOJI SMASHER SMILEY GAME](https://learnquester.github.io/emoji-smasher-smiley-game.html)
- [ITALIAN BRAINROT CHALLENGE](https://themindplay.github.io/italian-brainrot-challenge.html)
- [HOOP WORLD 3D](https://thelearnquester.web.app/hoop-world-3d.html)
- [YARN FEVER UNRAVEL PUZZLE](https://learnquester.github.io/yarn-fever-unravel-puzzle.html)
- [REVERSI](https://thequizzone.pages.dev/reversi.html)
- [BUS COLOR JAM](https://thequizzone.pages.dev/bus-color-jam.html)
- [AGE OF ZOMBIES](https://themindplay.pages.dev/age-of-zombies.html)
- [ZENITH RUSH](https://learnquester.github.io/zenith-rush.html)
- [MY LITTLE CITY](https://thelearnquester.web.app/my-little-city.html)
- [AGENT SQUAD](https://thelearnquester.web.app/agent-squad.html)
- [DYNAMONS 11](https://learnquester.github.io/dynamons-11.html)
- [INDEX23](https://themindplays.pages.dev/index23.html)
- [IDLE PET](https://thelearnquesters.pages.dev/idle-pet.html)
- [BILLIARD DIAMOND CHALLENGE](https://learnquester.github.io/billiard-diamond-challenge.html)
- [CUT THE ROPE 2](https://themindplay.pages.dev/cut-the-rope-2.html)
- [LOL SURPRISE OMG BB DRIVER](https://theskillquest.pages.dev/lol-surprise-omg-bb-driver.html)
- [INDEX35](https://themindplays.pages.dev/index35.html)
- [FISH STORY 4](https://themindplay.pages.dev/fish-story-4.html)
- [MONSTER SQUAD RUSH](https://learnquester.github.io/monster-squad-rush.html)
- [CREEPY DRESS UP](https://learnquester.github.io/creepy-dress-up.html)
- [MALATANG MASTER STACK RUN 3D](https://theskillquest.pages.dev/malatang-master-stack-run-3d.html)
- [LOVE ARCHER](https://learnquester.github.io/love-archer.html)
- [REAL STREET FIGHTER 3D](https://theskillquest.pages.dev/real-street-fighter-3d.html)
- [ROAD TO 7](https://learnquester.github.io/road-to-7.html)
- [CODEQUEST](https://themindplay.github.io/codequest.html)
- [AVATAR MASTER FIX UP FACE](https://learnquester.github.io/avatar-master-fix-up-face.html)
- [PUT THE FRUIT TOGETHER](https://themindzone.pages.dev/put-the-fruit-together.html)
- [HUGGY WUGGY ESCAPE](https://learnquester.pages.dev/huggy-wuggy-escape.html)
- [STICKMAN ARCHERO FIGHT STICK SHADOW FIGHT WAR](https://learnquester.github.io/stickman-archero-fight-stick-shadow-fight-war.html)
- [ANIMAL MERGE ZOO PARK](https://thelearnquester.web.app/animal-merge-zoo-park.html)
- [BUTTERFLY KYODAI DELUXE 2](https://learnquester.pages.dev/butterfly-kyodai-deluxe-2.html)
- [TIC TAC TOE MATCH THREE](https://thelearnquester.web.app/tic-tac-toe-match-three.html)
- [HOME RUSH THE FISH WAR](https://thelearnquesters.pages.dev/home-rush-the-fish-war.html)
- [MAGIC BOTTLES](https://learnquester.pages.dev/magic-bottles.html)
- [FLOWER SORT](https://theskillquest.pages.dev/flower-sort.html)
- [KINGDOM PUZZLES](https://thequizzone.pages.dev/kingdom-puzzles.html)
- [PHONE CASE DIY RUN](https://theskillquest.pages.dev/phone-case-diy-run.html)
- [HILL STATION BUS SIMULATOR](https://theskillquest.pages.dev/hill-station-bus-simulator.html)
- [2 PLAYER BATTLE](https://themindplaying.web.app/2-player-battle.html)
- [SPACE BLAST](https://thelearnquester.web.app/space-blast.html)
- [FRUIT JAM](https://learnquester.pages.dev/fruit-jam.html)
- [WIPE INSIGHT MASTER](https://learnquester.github.io/wipe-insight-master.html)
- [FALLING MAN](https://themindzone.pages.dev/falling-man.html)
- [FOOTBALL PENALTY](https://learnquester.github.io/football-penalty.html)
- [PING PONG BATTLE TABLE TENNIS](https://thelearnquester.web.app/ping-pong-battle-table-tennis.html)
- [GOOD TO DRIVE](https://themindplay.pages.dev/good-to-drive.html)
- [SODA BLOCK JAM](https://thelearnquesters.pages.dev/soda-block-jam.html)
- [POP THEM](https://thelearnquester.web.app/pop-them.html)
- [CATEGORY BOOKMARK](https://thelearnquester.web.app/category-bookmark.html)
- [CATEGORY CASUAL 2](https://thelearnquester.web.app/category-casual-2.html)
- [MMA SUPER FIGHT](https://themindzone.pages.dev/mma-super-fight.html)
- [LUNAR PHASE BATTLE](https://learnquester.pages.dev/lunar-phase-battle.html)
- [DELIVERY NOW](https://thequizzone.pages.dev/delivery-now.html)
- [PIXEL SHOOT](https://themindplays.pages.dev/pixel-shoot.html)
- [PIRATE ISLAND](https://learnquester.pages.dev/pirate-island.html)
- [CHINESE FOOD CHEF DUDU](https://themindzone.pages.dev/chinese-food-chef-dudu.html)
- [CATEGORY RELAXING223](https://thelearnquesters.pages.dev/category-relaxing223.html)
- [CUTE SHEEP SKYBLOCK](https://themindplaying.web.app/cute-sheep-skyblock.html)
- [DAILY JEWELS BLITZ MAHJONG](https://learnquester.pages.dev/daily-jewels-blitz-mahjong.html)
- [OFFICE PYRAMID SOLITAIRE](https://learnquesters.pages.dev/office-pyramid-solitaire.html)
- [CATEGORY ARENA255](https://thelearnquesters.pages.dev/category-arena255.html)
- [CATEGORY SOCCER 2](https://thelearnquester.web.app/category-soccer-2.html)
- [SHINY JEWELS](https://themindplay.pages.dev/shiny-jewels.html)
- [MONEY MAKER](https://learnquester.pages.dev/money-maker.html)
- [OFFICE SPIDER SOLITAIRE](https://themindplay.github.io/office-spider-solitaire.html)
- [LIVE 100 DAYS](https://themindplays.pages.dev/live-100-days.html)
- [MOTO ATTACK BIKE RACING](https://learnquester.pages.dev/moto-attack-bike-racing.html)
- [CATEGORY UNBLOCKEDGAMES](https://themindplays.pages.dev/category-unblockedgames.html)
- [JENNYS MATH PUZZLE](https://theskillquest.pages.dev/jennys-math-puzzle.html)
- [SNOWBOARD GAME PARTY](https://learnquester.github.io/snowboard-game-party.html)
- [CATEGORY SPEED158](https://themindplays.pages.dev/category-speed158.html)
- [SUPER TANK HERO](https://learnquesters.pages.dev/super-tank-hero.html)
- [TRI PEAKS EMERLAND SOLITAIRE](https://themindplay.pages.dev/tri-peaks-emerland-solitaire.html)
- [BARRY PRISON HIDE AND SEEK](https://themindplay.github.io/barry-prison-hide-and-seek.html)
- [LABUBA MERGE](https://learnquesters.pages.dev/labuba-merge.html)
- [CATEGORY LIGHTSPEED FILTER](https://thelearnquester.web.app/category-lightspeed-filter.html)
- [HOME BLOCK STORY](https://themindplay.pages.dev/home-block-story.html)
- [SNAKE 2048IO](https://thelearnquester.web.app/snake-2048io.html)
- [BARBEE MET GALA TRANSFORMATION](https://themindplays.pages.dev/barbee-met-gala-transformation.html)
- [MINEBUILD](https://learnquester.pages.dev/minebuild.html)
- [QUBE 2048](https://themindplay.pages.dev/qube-2048.html)
- [SHOOT AND DRIVE](https://themindplay.pages.dev/shoot-and-drive.html)
- [WHAT A WALK](https://themindplay.pages.dev/what-a-walk.html)
- [K WEDDING DREAM](https://learnquesters.pages.dev/k-wedding-dream.html)
- [GOAL IO](https://themindplay.github.io/goal-io.html)
