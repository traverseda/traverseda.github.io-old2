```yaml
created: '2017-11-12T20:39:57.973739+00:00'
published: true
tags: []
updated: '2017-11-12T20:39:57.973759+00:00'

```
---
# Off Grid power

This is a guide/my-notes on off grid power.

If you find any errors or have any questions, please don't hesitate to
[email me](mailto:{{'traverse.da@gmail.com'|obfuscate}})
at {{'traverse.da@gmail.com'|obfuscate}}.

## You can probably save a lot of money if you do it yourself

I recently (2017) paid $80usd for ~225watts of solar cells. That's around $0.35
per watt. Now these need to be assembled, you'll break a few 5w panels.
Still, an equivelent pre-assembled unit 
from costco is easily $600. It's also well under the price-per-watt of any
preassembled solution I've seen, which I haven't seen cheaper than $0.90/watt.

Now I got an excelent deal, but I think it demonstrates that doing it yourself
can be a whole lot cheaper.


---

## You may not need an inverter

A lot of consumer electronics run off of DC voltages very similar to what your
batteries store. It's wastefull and expensive to take
your 12 volt batteries, use an inverter to step it up
to the 110 volts common in homes, then step it back down to the 5 volts your
phone needs. You end up losing something like 20% of your energy to the
conversion. Going directly from 12 volts to the 5 volts your phone needs has
losses smaller than 5%.

add information about how to do this `XL6009`.

![](media/offGridPower/XL6009.jpg "XL6009 DC-DC power converter")

## Buy led tape

Led tape is the cheapest way to buy led lighting, and is a whole lot cheaper
than led light bulbs. It comes in a variety of colors, a pure-white for
workshops, a cozy warm white, full spectrum grow-lights, programmable so you can
pick your own colour, waterproof so you can use it under water, and probably any
option you can think of.

This tape runs directly off of 12 volts, so you can hook it directly up to your
batteries. Be aware that as your batteries lose power the led tape will dim. You
can get around that by using the aforementioned `XL6009` to convert your 12
volt batteries into... 12 volts. The batteries only store approximatly 12 volts, where as
the XL6009 outputs an even 12 volts no matter what.

There are two big reasons why this is cheaper

 * Getting all those leds into a small bulb is expensive

 * Converting from 110 volts down to the ~12 volts led's need is difficult in
   that small of a space.

