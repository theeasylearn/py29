#create dictionary 
teacher = {'name':'Ankit','surname':'Patel','age':41,'weight':81.00,'gender':True}
print(teacher)
#it will update age keys value 
teacher.update({'age':42})

#it will add new key value pair 
teacher.update({'city':"bhavnagar"})

print(teacher)

#last key value pair
teacher.popitem()
print(teacher)

teacher.pop('weight')
print(teacher)

print(teacher.values())
print(teacher.keys())

list = ['from','to','distance','price','type']

#create dicitionary using list 
bus = dict.fromkeys(list)
print(bus)
bus.update({'price':1000})
print(bus)

bus.clear()
print(bus)
print(teacher.items())