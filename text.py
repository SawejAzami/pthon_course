
# set****************
# a set is another data collection data type in python ,which store unique element in an unordered way
# Every element ins set are is unique and immutable
# set items can not be access using indexes

# create empty set  
s1=set()
# print(s1) #set()
s1={1,10,2,34,23,2,3,7,4,5,6,1,2,3,4,5,1}
print(s1) #{1, 2, 3, 4, 5, 6}
# for i in s1:
#     print(i)

s2=set("ABESEC")
print(s2)
# print(s2[0]) #TypeError: 'set' object is not subscriptable

# copy method provide the a fresh with different memory location
s3=s2.copy()
print(s3)

# by copy() method memory location will be different
print(id(s2))
print(id(s3))

s4=s2
# by this memory location will be same
print(id(s4))
print(id(s2))

# s2.clear() will remove all the element

# s2.add(value) will add one element in set

# s2.update([value1,value2,...]) will add many element in set
set4=set()
set4.update([1,2,3,4,5,6])
print(set4)

prime=set()
odd=set()
for i in range(1,51):
    if(i%2==1):
        odd.add(i)
print(odd)
