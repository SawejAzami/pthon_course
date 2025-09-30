# ***************** Lambda function 

increament=lambda x:x+5
print(increament(5))

add=lambda x,y:x+y
print(add(5,6))

multi=lambda x,y,z:x*y*z
print(multi(5,6,3))

# higher order function 

def fun1(a):
    return a

def fun2(fun):
    a=10
    return fun(a)

print(fun2(fun1))

# fun1 is first class function
# fun2 is higher order function

def fun3(x,y):
    return x+y

def fun4(fun,x,y):
    return fun(x,y)

print(fun4(fun3,10,30))

