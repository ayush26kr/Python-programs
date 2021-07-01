mylist=["apple","mango","banana","cherry"]
print(mylist)
print(mylist[1:3])
if "mango" in mylist:
    print("yes it is there")
mylist[1]="black-cherry"
print(mylist)

#inserting element to the list
mylist.insert(2,"guava")
print(mylist)
#removng element from the list
mylist.remove(mylist[1])
print(mylist)
#adding element to the end 
mylist.append("banana")
print(mylist)

#adding to list (extend)
newlist={"pencil","eraser","box"}
mylist.extend(newlist)
print(mylist)

#pop
newlist.pop()   #if index not specified it will pop out last element
print(newlist)

#printing list elements one by one (referrring the elements)
for x in newlist:
    print(x)

#printing list elements referring the index
l=["monkey","elephant","zebra","kangaroo","dog"]
for x in range(len(l)):
    print(l[x])