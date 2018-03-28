

myTuple = (4,5,6,7)

myList = [4,5,6,7]


print(myTuple[0])
print(myList[0])

try:
	myTuple[0] += 10
	
except:
	print('didnt work fo tuple manipulation')

try:
	myList[0] += 10
except:
	print('didnt work for list')

print(myTuple)
print(myList)



