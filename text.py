# dic={1:"a",2:"b",3:{1:"a",2:"b"}}
# for i in dic.items():
#     print(i)
# for i in dic.values():
#     print(i)
# for i in dic.keys():
#     print(i)
# dic2=dic
# dic3=dic.copy()
# print(id(dic)==id(dic2))
# print(id(dic)==id(dic3))


# key=(1,2,3,4)
# values='xyz'
# sqr={}
# sqr=sqr.fromkeys(key,values)
# #sqr.update(sqr.fromkeys(key,values))
# print(sqr)

# std={'name':'bob','age':24}
# print(std.get('name'))
# print(std.get('gender'))
# print(std.get('gender','M'))

# a={1:2,2:3,3:4}
# b={4:5,5:6}
# a.update(b)
# print(a)
# a.pop(2)
# a.popitem()
# print(a)

a={'A':100,'B':540,'C':220}
sum=0
for i in a.values():
    sum=sum+i
print(sum) #860
