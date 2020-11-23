def BinarySearchFunction (array , first , last , key):
	array.sort()
	if last >= first :
		mid = (first + last) // 2
		if array[mid] == key :
			return mid
		elif array[mid] > key :
			last = mid - 1
			return (BinarySearchFunction (array , first , last , key))
		elif array[mid] < key :
			first = mid + 1
			return (BinarySearchFunction (array , first , last , key))
		else :
			return -1
			
arr = [5,2,9,8,7,10]
x = 0
result = BinarySearchFunction(arr , 0 , len(arr)-1 , x)			

if result != -1: 
    print("Element is located at : ", result) 

