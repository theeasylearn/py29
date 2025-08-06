fruits = {'apple','banana','orange'}
print(fruits)
fruits.add('banana')
fruits.add('kiwi')
fruits.add('graps')
print(fruits)
fruits.remove('kiwi')
print(fruits)

set1 = {1,2,3}
set2 = {3,4,5}

print(set1,set2)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))