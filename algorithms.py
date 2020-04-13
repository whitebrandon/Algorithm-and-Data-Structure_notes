'''
# Linear Search Algorithm

def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)

# Binary Search Algorithm

def binary_search(list, target):
    first = 0
    last = len(list) -1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else: 
            last = midpoint - 1
    return None

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)

# Binary Search Algorithm (with Recursion)

def recusive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recusive_binary_search(list[midpoint + 1:], target)
            else:
                return recusive_binary_search(list[:midpoint], target)

def verify_recursive(result):
    print("Target found: ", result)
result = recusive_binary_search(numbers, 12)
verify_recursive(result)

result = recusive_binary_search(numbers, 5)
verify_recursive(result)
'''
### Arrays
new_list = [1, 2, 3] 

# 1. This allocates a base amount of memory for the array/Python list to use.

# 2. Since this is Python, the values aren't stored in memory. 
#    Instead, the values 1, 2. and 3 are stored elsewhere in memory.
#    And the array stores references to each of those objects.

# 3. To access a value, use a subscript along with an index value.


result = new_list[0] # The square brackets are the subscript

# 4. Accessing is a constant time operation on an array/Python list.
#    Because the array has a reference to the base location in memory and the memory is contiguous, we don't have to iterate over the entire list.
#    For this reason, accessing is a constant time operation on an array/Python list.
