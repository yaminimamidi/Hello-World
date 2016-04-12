list = ['one','two','three',4,5]
print list

for x in list:
 print x

 # add new list to the old elements.
new_list =[6,7]
list =list + new_list
print list


list.append('hi! there')
print list
print list.pop()


list.reverse()
print list

list.sort()
print list


list.remove(7)
print list

list.reverse()

print list

# How do I index a nested list?
# For example if I want to grab 2 from [1,1,[1,2]]?

x = [(1,2),(3,4),(5,6)]
for y in x:
 print y

print x[2][1]



z = ['1,2','3,4','5,6']
for x in z:
 print x

print z[2][0]
















