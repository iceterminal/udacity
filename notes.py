UNIT 1
-----------------------------------------
Programming is the core of computer science.
Natural languages are ambiguitus. 

Sentence -> Subject Verb Object
	Subject -> Noun
	Object -> Noun
	Verb -> eat, like
	Noun -> cookies, I, python

Backus Naur form - John Backus. Guy that created Fortran

<non-terminal> -> replacement
means something we are not done with.

Python Grammar for arithmetic expressions
	Expresson -> Expression Operator Expression
	Expression -> Number
	Operator -> +, *, -, /
	Number -> 0,1,2,3,4,5,etc.
	Expression -> (Expression)

print (7*7*24*60) #How many minutes in 7 weeks

#speed of light is 299792458 meters per second
#centimeters = 100	1 meter is 100 centimeters
#nanosecond = 1.0/1000000000	1 billionth of a second

print (100 * 299792458 * 1.0/1000000000) # how far light travels in centimeters in one nanosecond

Variables are storage of values
speed_of_light = 299792458 # meters per second
centimeters = 100
billionth = 1/1000000000
nanostick = speed_of_light * billionth * centimeters

= means assignment
Strings are sequence of characters between quotes.
Strings are immutable 
<string>[<expression>]
'udacity'[0] -> 'u'

<string>[<expression>:<expression>]
'udacity'[0:2] -> 'ud'

'audacity' change to Udacity
s = 'audacity'
print 'U' + s[2:]

Use the FIND method to find a string within a string.
<string>.find(<string>)
variable = string
newvariable = variable.find(string) # this will return the first index of the string found
print newvariable -> [indexnumber]
print newvariable[indexnumber] -> string #will print out the string from the index found
case of strings matters

To find a string AFTER the first occurence
<string>.find(<string>, <number>) #This will look for the occurence of the string after the index given

Extracting links from a webpage.
Get source of webpage.

page = content of webpage
start_link = page.find('<a href=')
start_quote = page.find('"', start_link) #This starts to find " after the first occurence
end_quote = page.find('"', start_quote + 1) #will find next quote after start_quote
url = page[start_quote + 1: end_quote]
print (url)


UNIT 2
-------------------------------------------------------
Procedures are a way to package code so we can reuse it more easily.
Control structures the way to keep going.

To find the second link on a page, we start from where we left off only beginning at the end of end_quote:
page = page[end_quote:]
start_link = page.find('<a href=')
start_quote = page.find('"', start_link) #This starts to find " after the first occurence
end_quote = page.find('"', start_quote + 1) #will find next quote after start_quote
url = page[start_quote + 1: end_quote]
print (url)

ETC if we wanted to get others after the first 2 links.

Procedural abstraction- something we do over and over again, but want to make a procedure.
Instead of having to type code over and over, create a procedure to redo code but with different input.

A procedure takes input in and outputs data.
Such as + operator. It will take numbers, ADD them together, then output the data

Procedure is also called function
Always starts with 'def'.
	def <name> (parameters):
		<block of code> #indented in 4 spaces or 1 tab

def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
        return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote + 1: end_quote]
	return url, end_quote
	page = page[end_quote:]


operands = arguments = inputs 

def rest_of_string(s):
	return s[1:]

print rest_of_string('audacity')

def square(n):
	n = n ** 2
	return n
  or
  	return n * n

def sum3(a, b, c):
	return a + b + c

def abbaize(a, b):
	return a + b + b + a


def find_second(a, b): # 'a' is the string we are looking in, for the 'b' string
	first = a.find(b)
	return a.find(b, first + 1)

def is_friend(name):
	return name[0] == 'D' or name[0] == 'N' #returns True if name starts with D or N

In concerns with True -or- False (OR)
if the first value evaluates to True, the second value is ignored
if the first value evaluates to False, the value of the second value is used.

Of 3 numbers, return largest.
def biggest (a, b, c):
	if a >= b and a >= c:
		return a
	elif b >= c and b >= c:
		return b
	else:
		return c
OR
using an older function, incorporate that into this function as Such
def bigger(a, b):
	if a > b:
		return a
	else:
		return b
THEN 
def biggest (a, b, c):
	return bigger (bigger(a, b), c) # this still compares only 2 inputs at a time
OR- use MAX (built in)
def biggest (a, b, c):
	return max (a, b, c)

WHILE LOOPs
------------------------------
while <testExpression>: # runs loop until the expression is false
	<block>
EX: 
i = 0
while i < 10:
	i = i + 1

factorial(n) = 
	n * (n -1) * (n -2) * etc.

def factorial(n): # take 'n' and multiple that by each decreasing number by 1. n=5 is 5*4*3*2*1
	x = 1
	while n >= 1:
		x = x * n
		n = n - 1
	return x

break statement gives us a option to stop the while loop
while <expression>:
	<block of code>
	if <break test>: #if this IF statement is true, the break will occur. If False, if is bypassed
		break
	<more code>
<after while loop>

def print_numbers(n):
	i = 0
	while i <= n:
		i = i + 1
		print i
# to use a BREAK it could be like this
def print_numbers(n):
	i = 0
	while True:
		if i > n:
			break
		i = i + 1
		print i

Multiple Assignment
You can have multiple names equal to multiple values
a, b = 1, 2 # so a will = 1 and b will = 2


def get_next_target(page):
	url, endpos = get_next_target(page)
	print url
	page = page[endpos:]
	url, endpos = get_next_target(page)


url, endpos = get_next_target('Here is a <a href="http://udacity.com"> link')
if url:
	print 'Here!'
else:
	print 'Not here!'


def print_all_links(page):
	while True:
		url, endpos = get_next_target(page)
		if url:
			print url
			page = page[endpos:]
		else:
			break -OR- return None, 0


def bigger(a, b):
	if a > b:
		return a
	else:
		return b
def biggest (a, b, c):
	return bigger (bigger(a, b), c)
def median(a,b,c):
	big = biggest(a,b,c)
	if big == a:
		return bigger(b,c)
	if big == b:
		return bigger(a,c)
	else:
		return bigger(a,b)

def countdown(num):
    while num > 0:
        print num
        num = num - 1
    print ('Blastoff!')

def find_last(a, b):
	last_pos = -1
	while True:
		pos = a.find(b, last_pos + 1)
		if pos == -1:
			return last_pos
		last_pos = pos 

def stamps(int):
	p5 = int // 5 # round floor
	p5a = int % 5 # remainder 
	p2 = p5a // 2 # round floor
	p1 = p5a % 2 # remainder 


def set_range(a, b, c):  # this is ugly way. Use BIG / BIGGEST functions to find answer
    if a >= b and a >= c:  # find highest and lowest numbers, remove median. Subtract low from high
        highest = a
    if b >= a and b>= c:
        highest = b
    if c >= a and c>= b:
        highest = c
    if a <= b and a <= c:
        lowest = a
    if b <= a and b <= b:
        lowest = b
    if c <= a and c <= b:
        lowest = c
    return highest - lowest


def fix_machine(debris, product): #takes str product & checks to see if all chars are in debris
    for i in product:
        if i not in debris:
            return "Give me something that's not useless next time."
    return product





 It is very common for students to feel like they understand solutions after they see them, but not be able to solve problems on your own. You shouldn't be dismayed or frustrated if that's the case! It takes time and practice to get good at solving programming problems yourself, but as you improve you will find it a rewarding and enjoyable activity.

Learning to program is a challenging skill that involves very different types of thinking than most people are used to. I hope this lesson will give you some helpful strategies for how to go about solving problems yourself, especially as you face more complex problems like the example one here (which was contributed by a CS101 student in the forums).