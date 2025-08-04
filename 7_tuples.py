#example of tuples 
gods = ('Shiv','Vishnu','Bramha')
devatas = ('India','Suryadev','chandra dev')
print(gods)
print(gods[0])
print(gods[1:3])
print(gods[2:])
print(gods + devatas)
print(gods.count('Shiv'))
print(gods.count('Mahadev'))
print(gods.index('Shiv'))
# print(gods.index('Mahadev')) 

#we can not change any item in tuple as it is immutable
# gods[0] = 'Shankar'
print(gods)