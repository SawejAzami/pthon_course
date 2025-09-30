n=10
for i in range(n-1):
    for j in range(i,n-1,1):
        print(" ",end=" ")
    for j in range(0,2*i+1):
        print("@",end=" ")
    print()


m=n//2+1
for i in range(1,m+1):
    for j in range(i,m,1):
        print(" ",end=" ")
    for j in range(0,i,1):
        print("*",end=" ")
    for j in range(1,m+2):
        if(i==m):
            print("@",end=" ")
        else:
            print(" ",end=" ")
    for j in range(0,i,1):
        print("*",end=" ")
    print()

for i in range(m,0,-1):
    for j in range(i,m+1,1):
        print(" ",end=" ")
    for j in range(0,i-1,1):
        print("*",end=" ")
    for j in range(1,m+2):
        print(" ",end=" ")
    for j in range(0,i-1,1):
        print("*",end=" ")
    print()


#                   @ 
#                 @ @ @ 
#               @ @ @ @ @ 
#             @ @ @ @ @ @ @ 
#           @ @ @ @ @ @ @ @ @ 
#         @ @ @ @ @ @ @ @ @ @ @
#       @ @ @ @ @ @ @ @ @ @ @ @ @
#     @ @ @ @ @ @ @ @ @ @ @ @ @ @ @
#   @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @
#           *               *
#         * *               * *
#       * * *               * * *
#     * * * *               * * * *
#   * * * * *               * * * * * 
# * * * * * * @ @ @ @ @ @ @ * * * * * *
#   * * * * *               * * * * *
#     * * * *               * * * *
#       * * *               * * *
#         * *               * *
#           *               *



n=5
for i in range(0,n):
    for j in range(0,n-i):
        print(" ",end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    for j in range(0,n):
        if(i==n-1):
            print("@",end=" ")
        else:
            print(" ",end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
for i in range(0,n-1):
    for j in range(0,n+1):
        print(" ",end=" ")
    for j in range(0,n):
        print("@",end=" ")
    print()
for i in range(0,n-1):
    for j in range(0,n+1):
        print(" ",end=" ")
    for j in range(0,i):
        print(" ",end=" ")
    for j in range(n-2*i,0,-1):
        print("*",end=" ")
    print()


#           *           *
#         * *           * *
#       * * *           * * *
#     * * * *           * * * *
#   * * * * * @ @ @ @ @ * * * * *
#             @ @ @ @ @
#             @ @ @ @ @
#             @ @ @ @ @
#             @ @ @ @ @
#             * * * * *
#               * * *
#                 *



n=4
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    for j in range(1,n-i):
        print(" ",end=" ")
    for j in range(0,n):
        if(i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
for i in range(n,-1,-1):
    for j in range(0,i+1):
        print("*",end=" ")
    for j in range(1,n-i):
        print(" ",end=" ")
    for j in range(0,n):
        if(i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()

# *
# * *             *
# * * *           * * 
# * * * * * * * * * * *
# * * * * *         * * * *
# * * * * * * * * * * *
# * * *           * *
# * *             *
# *

print()
n=4
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    for j in range(1,n-i):
        print(" ",end=" ")
    for j in range(0,n):
        if(i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
for i in range(0,n-1):
    for j in range(0,n-i-1):
        print("*",end=" ")
    for j in range(0,i):
        print(" ",end=" ")
    for j in range(0,n+1):
        print(" ",end=" ")
    for j in range(1,n-i-1):
        print("*",end=" ")
    print()

# *
# * *             *
# * * *           * *
# * * * * * * * * * * *
# * * *           * *
# * *             *
# *

n=3
for i in range(0,n):
    for j in range(0,2*n-2):
        print(" ",end=" ")
    for j in range(1,n-i):
        print(" ",end=" ")
    for j in range(0,2*i+1):
        print("*",end=" ")
    print()
for i in range(0,n):
    for j in range(0,n*2-1):
        print(" ",end=" ")
    for j in range(0,n):
        if(j==0 or j==n-1):
            print("@",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n-1,-1,-1):
    for j in range(1,n-i):
        print(" ",end=" ")
    for j in range(0,2*i+1):
        print("*",end=" ")
    for j in range(0,n-i-1):
        print(" ",end=" ")
    for j in range(0,n):
        if(i==n-1):
            if(j==0 or j==n-1):
                print("@",end=" ")
            else:
                print(" ",end=" ")
        else:
            print(" ",end=" ")
    for j in range(1,n-i):
        print(" ",end=" ")
    for j in range(0,2*i+1):
        print("*",end=" ")
    print()