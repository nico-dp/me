"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ["what", "does", "this", "line", "do", "?"]

# I think that this will go through the list of words and print each word
for word in some_words:
    print(word)
# It went through the list of and printed each word

# I think that this will do the same thing as x and word are both variables
for x in some_words:
    print(x)
# This also printed every word in the list, although in the debugger it shows word: '?' and im not sure why

# This will print the entire list some_words
print(some_words)
# This printed the entire list some_words, in the debugger it once again shows word: '?' and now x: '?'.
# I know think that this is because the debugger sees the variables above but has nothing to do with them

# I think that len stands for length and therefore if the list has more than the words it will print "some_words contains more than 3 words"
if len(some_words) > 3:
    print("some_words contains more than 3 words")
# It printed "some_words contains more than 3 words"

# Well according to google, this will print my computers; system, node, release, version, machine, and processor
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())


usefulFunction()
# I guess it did this?