#list
#list canot be spread

list = ["apple","mango","orange","grapes"]
print(type(list))

for x in list:
    print(x)

list[3] = "strabrery"
print(list)
print(list.pop())
list.insert(0,"banana")
print(list)

#tuple
print()
tuple1=("car","van","bike")
print(tuple1)
print(type(tuple1))


list.extend(tuple1)
print(list)


#set
print()
set1 = {'a','b','c','d'}
print(set1)
print(type(set1))

set2 = {'a','b','c','d','a'}
print(set2)

set2.add('e')
print(set2)
