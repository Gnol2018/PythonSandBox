
array = [2,3,5,6,7,9]

def binary_search(int_array, find_number):
    low = 0 
    mid = 0
    high = len(int_array) - 1
    while low <= high:
        mid = (low + high) // 2
        if int_array[mid] < find_number:
            low = mid + 1
        elif int_array[mid] > find_number:
            high = mid - 1
        else:
            return mid
        
    return "Not found"
        
x = binary_search(int_array=array, find_number=7)
print("x should be 4: ", x)