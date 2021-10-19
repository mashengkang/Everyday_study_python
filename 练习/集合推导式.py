# coding:utf-8

varset = {1, 2, 3, 4}
# (1)普通推导式
newset = {i << 1 for i in varset}
print(newset)  # {8, 2, 4, 6}

# (2)带有条件表达式的推导式
newset = {i << 1 for i in varset if i % 2 ==0}
print(newset)

# (3)多循环的集合推导式
var1 = {1,2,3}
var2 = {4,5,6}
newset = set()
for i in var1:
    for j in var2:
        newset.add(i+j)
print(newset)  # {5, 6, 7, 8, 9}

newset = {i+j for i in var1 for j in var2}
print(newset)  # {5, 6, 7, 8, 9}

# (4)带条件表达式的多循环的集合推导式
newset = {i+j for i in var1 for j in var2 if i%2==0 and j%2==0}
print(newset)


