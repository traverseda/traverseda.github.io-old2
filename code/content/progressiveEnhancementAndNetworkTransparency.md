```yaml
contentHash: 42b7d7fbbf3bd7f4d38978d0bb1f6949b065813c706cb83e87dd08988fe7265b
created: !!python/object:arrow.arrow.Arrow {_datetime: !!timestamp '2017-11-03 17:53:11.898369'}
firstPublish: '2017-08-07T15:19:34.721682+00:00'
includeToC: false
lastRender: '2017-11-02T00:15:47.472782+00:00'
published: false
rendered: null
stripHtml: false
tags: [home]
updated: !!python/object:arrow.arrow.Arrow {_datetime: !!timestamp '2017-11-03 17:53:11.898444'}

```
---
# Progressive Enhancement and Network Transparency

Wayland has a number of features that are "out of scope". Good network
transparency is one of the things that make linux unique and powerful, and
wayland is in a unique position to set standards for network transparency.

To put it simply, I think that unless wayland codifies network transparency,
we're going to end up with 4+ competing standards, and a bunch of duplicated
effort. There are plenty of technical reasons why wayland should ignore network
transparency, but also a bunch of social reasons why they *need* to show people
a path forward, lest we end-up with an unmanagable situation down the line.

I think that wayland can get most of the advantages of both by creating a simple
system for progressivly-enhancing a network-transparent client.

## The bare minimum, a pixel-stream

A pixel stream is a good place to start. It has the *most* compatability, and
doesn't require any extra code to be written. You can consume a pixel-stream
without writing much code at all, and without using complicated build-systems or
a lot of external dependencies.

The pixel-stream protocol is unlikely to change, and if it does it's reasonable
to simply maintain multiple versions of it. We can maintain backwards
compatability with pixel-streams basically forever.

This makes it the perfect target for embedded devices, where backwards
compatability is *important*. It's also great for when you don't care about
network resources, it's low-cpu and high bandwidth.

It's the perfect target if you want to drag a window from your laptop to your
desktop, or vice-versa.

## The slightly better than minimum, pixel-streams with damage detection

A standard pixel-stream would, by default,
copy each frame into our network stream. This is about as simple as it gets, but
is hard on bandwidth, even after compression.

Video-compression isn't able to "de-duplicate". It's can't say "this button is
being used repeatedly, let's keep a copy of it". It is, essentially, sending a
new (compressed) copy of that button with every frame.

There are a number of techniques that could be used to make this better, one of
the more interesting one's being using something like
[rzip](https://rzip.samba.org/) to deduplicate long-distance (in the temporal axis) 
redundancies in pixel-stream data.

But that's a bit out-there. There's one technique that's been used reliably in
many projects, and that's "damage-detection". Basically what that means is that
wayland only sends pixel-data for screen-elements that have changed. This means
it's a lot more complicated, the server needs to keep track of what the client
has already seen, and the client needs to be able to do partial updates, not
just blit a stream into graphics memory.

## Almost good-enough, client extensions and data-streaming

Do you know what's better than streaming a bunch of pixels? Streaming the data
you used to *generate* those pixels. Alright, not all the time, there are plenty
of situations where it isn't. But most of the time.

It's almost always going to be cheaper to send `01000001` than a picture of the
letter A, no matter how good your compression algorithms are.

Your font-rendering library has a choice. It can render to a bunch of pixels, or
it can render to a command-stream, and have the client render those same glyphs.
Why in the world would you complicate your font-rending pipeline like that? To
save a few bytes here and there?

If you send a data-stream of glyph draw commands instead of pixel data, you can

 * View the same instance of a window on two different screens, with two
   different sub-pixel rendering schema
 * Display fonts beautifully on high-dpi clients
 * Magnify text without graphical aberrations
 * Render fonts cleanly on VR displays

This same technique can be applied to other libraries. Full client-side
rendering of an openGL data-stream will most likely be necessary for performant
rendering of remote VR apps, as viewpoint-translations need to happen with
incredibly low-latency.

But most importantly it provides a way to account for future use, as new
libraries become network transparent.

What's important isn't implementing an individual feature like client-side
font-rendering, what's important is that wayland provides a way for libraries to
register themselves as available, and for libraries to communicate across the
network. Whether that's used for client-side font rendering, clipboard-sharing,
or simple sound-streaming. Wayland has the opportunity to set the standard here,
and I desperately hope they take it before it's too late.

# Of course it's not that simple

I've tried to describe high-level goals here, for 3 different levels of
network-transparency

 * Basic pixel-scraping
 * Efficient pixel-scraping
 * Network transparent libraries

But even basic network transparency support is difficult right now.

Derek Foreman had this to say in [his
article](https://blogs.s-osg.org/wow-wayland-over-wire/) on wayland-over-the-wire

> * File descriptor passing is used extensively in the protocol. For example, keymaps are passed from the compositor to the client as file descriptors; the client is supposed to mmap() the file descriptor and treat it like an array. This sounds a little silly at first, but a keymap is actually a fairly large chunk of data that’s too large to fit in a single Wayland message packet (they can’t be larger than 4Kb). Obviously you can’t (usefully) pass a file descriptor over the network.
> * Keyboard repeat is handled on the client side, so if you have a dodgy network connection and a key press packet arrives but the key release packet is delayed, the client would start repeating keys.
> * Buffers are shared between the client and compositor… somehow. They could be shared memory through mmap or dmabuf, or it could be mesa’s buffer extension. In any event, image data is never pushed to the compositor through a network socket, it always takes the form of some kind of handle that both the client and compositor understand.  These handles are local only and are meaningless over a network.

