"""
stringjumble.py
Author: Adam Pikielny
Credit: http://stackoverflow.com/questions/493386/how-to-print-in-python-without-newline-or-space
http://stackoverflow.com/questions/743806/split-string-into-a-list-in-python

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
import sys

stringinput=(input("Please enter a string of text (the bigger the better): "))
liststringinput=list(stringinput)
liststringinput.reverse()
for x in liststringinput:
    sys.stdout.write(x)
print("\n")

# split the text
words = stringinput.split()

    # for each word in the line:
words.reverse()
for word in words:
    sys.stdout.write(word + " ")