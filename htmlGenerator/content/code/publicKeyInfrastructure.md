# On public key infrastructure

Using GPG always feels vaguely... Unsafe. You can never really be sure that you
haven't lost control of your private key, and I feel it creates a false sense of
security. Intellectually I know that it's better than nothing, but it still
feels a bit like giving some vague incomprehensible system power-of-attorney.

The big problem of crypto has always been UX, and I think we can do a lot better.

## Show me every piece of text I sign

Show me every piece of text I sign. Make a popup, send me an email, something.
Once my password is cached, silently signing whatever should not be an option.

### Maybe show me every piece of text I've ever signed

This makes is a lot easier to tell if I've lost control of my key.

## Show me what app requested that I sign something

If I sign an email, I want "email" to be part of that context. That way if my
email app tricks me into signing a message saying "release all my funds to the
account at XXX XXX XXX", it's clear that's in the context of email, and not in
the context of my check-signing app.

## Use "2 factor" signing

I should be able to say "only trust this message if it's signed by two of my
device-keys". That process should be pretty transparent.

## Use different levels of security for different contexts

Messages in the "email" context should be considered valid with only one devices
signature. A bank transfer should require more effort. Changes to my security
policy (signing messages in the "keyring context")
could require a dedicated hardware device I keep in my safety deposit
box.

## Date stamp every message I sign

Prevent replay attacks. If I send my mom a message saying "can you fax me a copy of
my birth certificate" I don't want that same message to get used years latter
when I don't use that fax service.

## Don't wait for me to revoke a certificate

Maintaining a crypto key securely takes work, without me actively confirming that
I still use and control the key, it should be presumed that I don't. Set a sane
default for expiration, and require user intervention to push that expiration
off.

# Finally, a word on securing distributed apps with a web-of-trust

Right now, if you want to right a distributed web app, your only real choice is
to use block chains. A proper web-of-trust solves a lot of those problems, and
you can use distributed consensus algorithms. Of course that's hard to
implement.

