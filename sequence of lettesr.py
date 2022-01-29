# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 16:19:46 2022

@author: jaxso
"""

userInput = input('type in a sentence')
counter = 0
recent = 'a'
high = 0
word = ': '
wordTwo = ': '
justMissed = False
for letters in userInput:
    print(letters)
    if recent <= letters:
        counter += 1
        word += letters
        recent = letters
        if len(word) > len(wordTwo):
            wordTwo = word
        
    else:
        counter = 1
        recent = letters
        word = ': ' + letters
    if counter > high:
        high = counter
print('Longest substring in alphabetical order is' + wordTwo)
print(high)
    
    