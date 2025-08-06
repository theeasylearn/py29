#create dictionary 
teacher = {'name':'Ankit','surname':'Patel','age':41,'weight':81.00,'gender':True}
print(teacher)
teacher['email'] = 'ankit3385@gmail.com'
teacher['weight'] = 80.00
print(teacher)
del teacher['email']
print(teacher)

#access single key/value pair 
print(teacher['surname'])
# print(teacher['city'])
