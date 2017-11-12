This is a custom static-site generator. It's pretty decent, but every page
needs to be loaded into memory at the moment, which isn't great. Should be
fixable, but clear/simple code is more important to me right now.

In order to get it playing nicely both in a folder and on a webserver, we've had
to employ some hacks. Use relative urls like they were absolute urls.
