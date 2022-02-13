from unittest.mock import mock_open


names = ["Sharique","Ahmed","Bilal"]

# names1 = ['string',1,True,1.0,['list','one']]

print(names)

names = ["sharique","ahmed","bilal"]
#for names in name
message = print(f"My first Name is {names[0].title()}")
print(message)

name = 'sharique'
#for name in names
    print(f"hello {name}"!)


motorcycle = ["honda","suzuki","yamaha"]
print(motorcycle)
popped_motorcycle = motorcycle.pop(2)
print(motorcycle)
print(popped_motorcycle)

motorcycle = ["honda","suzuki","yamaha"]
print(motorcycle)
motorcycle.remove('honda')
print(motorcycle)

motorcycle = ["honda","suzuki","yamaha"]
print(motorcycle)
motorcycle.insert('ducati')
print(motorcycle)

motorcycle = ["honda","suzuki","yamaha"]
print(motorcycle)
motorcycle.reverse(False)
print(motorcycle)


motorcycle = ["honda","suzuki","yamaha"]
print(motorcycle)
','.join(motorcycle)

motorcycle = ["honda","suzuki","yamaha"]
for i in range(0,len(motorcycle),2):
    print(motorcycle)




