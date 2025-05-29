'''
Built in data types
1.List
2.tuple
3.Dictionary
4.set

'''
#creating list
mylist=["vishnu","age",22]
print(mylist)

'''
properties of list

1.Orderd 
 0    1      2      3   4
[1,"salem","mango",2.5,56,"salem",56]
 -5     -4  -3     -2  -1

 '''
print(mylist[0])
print(mylist[0:3])


'''
2.allow duplicates
3.mutable  (add,update,delete)'''

#add
print(mylist)
mylist.append(2025)
mylist.insert(3,21)
print(mylist)
hridhu=[2,'Hridhu',8,]
mylist.extend(hridhu)
print(mylist)




#update
newlist=[1,"hridhu","age",8]
print(newlist[1])
newlist.append(9)
print(newlist)
newlist.insert(2,"VIshnu")
print(newlist)
list2=[2,"sindhu","age",48]
newlist.extend(list2)
print(newlist)
newlist[2]=20
print(newlist)
newlist[0:3]=[2,"Sasi",52]
print(newlist)

#delete
newlist.pop()
print(newlist)
newlist.pop(3)
print(newlist)
newlist.clear()
print(newlist)
del newlist
print(newlist)




      
