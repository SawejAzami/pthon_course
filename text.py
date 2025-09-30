


# # wap to remove duplicate from list
# # wap to count -ve +ve and string type element
# # wap to print all the +ve number in a 
# #wap to print transpose of a mtrix
# # wap to create a flat list from nested list
# # print a reverse order of a nested list

# # list=[[1,2,7],[3,4,8],[5,6,9]]
# # sum=0
# # for i in range(len(list)):
# #     for j in range(len(list[i])):
# #         sum=sum+list[i][j]
# #         print(list[i][j],end=" ")
# #     print()
# # print(sum)

# # pow=[]
# # for i in range(10):
# #     pow.append(3**i)
# # pow=[3**i for i in range(10)]
# # print(pow)

# # even=[x for x in range(10) if x%2==0]
# # print(even)

# # n=4
# # for i in range(n,0,-1):
# #     print(" "*(n-i)+"* "*i)
# # for i in range(2,n+1):
# #     print(" "*(n-i)+"* "*i)


# # for i in range(n):
# #     for j in range(n):
# #         if(i==0 or j==0 or i==n-1 or j==n-1):
# #             print("*",end=" ")
# #         else:
# #             print(" ",end=" ")
# #     print()

# # a=1
# # for i in range(n):
# #     for j in range(i+1):
# #         print(a,end=" ")
# #         a=a+1
# #     print()

# # t1=(1,2,3,4)
# # t2=(1,3,5,6)
# # if(t1[0]==t2[0]):
# #     print(t1+t2)

# # tp1=tuple(input("Enter the tuple").split())
# # tp2=tuple(input("Enter the tuple").split())
# # if(tp1[0]==tp2[0]):
# #     print(tp1+tp2)

# # d=dict()
# # print(d)
# # print(type(d))

# # d={'name':'harsh','empcode':1209,'subject':'python'}
# # print(d['name'])
# # print(d['subject'])

# room={1:'store',2:'kitchen'}
# temp=room[1]
# room[1]=room[2]
# room[2]=temp
# print(room)



# ************************
# dictionery datastucture
# syntax  dict_variable={key1:val,key2:val2,key3:val3......}
# d={} #empty dictionery

# key are unique 

# d=dict()

q={1:"a",2:"b",3:"c",'A':34}
print(q[2]) # b
print(q['A']) #34
q['B']=12
print(q) #{1: 'a', 2: 'b', 3: 'c', 'A': 34, 'B': 12}
q[2]="hello"
print(q) #  {1: 'a', 2: 'hello', 3: 'c', 'A': 34, 'B': 12}

# deleting the items
# q.clear() # clear all entries here q will exist
# print(q) 3{}
# del(q) # it will remove the existance of the q from the memory
# print(q)  #name 'q' is not defined

# to delete the particular key from the dictionery
# dictioneryName.pop(key,[value is optional])
print(q.pop(1)) # a
print(q.pop(12,"hi")) # it will give "hi" if key is not present
print(q) #{2: 'hello', 3: 'c', 'A': 34, 'B': 12}
# q.pop(1)
# print(q) # KeyError: 1
# dictioneryName.popitem() # it will delete the any random key
q.popitem()  # it will delete the last key
print(q)
a={ 3: 'c',2: 'hello', 4: 34}
sorted(a.items())  #{3: 'c', 2: 'hello', 4: 34} it not sorting why?
print(a)