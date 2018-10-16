import re

"""

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w',str)
if match:
	print 'found', match.group()
else:
	print 'not found'


# Basic Patterns

# The power of regular expressions is that they can specify patterns, not just fixed characters. Here are the most basic patterns which match single chars:

# a, X, 9, < -- ordinary characters just match themselves exactly. The meta-characters which do not match themselves because they have special meanings are: . ^ $ * + ? { [ ] \ | ( ) (details below)
# . (a period) -- matches any single character except newline '\n'
# \w -- (lowercase w) matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_]. Note that although "word" is the mnemonic for this, it only matches a single word char, not a whole word. \W (upper case W) matches any non-word character.
# \b -- boundary between word and non-word
# \s -- (lowercase s) matches a single whitespace character -- space, newline, return, tab, form [ \n\r\t\f]. \S (upper case S) matches any non-whitespace character.
# \t, \n, \r -- tab, newline, return
# \d -- decimal digit [0-9] (some older regex utilities do not support but \d, but they all support \w and \s)
# ^ = start, $ = end -- match the start or end of the string
# \ -- inhibit the "specialness" of a character. So, for example, use \. to match a period or \\ to match a slash. If you are unsure if a character has special meaning, such as '@', you can put a slash in front of it, \@, to make sure it is treated just as a character.


## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.
match = re.search(r'iii', 'piiig') ##=>  found, match.group() == "iii"
print match.group()
match = re.search(r'igs', 'piiig') #=>  not found, match == None
print match

## . = any char but \n
match = re.search(r'..g', 'piiig')
# =>  found, match.group() == "iig"
print match.group()

## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g') #=>  found, match.group() == "123"
match = re.search(r'\w\w\w', '@@abcd!!') #=>  found, match.group() == "abc"



# Repetition

# Things get more interesting when you use + and * to specify repetition in the pattern

# + -- 1 or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
# * -- 0 or more occurrences of the pattern to its left
# ? -- match 0 or 1 occurrences of the pattern to its left

# Repetition Examples

# ## i+ = one or more i's, as many as possible.
# match = re.search(r'pi+', 'piiig') =>  found, match.group() == "piii"

# ## Finds the first/leftmost solution, and within it drives the +
# ## as far as possible (aka 'leftmost and largest').
# ## In this example, note that it does not get to the second set of i's.
# match = re.search(r'i+', 'piigiiii') =>  found, match.group() == "ii"


# ## ^ = matches the start of string, so this fails:
# match = re.search(r'^b\w+', 'foobar') =>  not found, match == None
# ## but without the ^ it succeeds:
# match = re.search(r'b\w+', 'foobar') =>  found, match.group() == "bar"




## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace.
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') #=>  found, match.group() == "1 2   3"
match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx')# =>  found, match.group() == "12  3"
match = re.search(r'\d\s*\d\s*\d', 'xx123xx') #=>  found, match.group() == "123"


# Emails Example

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
	print match.group()  ## 'b@google'


# Square Brackets
# Square brackets can be used to indicate a set of chars, so [abc] matches 'a' or 'b' or 'c'. 

match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
	print match.group()  ## 'alice-b@google.com'
# (More square-bracket features) You can also use a dash to indicate a range, so [a-z] matches all lowercase letters.
# To use a dash without indicating a range, put the dash last, e.g. [abc-]. 
# An up-hat (^) at the start of a square-bracket set inverts it, so [^ab] means any char except 'a' or 'b'.
"""


# # Group Extraction
# str = 'purple alice-b@google.com monkey dishwasher'
# match = re.search(r'([\w.-]+)@([\w.-]+)', str)
# if match:
# 	print match.group()   ## 'alice-b@google.com' (the whole match)
# 	print match.group(1)  ## 'alice-b' (the username, group 1)
# 	print match.group(2)  ## 'google.com' (the host, group 2)


# ## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
# do something with each found email string
	print email


# findall With Files
# Open file
# f = open('test.txt', 'r')
# # Feed the file text into findall(); it returns a list of all the found strings
# strings = re.findall(r'some pattern', f.read())


# findall and Groups
# The parenthesis ( ) group mechanism can be combined with findall()
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print tuples  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
	print tuple[0]  ## username
	print tuple[1]  ## host


# Substitution (optional)
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
print re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str)
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher










