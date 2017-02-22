```yaml
stripHtml: false
includeToC: false
lastRender: '2017-02-22T13:02:37.207928+00:00'
published: false

```
---








































































#Computing Enviroments

These are my personaly notes. I've tried to make them intelegable to outsiders,
but I'm not editing it or anything. Please excuse horible spelling and rambling,
it's just not a priority for me.

For a long time I've been thinking about OS design.
Why do we use file systems instead of databases? Why do we ever use a database
instead of a file system? Why has the web taken over as the dominent form of
interaction with computers for most people?

The api's you use and the social factors all tie together into an "operating
enviroment". And right now that operating enviroment is universally kind of
shitty.

Here collected on some of my thoughts on a less shitty operating enviroment. I'm
implementing some of these ideas in
[akashic](https://github.com/akashic-os/akashic-core).

#Basic overview

In unix, everything is a file. Except a bunch of things aren't, and sometimes
"file" is a euphimism for some custom binary data type. But when everything is
working well, everything is a flat text file that can be piped and otherwise
munged.

I'd like to fix that.

#Database

Right now for akashic I'm using rethinkdb as are central data store.

My dream database is pretty different though. Please excuse the rambling.

First, data objects are capnproto serialized. Basically, this means that our
basic data format is C structs and is statically typed.

Queries are made using some kind of tiny DSL. Something not entirely unlike
`asm.js`. Queries are essentially a map for a map reduce.

Queries are ongoing. You register a query sort of like registering for inotify
in linux.

Indexes are a variation of queries. Essentially they build a new 'index' data object
whenever the data in their source data object changes. They use the same DSL as
queries, and are essentially just functions. Indexes are ultimatly just some
preprocessing on data, and that can take whatever format the client wants.

We build our permissions system as a set of filters. Essentially, a permission is just
a filter that filters the input and output of a user query. This allows us to
easily create filters like `limit user Y to data objects with tag X`, and to
create much more complicated permissions.

We build our replication system using the same query system. Replication is just
a bi-directional pipe for changes between two data objects on different systems.

We allow access to data objects as shared memory, allowing for things
like an ACID layer on what would otherwise be an eventual consistancy model.

Finally, add support for more complicated data types, built on top of our
capnproto C-struct like serialization format. I'm very much in favour of some
sort of duct-typed model built out of statically typed data objects.
