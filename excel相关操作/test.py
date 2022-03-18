lis = ['apple','lemon','pear','peach']
def fn(x):
    return x[::-1]

lis.sort(key=fn,reverse=True)
print(lis)