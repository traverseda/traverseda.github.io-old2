```yaml
created: '2017-11-03T18:43:55.500859+00:00'
published: true
tags: [home]
updated: '2017-11-03T18:43:55.501098+00:00'

```
---
#Heading 1
##Heading 2
###Heading 3

**Bold Text**

*Italic Text*

~~StrikeThrough~~

> qoute

---

 * Item 1
 * item 2
 * item 3
 * item 4

---
```python
"""
Write a program that prints the numbers from 1 to 100. But for multiples of
three print “Fizz” instead of the number and for the multiples of five print
“Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
"""

def buzz(data):
    for i in data:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

buzz(range(1,100))

```
---
```python
"A much"
"thinner"
"code block."

```
