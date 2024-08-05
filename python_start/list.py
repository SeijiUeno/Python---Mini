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
# append
motorcycles.append('honda')
print("\nAdding honda in the end with append():\n" + str(motorcycles))
# insert
motorcycles.insert(2,'harley')
print("\nInserting new motorcycle in the list, position 2, using insert()\n" + str(motorcycles))
# del
del motorcycles[2]
print("\nAfter using the Del Statement in position 2, [del]\n" + str(motorcycles))
# pop
popped_motorcycle = motorcycles.pop()
print("\nPrinting motorcycles after .pop()\n" + str(motorcycles))
print("It returns the popped item: " + popped_motorcycle + "\n")
# removing an item by value, remove
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print("\nA " + too_expensive.title() + " is too expensive.")
print("\nAfter removing ducati by value: \n" + str(motorcycles) + "\n")

#Sorting Lists

#sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print("\nAfter using .sort\n" + str(cars))
#sort(reverse)
cars.sort(reverse=True)
print("\nAfter using .sort(reverse=True)\n" + str(cars))
print ("\nSorting it temporarily (sort)\n" + str(sorted(cars)))
#reverse 
cars.reverse()
print("\nAfter using .reverse\n" + str(cars))

#length
length = len(cars)
print ("\nThe list size is " + str(length))

