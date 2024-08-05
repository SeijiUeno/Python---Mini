#simple lists in python

bicycles = ['treak', 'cannondale', 'redline', 'specialized']
print("Print of representation list\n" + str(bicycles))
print("\nPrint of First element + title() to capitalize it:\n" + bicycles[0].title() + '.')

#Modifying elements

motorcycles = ['honda', 'yamaha', 'suzuki']
print("\nBefore modification -> " + str(motorcycles))
motorcycles[0] = 'ducati'
print("\nAfter modification -> " + str(motorcycles))

#Add new element to the end of the list

motorcycles.append('honda')
print("\nAdding honda in the end with append():\n" + str(motorcycles))

motorcycles.insert(2,'harley')
print("\nInserting new motorcycle in the list, position 2, using insert()\n" + str(motorcycles))

del motorcycles[2]
print("\nAfter using the Del Statement in position 2, [del]\n" + str(motorcycles))

