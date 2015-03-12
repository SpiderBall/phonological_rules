#!/usr/local/bin/python -tt
#! -*- coding: utf-8 -*-

import re
import sys

if sys.version_info >= (3,0):
    xrange = range

#TODO create a function to loop through a word until it finds the char 
#that is subject to change (first argument) in the appropriate environment (2nd arg)
#and replace it with the appropriate char as needed (arg 3)

#NOTE: this may make any rule that depends on a rhyme scheme impossible to test on here
# use this first, then test for a rhyme scheme if all else fails (we'll do this later)

#this would be easier if i created a word class so i dont need to pass in everything

#NEXT i should make a rule generator. That will be much tougher

def rule_check(word, charToChange, newChar, envbefore, envafter):
    for i in xrange(len(word)):
        if word[i] == charToChange and checkenv(envbefore, envafter):
            charToChange = newChar

def checkenv(envbefore, envafter):
	#TODO: define this function
