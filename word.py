#!/usr/local/bin/python -tt
# -*- coding: utf-8 -*-

# NOTE: the above is NOT a comment -- it's an interpreter instruction.
# Do not remove it.

import sys

def class Word(object):
	"""This is a class to create a phonological word for the primary
	purposes of applying phonological rules to broad transcriptions of
	words to allophonic transcriptions, and to search a list of words
	for the purpose of determining phonological rules.
	
	Attributes:
		segments: An ordered list of IPA substrings that are the discrete
				phonological units of a word, with suprasegmental
				markers removed, and stresses marked in another list.

		stresses: A list of integers which indicate at which syllables
				the stresses of the word fall.
		
		breaks: A list of integers which indicate after which segments
				the syllable breaks of the word fall. This variable will
				be "Nil" in monosyllablic words.
	"""
	
	def __init__(self, ipaString):
		"""Return a Word object where the discrete segments are in the
		indices of the segments[] list and the locations of stresses and
		breaks are recorded in stresses[] and breaks[] respectively. """
		

	# TODO: Procedure to break down ipaString into segments[]
	# TODO: Procedure to find stresses ONLY IF IPA markers are present
	# TODO: Procedure to find breaks even if IPA markers are absent
	# Write as helper functions with __function_name__ or as
	# helper non-member functions outside class def?

# end class definition

