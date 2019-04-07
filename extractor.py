from pyteaser import SummarizeUrl, Summarize
import wikipedia #for gathering wikipedia content
import collections #for counting the most counted word
from collections import Counter 
import re #for regular expressions

def remove_num(sent):
	return [x.strip() for x in re.split(r'\[].[0-9*][\]', sent) if x.split()]

def fact_extract(user_input):

	#user_input = str(raw_input('Enter input: ')) this will come from the front end instead of cli
	url = wikipedia.page(user_input).url
	error=''
	# s = Summarize(user_input, wikipedia.page(user_input).content) is to summarize if the url is not available
	# this one is for extracting the content directly from the keyword entered by the user
	s = SummarizeUrl(url)
	if s == '':
		return "NO CONTENT"
	else:
		summ = ' '.join(word for word in s)

	'''try:
		summ = ' '.join(word for word in s)	
	except TypeError:
		return error'''
		#summ = summ.replace("]","")
	
	
	#non reg ex way of dealing with expressions
	def removeNestedParentheses(s):
	    ret = ''
	    skip = 0
	    for i in s:
	        if i == '[':
	            skip += 1
	        elif i == ']'and skip > 0:
	            skip -= 1
	        elif skip == 0:
	            ret += i
	    return ret

	summ = removeNestedParentheses(summ)
	summ = summ.replace(". ",".\n\n")
	
	return summ