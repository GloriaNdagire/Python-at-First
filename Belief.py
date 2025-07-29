'''
#this is just a comment
print("Welcome To My World")
print('Welcome To My World')

name = "Gloria"
print(name)

names= len(name)
print(names)

age = 20
print(age)

city="New York City"

Age = 30

print(str(age)  + " " +str(Age))

print("My name is "+ name +" and I am " + str(age) + " years old.")  #concatenating strings

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

print(full_name)
print("What is your name?")
myAge = input()
print("My name is "+ myAge)
print( 'It is good to see you, {}'.format(myAge))  #{} these here are acting like placeholders

message = "hello, my name is {}, i am {} years old, and i live in {}.".format(name, age, city)
print("hello, my name is {}, i am {} years old, and i live in {}.".format(name, age, city) )
print("Hello, my name is "+ name+ " i am " + str(age) + " years old, and i live in " + city +".")
print(f"hello, my name is {name}, i am {age} years old, and i live in {city}.") # f-strings are preferred because they make the code mor readable and easy

print('hello' == 'Hello')
print('dog' != 'cat')

#but don't use this, use this below

print('hello' is 'Hello')
print('dog' is not 'cat')

#can be used to evaluate things

print(4<5) and (5<6)
print(1 == 2) or (2 == 2)
print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)

#if statements

if name == 'Alice':
 print ('Hi, Alice.')
else:
   print('Hello, stranger.')

#example
myName1 = input ()

if myName1 == 'Gloria' :
   print("Hi, Pretty Girl")
else: 
   print("God bless you")

# use of elif
name = 'Bob'
age = 5
if name == 'Alice':
   print('Hi, Alice')
elif age < 12:
   print('You are not Alice, kiddo.')

#Combination of if, elif and else...example
name = 'Bob'
age = 30
if name == 'Alice':
   print('Hi, Alice.')
elif age < 12:
   print('You are noy Alice, kiddo.')
else:
   print('You are neither Alice nor a little kid.')

# we are now on Loops
# WHILE LOOPS
yet = 0
while yet < 5:
   print('Hello, World.')
   yet = yet + 1

while True:
   print('Please type your name.')
   name = input()
   if name == 'your name':
      break
   print ('Thank you!') 

#another while loop

while True: 
   print('Who are you?')
   name = input()
   if name != 'Joe' :
      continue
   print('Hello, Joe. What is the password? (It is a fish.)')
   password = input()
   if password == 'swornfish' :
      break
print('Access granded.') 

# ANOTHER TYPE OF LOOP IS THE FOR LOOP
print('My name is')
for i in range(5):
   print('Jimmy Five Times ({})' .format(str(i)))

for i in range(0, 10, 2):   #0 is the first number in the range, 10 is the last number in the range and 2 is the increment
   print(i)  
print(" ")
for i in range(5, -1, -1):
   print(i) 
print(" ")


##import random
for i in range(5):
   print(random.randint(10, 20))   #this is a random module, one the iterates random numbers between 10 and 20, but with in only five iterations

#from random import............This is how you can import everything from the random module

##import sys
while True:
   print('Type exit to exit.')
   response = input()
   if response == 'exit':
      sys.exit()
   print('You typed {}.'.format(response))   

 ##function
def hello(name):
   print('Hello {}' .format(name))

hello('Alice')    
hello('Bob') 

##another function
import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'it is certain'
    elif answerNumber == 2:
        return 'go away'
    elif answerNumber == 3:
        return 'sit up'    
    elif answerNumber == 4:
        return 'stand up'    
    elif answerNumber == 5:
        return 'grow'    
    else:
        return 'don\'t do it'

r = random.randint(1,6)
fortune = getAnswer(r)
print(fortune)     

print('Hello ', end='')
print('Gloria') 
print('cats', 'dogs', 'mice', )    
print('cats', 'dogs', 'mice', sep=',')
print(" ")  

#checking for an error or error handling
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError as e:
        print('Error: Invalid argument: {}' .format(e))

print(spam(2))        
print(spam(12))        
print(spam(0))         
print(spam(1)) 

#WITH FINALLY
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError as e:
        print('Error: Invalid argument: {}' .format(e))
    finally:
        print("-- division finished --")   

print(spam(2))        
print(spam(12))        
print(spam(0))         
print(spam(1)) 

#Here is how you create a list in py
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0])   #if you do spam[-1] that means it will be counting from the end of the list

#also
print(spam[0:4]) # so this starts from index[0] and ends at index[4], which inother words is the entire list
print(spam[1:3])
print(spam[1:4])
print(spam[0:-1])

#how to add staff onto the list
spam2 = spam [:]
spam.append('dog')
print(spam)
print(spam2)
#showing length of the array
print(len(spam))
#how to replace a member in an array
spam[1] = 'lion'
print(spam)
# you can concatenate the array using the + sign eg ['a' , 1, 'b'] + [1,2,3]
# you can delete members in an array
del spam[2]
print(spam)


supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i, supply in enumerate(supplies):
     print ('Index {} in supplies is {}' .format(str(i), supply))

name = ['Pete', 'John', 'Elizabeth']
age = [6, 23, 44]
for n, a in zip(name,age):
     print(f"{n} is {a} years old")


just = 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
print(just)

print("")

just = ['hello', 'hi', 'howdy', 'heyas']
justify='howdy' in just 
jus = 'howdy' not in just
print(justify)
print(" ")
print(jus)

spam = 'Hello'
spam += ' world'
print(spam)
print(" ")
bacon = ['zophie']
bacon *=  3
 
print(bacon)

spam = ['cat', 'bat', 'rat', 'elephant']
g=spam.index('rat')
print(g)  #this will return the index of the item in the list
print(" ")

spam = ['cat', 'bat', 'rat', 'elephant']
spam.append('mouse')
print(spam)  #this will add the item to the end of the list
print(" ")

spam = ['cat', 'bat', 'rat', 'elephant']
spam.insert(3, 'mice')
print(spam)  #this will insert the item at the specified index
print(" ")

spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('elephant')
print(spam)  #this will remove the specified item from the list
print(" ")

spam = ['cat', 'bat', 'rat', 'elephant']
spam.sort()
print(spam)  #this will sort the list in alphabetical order  this can also be used for numbers
print(" ")

spam.sort(reverse=True)
print(spam)  #this will sort the list in reverse alphabetical order
print(" ")

#tuple
eggs = ('hello', 90, 900, 800)
print(eggs[3])  #this will return the first item in the tuple
print(eggs[1:3])
print(len(eggs))
'''
# the next one is a dictionary like thing in other programming languages it is called an object
#for example.....myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'} here the keys are size, color and desposition, 
#and the values are fat, gray and loud

spam = {'color': 'red', 'age': 42} #we can use the .value to print out all the values and .keys to print out all the keys
for v in spam.values(): #here we want to loop all the values which are red and 42
    print(v) 
print(" ")     
for v in spam.keys():
    print(v) 
#and then with the .items to print out all the items       
print(" ")     
for v in spam.items():
    print(v) 

spam = {'color': 'red', 'age':42}
for k,v in spam.items():
    print("Keys: {} and values: {}". format(str(k), str(v)))    

spam = {'nationality': 'ugandan', 'religion':'anglican', 'name': 'gloria'}
just = 'nationality' in spam.values()
print(just)

picnic_items = {'apples': 5, 'cups': 2}
message = 'I am bringing {} cups.' .format(str(picnic_items.get('cups', 0)))
print(message)

#adding onnto the dictionary
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
    print(spam)

#joining dictionaries to be one
spam1 = {'cup': 'drop', 'sound': 'loud'}    
spam2 = {'cry': 'silent', 'report': 'beating'}
spam3 = {**spam1, **spam2}
print(spam3)    
print(" ")

#two ways to create sets a set is an unordered collection with no duplicates you can use it to eliminate or sth
s = {1, 2, 3, 2, 3, 4}
print(s)        #and since they don't allow duplicating thet means on the output theres 
print(" ")      #only one 2 and one 3,  note that you can't access them by "s[0]" because they are an unordered list 

#you can add an element to a cell
g = {1,2,3}
g.add(5)
print(g)
print(" ")

#you can also use .update to add more than one element to a set
g = {1,2,3}
g.update([10, 12, 13, 14])
print(g)
print(" ")

#you can use .remove to remove an element from a set
g = {1,2,3}
g.remove(1)
print(g)
print(" ")

#use .union to merge two sets together, for example
s1 = {1,2,3}
s2 = {4,5,6}
print(s1.union(s2))
print(" ")

#use .intersection were it will return the common members in each set
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.intersection(s2))
print(" ")

#use .difference method to return the members that are unique to the fist set for example
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.difference(s2))
print(s2.difference(s1))
print(" ")

#use .symmetric_difference to return elements that are not common between the two sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.symmetric_difference(s2))
print(" ")

#this is used to subtract one from each of the elements in the list
a = [1, 3, 5, 7, 9, 11]
b = [i-1 for i in a]
print(b)

#an example of set comprehension
b = {"abc", "def"}
{s.upper() for s in b}

#this is a dictionary comprehension were we are going to do something for each element in the dictionary
c = {'name': 'Pooka', 'age': 5}
{v: k for k, v in c.items()}

#escape characters
#if you want to go to a new line
print("Hello there!\nHow are you?\nI\'m doing fine.")

#if you put the letter r to beginning of a string, it becomes a raw string
#and i raw string completely ignores all escape characters and prints any backslash in the string output
print(r"That is Carol\'s cat.")

#research about textwrap import dedent
from textwrap import dedent
def my_function():
    print('''
          dear Alice,
          
          Eve's cat has been arrested for catnapping, cat burglary, and extortion
          
          sincerely,
          Bob
          ''').strip()
    
#slicing the string
spam = 'Hello world! '
print(spam[0])
print(spam[0:5])
print(spam[0:10])
print(spam[ :5])
print(spam[6:])

#boolean in strings
'Hello' in 'Hello World'
'HELLO' in 'Hello World'
'cats' not in 'cats and dogs' 

#checking whether a string is in upper or lower case
spam = 'Hello world'
spam.islower()
spam.isupper()
'HELLO'.islower() 
'Hello world!'.startswith('Hello')   
'Hello world!'.endswith('world!') 

#join
', '.join(['cats', 'rats', 'bats'])
' '.join(['My', 'name', 'is', 'Simon'])

#split 
'My name is Simon'.split() #so normally it splits with spaces
'MyABCnameABCisABCSimon'.split('ABC')  #but you can split with literally anything

#r
'Hello' .rjust(10) # so here the word will be adjusted such the there are 10 characters output will be '      Hello'
'Hello' .rjust(20) # so here the word will be adjusted such the there are 10 characters output will be '            Hello'
'Hello'.rjust(20,'*')
'Hello'.rjust(20,'-')

#center
'Hello'.center(20) #this is going to centre the output with in the given number of characters
'Hello'.center(20, '=')

#strip this removes spaces
spam = '     Hello World     '
spam.strip()

#rstrip
spam.rstrip() #this will just remove the space at the beginning

#lstrip
spam.lstrip #this will remove the space at the end


''' this is for guidance
spam = 'Hello world'
print(spam.islower())

print(spam.isupper())
message = 'HELLO'.islower()
print(message)
'''

def box_print(symbol,width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)
for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('zz', 3, 3)):
    try:
        box_print(sym,w,h)
    except Exception as err:
        print('An exception happened: ' + str(err))      




