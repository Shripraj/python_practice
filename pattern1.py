##printing star pattern
# * * * *
# * * * *
# * * * *
# * * * *
for i in range(0,4):
    for j in range(0,4):
        print("* ",end=" ")
    print()
print("\n")
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
for i in range(0,4):
    for j in range(0,4):
        print(i ,end=" ")
    print()
print("\n")
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
for i in range(0,4):
    for j in range(0,4):
        print(j+1 ,end=" ")
    print()
print("\n")
# 1 2 3 4   1 2 3 4   
# 1 2 3 4   1 2 3 4
# 1 2 3 4   1 2 3 4   
# 1 2 3 4   1 2 3 4
for i in range(0,4):
    for j in range(0,4):
        print(j+1," " , end=" ")
    for k in range(0,4):
        print(k+1,end=" ")
    print()
print("\n")