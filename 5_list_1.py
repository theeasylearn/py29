#concept of list 
list = ['Ankit Patel',100,3.14,True,None]
#           0           1   2   3   4
print(list)
#access 1st item 
print(list[0]) #ankit patel

#access 2nd item
print(list[1]) # 100

#display 2 items from begining 
print(list[0:2]) #Ankit Patel 100

#print last 3 items 
print(list[2:])

#print list 3 times
print(list * 3)

another_list  = [200,300]
print(list+another_list)

#insert new item at the begining of the list 
list.insert(0,"Apple")
# 'Apple', 'Ankit Patel', 100, 3.14, True, None
list.insert(0,500)
# 500,'Apple', 'Ankit Patel', 100, 3.14, True, None
list.insert(0,1000)
# 1000,500,'Apple', 'Ankit Patel', 100, 3.14, True, None
list.insert(1,'kiwi')
# 1000,Kiwi,500,'Apple', 'Ankit Patel', 100, 3.14, True, None
list.insert(2,'banana')
# 1000,Kiwi,'banana',500,'Apple', 'Ankit Patel', 100, 3.14, True, None

#insert at end 
list.append('Bhavnagar')
list.append(True)
print(list)

#we can delete item from list 
del list[0]  #delete item @ 1st position
del list[0]  #delete item @ 1st position
del list[2]  #delete item @ 1st position
print(list)

print(len(list))
del list[len(list)-1]
print(list)
# we cal remove all items 
list.clear()
print(list)

#we can edit list
another_list[0] = "pinapple"
print(another_list)