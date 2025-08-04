#list related methods 
fruits = ['apple', 'banana', 'orange', 'grape', 'mango','apple']
grains = ['rice', 'wheat', 'oats', 'barley', 'corn']

print("Fruits:", fruits)
print("Grains:", grains)
fruits.extend(grains)
print("now Fruits has : ", fruits)

print("position of rice ",fruits.index('rice'))
# if index method can not find nuts it will raise ValueError and stop program
# print("position fo rice ",fruits.index('nuts')) 

item = fruits.pop(1)
print("remove 1st item",item)
print("count of apple ",fruits.count('apple'))
print("count of banana ",fruits.count('banana'))

fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

#we cant copy one list into another list using = operator. = operator create reference 
# of list into another variable. so we change any variable other variable will also change 
# wrong way 
# copy_of_fruits = fruits 
copy_of_fruits = fruits.copy()
print(fruits)
print(copy_of_fruits)

copy_of_fruits.clear()

print("after delete all items from copy_of_fruits")
print(fruits)
print(copy_of_fruits)
