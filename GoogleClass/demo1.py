

# ---------------- Sorting --------------------------
"""
# a = [5, 1, 4, 3]
# print sorted(a)  ## [1, 3, 4, 5]
# print a  ## [5, 1, 4, 3]


# strs = ['aa', 'BB', 'zz', 'CC']
# print sorted(strs)  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
# print sorted(strs, reverse=True)   ## ['zz', 'aa', 'CC', 'BB']


# Custom Sorting With key=
strs = ['ccc', 'aaaa', 'd', 'bb']
print sorted(strs, key=len)  ## ['d', 'bb', 'ccc', 'aaaa']

## "key" argument specifying str.lower function to use for sorting
print sorted(strs, key=str.lower)  ## ['aa', 'BB', 'CC', 'zz']

## Say we have a list of strings we want to sort by the last letter of the string.
strs = ['xc', 'zb', 'yd' ,'wa']
def MyFn(s):
	return s[-1]
## Now pass key=MyFn to sorted() to sort by the last letter:
print sorted(strs, key=MyFn)  ## ['wa', 'zb', 'xc', 'yd']

a = [5, 1, 4, 3]
print a.sort()
print a  ## [5, 1, 4, 3]


# Tuples
tuple = (1, 2, 'hi')
print len(tuple)  ## 3
print tuple[2]    ## hi
# tuple[2] = 'bye'  ## NO, tuples cannot be changed
tuple = (1, 2, 'bye')  ## this works
tuple = ('hi')
print tuple

(x,y,z) = (42,13,"hike")
print z

def Foo():
	return (1,1)
(err_string,err_code) = Foo() 
print(err_code,err_string)
"""

# ---------------- List Comprehensions (optional) ----------------


# The syntax is [ expr for var in list ] 
nums = [1,2,3,4]
squares = [ n*n for n in nums ]
print squares

strs = ['hello', 'and', 'goodbye']
shouting = [s.upper() + '!!!' for s in strs]
print shouting

# You can add an if test to the right of 
# the for-loop to narrow the result.  
nums = [2,8,1,6]
small = [n for n in nums if n <= 2]
print small

fruits = ['apple', 'cherry', 'banana', 'lemon']
afruits = [s.upper() for s in fruits if 'a' in s]
print afruits


# ---------------- Lists --------------------------
"""

# colors = ['red', 'blue', 'green']
# print colors[0]    ## red
# print colors[2]    ## green
# print len(colors)  ## 3

# b = colors   ## Does not copy the list

# # FOR and IN
# squares = [1,4,9,16]
# sum = 0 
# for num in squares:
# 	sum += num
# print sum

# list = ['larry', 'curly', 'moe']
# if 'curly' in list:
# 	print 'yay'

# # Range
# a = []
# for i in range(100):
# 	a.append(i)
# 	print i 

# # While Loop
# i = 0
# while i < len(a):
# 	print a[i]
# 	i += 3

# List Methods

list = ['larry', 'curly', 'moe']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end
print list  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print list.index('curly')    ## 2

list.remove('curly')         ## search and remove that element
list.pop(1)                  ## removes and returns 'larry'
print list  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']



list = [1, 2, 3]
# print list.append(4)   #### Correct pattern: NO, does not work, append() returns None 
list.append(4)
print list  ## [1, 2, 3, 4]

# List Build Up
list = []          ## Start as the empty list
list.append('a')   ## Use append() to add elements
list.append('b')
print list


# List Slices
list = ['a', 'b', 'c', 'd']
print list[1:-1]   ## ['b', 'c']
list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print list         ## ['z', 'c', 'd']



"""


# ---------------- Strings --------------------------
# str = 'Hello'
# print str[:-3]
# print str[-3:]

# text =  "%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down')
# print text

# text = ("%d little pigs come out or I'll %s and %s and %s" %
#     (3, 'huff', 'puff', 'blow down'))


# ustring = u'A unicode \u018e string \xf1'
# print ustring

# s = ustring.encode('utf-8')
# print s

# t = unicode(s,'utf-8')
# print t