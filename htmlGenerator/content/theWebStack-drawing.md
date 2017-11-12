#Drawing on the web

The web has gone through a great number of iterations, and has a great number of
problems. This is my understanding of that's wrong with one particular subset,
the drawing protocols.

##Html, from data-serialization to drawing protocol



---

Html is supposed to be data-objects, but the models breaks a lot. XML was
original an object notation format, like json.

CSS is supposed to be purely presentation.

Originally it was like this

Html: data
CSS: Presentation
Javascript: Not really supposed to exist, but the most legitimate use is as
logic that acts on presentation, that adds or removes classes from your html

A lot of systems mix data and presentation pretty hard though. Html can be
thought of as your application data, or as data about the structure of a scene
graph. That's where a lot of this inconsistency comes from, I think.

React accepts that you can't in practice keep html and css separate, and keeps
the data in a custom JS data structure. Changing the model so that both html and
css are used for presentation. Html turns into the data for your scene graph,
not your application data.

Transforming the model thusly

Html: Scene graph data structure, list of draw-objects, etc
CSS: Rendering rules, how to draw your draw-objects.
Application data: Literally just a json-serialization of application context
Javascript: Transforms your application data into html.


