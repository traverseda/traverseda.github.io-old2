```yaml
contentHash: 898a234fd5a930a6118c83a5d8453c8f76826911b1d3dd400d5d032f469db39d
stripHtml: false
lastRender: '2017-02-22T13:02:37.210597+00:00'
includeToC: false
published: false

```
---

#Engineering Linearity
##Preventing "a photo-copy of a photo-copy of a photo-copy" in self-replicating machines.

One of the goals of the reprap community is to get self-replicating machines.
This workds pretty alright for the most part. It's more expensive then just
buying the parts, and obviously it only works for the plastic components, not
the hot-end or motors or control board. But on the whole it's an alright first
step.

The big problem is the "photo-copy of a photo-copy of a photo-copy" effect. If
you print a 3D printer on a 3D printer, it's slightly less accurate. And so on
and so on. This keeps us from true self-replication.

A rack and pinion system printed using a 3D printed rack and pinion system is
going to be less accurate then the original. After so many copies,
you've run out of lineararity.

Repraps get around this using various "vitamens". Using cold-rolled steal bars
instead of 3D printed parts, and getting their linearity from those handfull of
"known good" components.

But we have another source of pre-engineard linearity. The clocks on
microcontrollers provide a *high* degree of linearity in the 4th dimension,
time.
