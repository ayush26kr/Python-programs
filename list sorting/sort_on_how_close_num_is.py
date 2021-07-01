#sort the given list on how close number is to 50
def myfunc(n):
    return abs(n-50)

list=[44,87,65,98,43,25,12,8,37]
list.sort(key=myfunc)
print(list)