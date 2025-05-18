# typecasting i) implicit and explicit
# datatype
# to run the python file ->python file.py
# we use ** for exponetial expression -> 2**4=16

#  a,b,c=input("enter the number").split()
##  it is use to take multiple input in same line

# ********To print in same line******
print(sum,end=" ")

## how to take input
a=int(input("enter the number"))


## to round off the digits near to integer place ,
rounded=round(k,2)
# exmple->
rounded=round(2.9858734,2)
print(rounded)

## to check the list of keyword
import keyword
print(keyword.kwlist)

## type() is use to check the data type of a variable
a=23
print(type(a))

## id() give the unique id for a given object or variable or values
a=23
id(a)


## dir() is a vital function that return all the property and method associated with object

## operator
Arithmetic  #-> +,-,*,/,%
logical #-> and,or,not
relational  # it give answer in boolean form #-> >,<,==,!=,<=,>=
assignment  #-> =+,=-,=*,=/,
bitwise #-> &,|,~,^,>>,<<
8<<2 -> 8*2*2-> 32 is answer
8<<3-> 8*2*2*2-> 64

9>>3 ->9/2*2*2-> 1

# ^ XOR bit operator give the result high if input of high are odd then result is true , if input of high are even then result is false
identity and membership

#define the string
text="hello world"
# or
text=input("enter the text")

print(text[2])
# =>l
print(text[2:6])  # it will give a sub string from index 2 to 6-1

# text="Shenanigan"
# print(text[0:2])
# print(text[8:10])
# print(text[2:10])
# print(text[0:6])
# print(text)
# print(text[0:10:2])
# print(text[0:10:3])
# print(text[0:10:4])
# print(text+" type")
# print(text[0:6]+"Wabbite")


# text1="hii"
# print(text1*3)  # # it will give the string 3 times

# # len() it is use to find the length of string
# print(len(text1))

# #print first middle and last character
# a=input("enter the text")
# b=len(a)
# # m=a[b//2]
# # m=int(len(a)//2)
# m=int(len(a)/2)
# print(a[0]+a[m]+a[-1])

##print three middle character

# print(a[m-1]+a[m]+a[m+1])


## use of String.isalnum

# a="abes2345"
# print(a.isalnum())

## isdigit() is return true if it contain only digit
## islower() return true if string has lower case
## isspace() return true if string contain only whitespace
## istitle() return true if starting  letter of each words are capital
# isupper() return true if string has Upper case
# isalpha() to check it is alphabet or not
## replace(old,new)
## replace("old","new",max) replace all occurrance of old in string with new

# ******* odd or even
# n=int(input("enter the number to check where it is odd or even"))
# if (n%2==0):
#     print("even")
# else:
#     print("odd")

# ************ if number is +ve then increment by one

# n=int(input("enter the number"))
# if(n>0):
#     print(n+1)
# else:
#     print("number is not +ve")

# ********** find it is number or alphabet

# ***************write a program to promt the user to enter the number

n=int(input("enter the number"))

if(n<=10 and n>=1):
    print("between 1 nad 10")
elif(n<=20 and n>=11):
    print("between 11 and 20")
elif(n<=30 and n>=21):
    print("between 21 and 30")
elif(n<=40 and n>=31):
    print("between 31 and 40")
elif(n<=50 and n>=41):
    print("between 41 and 50")
else:
    print("greater than 50")

# ********** write a program to determine wether a person is eligible to vote or not if not then find how many year remain to vote

n=int(input("enter the number"))
if(n<18):
    print("not eligible to vote")
    print("after",18-n,"year is eligible to vote")
else:
    print("eligible to vote")


# ********A COMPANY DECIDE TO GIVE BONUS TO ALL EMPLOYE A 5% BONUS ON SALARY IS GIVEN TO MALE WORKER AND 10% GIVEN TO WOMEN WORKER , WRITE A PROGRAM TO ENTER THE SALARY AND GENDER  , IF THE SALARY OF EMPLOYE IS LESS THEN 10000 THEN GIVE EXTRA 2% BONUS on salary , CLCULATE THE TOTAL BONUS OF EMPLOYE AND DISPLAY IT

gender=input("enter the gender of employe")
salary=int(input("enter the salary of employe"))

if(gender=='M'):
    if(salary<=10000):
        print("Bonus of Male employe is ",salary*.07)
    else:
       print("Bonus of Male employe is ",salary*.05)
else:
    if(salary<=10000):
        print("Bonus of Female employe is ",salary*.12)
    else:
       print("Bonus of Female employe is ",salary*.10)

# ******************* while loop
# write a program to print the number from 1 to 5
i=1
while(i<=5):
    print(i)
    i=i+1  # increment or decrement operator are not used in python

#  write a program to print all the number in the range from m to n
m=int(input("enter the number m"))
n=int(input("enter the number n"))
while(m<=n):
    print(m)
    m=m+1
# ************* average
m=int(input("enter the number m"))
n=int(input("enter the number n"))
sum=0
k=n-m+1
while(m<=n):
    sum=sum+m
    m=m+1
print(sum)

print(k)
avg=sum/k
print("average :",avg)

# **************count even and odd
m=int(input("enter the number m"))
n=int(input("enter the number n"))
even=0
odd=0

while(m<=n):
    if(m%2==0):
        even=even+1
    else:
        odd=odd+1
    m=m+1

print("number of even: ",even)
print("number of odd: ",odd)

#  write a program to read a character until a * is encounter
#  and also count the number of uppercase and lowercase and number enter by the user
n=input("enter the value and if you want to stop then enter *")
lower=0
upper=0
num=0
while(n!="*"):
    n=input("again enter")
    if(n.islower()==True):
        lower=lower+1
    elif(n.isupper()==True):
        upper=upper+1
    elif(n.isdigit()==True):
        num=num+1
    else:
        break
print("lower:",lower)
print("upper:",upper)
print("number:",num)

# # loop************
# while(condition):
#     statement 1
#     statement 2
# statement 3

a=1
sum=0
while(a<=10):
    sum=sum+a
    a=a+1
print("sum:",sum)
print("avg:",sum/10)

#************* Question **********
#1. WAP that counts the number of lowercase characters, uppercase characters and
#digits entered by the user

# 2. WAP that prompts user to enter a number. If a number is equal to 99, print "Congratulations".
#If the number is less than 99, print - enter again and aim higher else print enter again a lower
#number. The program run until the user guesses the correct number that is 99.

#3. WAP to sum the series 1^2/1 + 2^2/2 + 3^2/3 + .....+n^2/n
#4. WAP to sum the series 1^1/1 + 2^2/2 + 3^3/3 + .....+n^n/n
#5. WAP that prompts the user to enter 5 words. If the length of any word is less than 6 characters
# then it asks the user to enter it again . However if the word is of 6 or more characters, then it
#displays it on screen.

#WAP to print FloyD's triangle


# Write a program to print numbers from 0 to 10 using  while loop.
#2. Write a program to print numbers from 0 to 10 and 10 to 0 using two while loops.
#3. WAP to calculate the sum and average of first 10 numbers .
#4. WAP to calculate the sum of numbers from m to n.
#5. Write a program that prompts the user to input a series of integers until the user stops
#entering 0 using a while loop. Calculate and print the sum of all the positive integers
#entered.
#6. Write program to print the factorial of the number using a while loop.
#7.Write program that prompts the user to enter a positive integer. It then calculates and
#prints the factorial of that number using a while loop.


#3. WAP to sum the series 1^2/1 + 2^2/2 + 3^2/3 + .....+n^2/n

i=1
n=3
sum=0
while(i<=n):
    sum=sum+i**2/i
    print(sum,end=" ")
    i=i+1
   
print("sum=",sum)

#5. WAP that prompts the user to enter 5 words. If the length of any word is less than 6 characters
# then it asks the user to enter it again . However if the word is of 6 or more characters, then it
#displays it on screen.
"""a1=input("enter ")
print(len(a1))"""
a,b,c,d,e=input("enter the 5 words more than 6 character").split()


if(len(a)<6 and len(b)<6 and len(c)<6 and len(d)<6 and len(e)<6):
    print("enter the words again") 
else:
    print(a,b,c,d,e)

#******* For Loop *******

# for i in range(start,stop,step):  
# bydefault start=0, step=1,stop will be stop-1


# sum=0

# for i in range(1,11,1):
#     print(i,end=" ")
#     sum=sum+i
# avg=sum/10
# print(sum)
# print(avg)

# sum=0

# for i in range(2,22,2):
#     print(i,end=" ")
#     sum=sum+i
# avg=sum/10
# print(sum)
# print(avg)

# sum=0
# for i in range(1,25,4):
#     print(i,end=" ")
#     sum=sum+i
# avg=sum/6
# print("")
# print(i)
# print(sum)
# print(avg)


# sum=0
# for i in range(3,33,3):
#     print(i,end=" ")
#     sum=sum+i
# avg=sum/10
# print("")
# print(sum)
# print(avg)

#************** Fibonacci series upto n terms

n=int(input("enter the number"))
a=0
b=1
for i in range(1,n+1,1):
    print(a,end=" ")
    sum=a+b
    a=b
    b=sum

#************* Factorial from 1 to 10
fact=1
for j in range(1,11,1):
    for i in range(1,j+1,1):
        fact=fact*i
    print(fact,end=" ")
    fact=1

# ******* check Prime number

n=int(input("enter the number to check for prime"))
flag=0
for i in range(2,n,1):
    if(n%i==0):
        flag=1
if(flag==1):
    print("it is not prime number")
else:
    print("it is prime")


#  ********** print prime number from 1 to 100

for j in range(1,100,1):
    flag=0
    for i in range(2,j,1):
        if(j%i==0):
            flag=1
    if(flag==0):
        print(j,end=" ")
    
# ******************pattern 

for i in range(0,5,1):
    for j in range(0,5,1):
        if(i==4 or j==0):
            print("*",end="")
        else:
            print(" ",end="")
    print("")

*    
*
*
*
*****


for i in range(0,5,1):
    for j in range(0,5,1):
        if(i==4 or i==0 or j==0 or j==4):
            print("*",end="")
        else:
            print(" ",end="")
    print("")

*****
*   *
*   *
*   *
*****


for i in range(0,5,1):
    for j in range(0,3,1):
        if(i==4 or i==0 or j==0 or j==2):
            print("*",end="")
        else:
            print(" ",end="")
    print("")

***
* *
* *
* *
***


#  **********************  List 
# list are used to store multiple items or valuein single variable
list1=[]  # how to declare

list1=[1,2,3,4]
print(list1)  #[1, 2, 3, 4]

list2=[[1,2],[3,4]]
print(list2) #[[1, 2], [3, 4]]

list3=[1,"hello",2.5,True]
print(list3) #[1, 'hello', 2.5, True]
print(list3[1]) #hello
print(list3[-1]) # true
print(list3[-2]) #2.5
print(list3[1:]) #['hello', 2.5, True]
print(list3[1:2]) #['hello']

# list3=[1,"hello",2.5,True]

# append()   add a single item at last
# extend() add a multiple item at last
# insert(index,value)

list3.append(40) #[1, 'hello', 2.5, True, 40]
list3.extend([20,30,40])  #[1, 'hello', 2.5, True, 20, 30, 40]
list3.insert(2,"world") #[1, 'hello', 'world', 2.5, True]

# remove(value to remove) it remove first occurrence value
#pop()  remove last item
#del  remove given index item
# clear() empty the list


del list3[2]  #[1, 'hello', True]
list3.pop()  #[1, 'hello', 2.5]
list3.clear() #[]
list3.remove(2.5)  #[1, 'hello', True]
list3.index(1)

print(list3)




# insert 10 number in a list and place each variable into  another list according to their even and odd list

i=0
list=[]
listEven=[]
listOdd=[]
while(i<10):
    i=i+1
    a=int(input("enter the number"))
    list.append(a)

for var in list:
    if(var%2==0):
        listEven.append(var)
    else:
        listOdd.append(var)

print(listEven)
print(listOdd)

# for var in list[1,3]:    // it will print from 1 to 3 index value



# ***************sort
#    In sort suffeling is done in original list  and sort in increasing order
# ************ sorted
#  it will sort the list in new list 
#  syntax   newlist=sorted(oldlist,reverse=false)  
# when reverse is false then it will sort in increasing order


list=[1,43,56,4,7,9,2,23]
list.sort()
print(list)  #[1, 2, 4, 7, 9, 23, 43, 56]
list.reverse()   #[56, 43, 23, 9, 7, 4, 2, 1]
print(list)

list1=[2,3,1,5,7,5,9,6,8]
newlist=sorted(list1,reverse=False)
print(newlist)   #[1, 2, 3, 5, 5, 6, 7, 8, 9]

#  ******** len(list)  will count the number of element
# ********* list.count(element) count the number of element
# ******** list.index(elm) find the index of element

list=[1,2,3,4,4,6,8,9,4,5]

print(len(list)) #8

print(list.count(4))  #3



# write a program to remove all occurrance of particular element from list

# list=[1,5,4,3,4,5,3,4,5,6,3,9,5,5]
# print(list)
# elm=5
# c=list.count(elm)
# for i in range(c):
#     list.remove(elm)   
# print(list)


# write a program to remove all occurrance of particular element from list

list1=[1,5,5,4,3,4,5,3,4,5,6,3,9,5,5]
print(list)
elm=5

for i in list1[:]:  # Creates a shallow copy of the list
    if i == elm:
        list1.remove(i)

# for i in list1:
#     print(i)
#     if(i==elm):
#         print(i)
#         list1.remove(i)
#         print(list1)
print(list1,end= " ")

# WAP to find a maximum number in list
#***************** enumerate are used to track index and value

list2=[1,5,4,3,4,5,3]
for value,index in enumerate(list2):
    print(f"value:{value} ,Index:{index}")
#  f -> fString
# value:0 ,Index:1
# value:1 ,Index:5
# value:2 ,Index:4
# value:3 ,Index:3
# value:4 ,Index:4
# value:5 ,Index:5
# value:6 ,Index:3

# ****************WAP to count the number of string from a given list ofstring. the string is 2 or more and first and last character are the same ***********


#***********************************#
ready=[]
ready.extend([20,40,60,70])
ready.pop()
ready.extend([40,60,70])
print(ready)
print(ready.index(40))

print(ready.count(70))
k=sorted(ready,reverse=True)
print(k)
#***********************************#

# write a program to take list of fruits from  user and print only those fruits name that have 'a' in it

# fruits=[]
# i=0
# while(i<5):
#     i=i+1
#     fruit=input("enter the fruits name")
#     fruits.append(fruit)

# list=[]
# for i in fruits:
#     if 'a' in i:
#         list.append(i)

# print(list)
# print(fruits)

# ********* other method list comprehension

list=['apple','banana','kiwi','papaya']
newlist=[x for x in list if 'a' in x]
print(newlist)
print(list)


# write a program to write a title case

list=["hello","hi","only","laptop"]
newlist=[x.title() for x in list]
print(newlist) #['Hello', 'Hi', 'Only', 'Laptop']


# write a program to write a title case

list=["hello","hi","only","laptop"]
newlist=[x.title() for x in list if 'a' in x]
print(newlist)  #['Laptop']


# write a program to print all the odd number in range 1 to 20 using list comprehension
list=[x for x in range(1,20) if x%2!=0]
print(list)  #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# write a prgram to copy only those value from list that are not integer
list=[1.2, 3.3, "5", 7, 9, "11", 13, "15", 17, 19]
newlist=[x for x in list if type(x)!=int]
print(newlist)

# write a program to print all the odd number in range 1 to 20 using list comprehension
# list=[x for x in range(1,20) if x%2!=0]
# print(list)  #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# # write a prgram to copy only those value from list that are not integer
# list=[1.2, 3.3, "5", 7, 9, "11", 13, "15", 17, 19]
# newlist=[x for x in list if type(x)!=int]
# print(newlist)

fruits=["orange","apple","cherry","kiwi","mango"]

newlist=[x if x!="banana" else "orange" for x in fruits]
print(newlist)

## write python Fibonacci series program using while loop

a=0
b=1
n=5
while(n!=0):
    n=n-1
    c=a+b
    print(c)
    a=b
    b=c

##  number of digits

n=int(input("enter the number"))
count=0
while(n>0):
    n=int(n/10)
    count=count+1
print(count)

## sum of natural number

n=int(input("enter the number"))
sum=0
while(n>0):
    sum=sum+n
    n=n-1
print(sum)

#  square from 1 to 10

n=1
while(n<=10):
    print(n*n)
    n=n+1

## print table of any number

num=int(input("enter the number"))
n=1
while(n<=10):
    print(num*n)
    n=n+1

# print odd and even
n=1
odd=[]
even=[]
while(n<=50):
    if(n%2==0):
        even.append(n)
    else:
        odd.append(n)
    n=n+1
print(odd)
print(even)

#******* function in python
def sum():
    return 10
print(sum()) #10

# with argument

def sum1(a,b):
    c=a+b
    print(c)
sum1(10,50) #60

#**** type of argument
# default
# keyword
# positional
# arbitrary

# default
def sum2(a,b=40):
    c=a+b
    print(c)
sum2(10) #50

#keyword - here we define the keyword during calling of function so we use same name in the parameter ,order is not neccessary
def sum3(a,b,c):
    return a+b+c
print(sum3(a=10,b=20,c=30)) #60

# positional
def sum4(x,y):
    return x
print(sum4(10,20)) #10

#arbitrary
def num(*args):
    for i in args:
        print(i,end=" ")
num(1,2,3,4,5) #1 2 3 4 5


# *********** type of variable
# global 
# logcal
# non local