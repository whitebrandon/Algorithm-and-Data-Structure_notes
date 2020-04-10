# INTRO TO ALGORITHMS | PART THREE: Algorithms in Code

a COURSE BY TREEHOUSE
taught by Pasan Premaratne

PY CODE by Brandon White | white.brandonsean@gmail.com

## LINEAR SEARCH IN CODE

Linear Search in Python
````
def linear_search(list, target):
    '''
    Returns the index position of the target if found, else returns None
    '''

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return -1
````
````
def linear_search(lst, target):
  '''
  This version calls the enumerate function on the list
  '''
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1
````

Linear Search in JavaScript
````
function linearSearch(array, key){
  for(let i = 0; i < array.length; i++){
    if(array[i] === key) {
        return i;
    }
  }
  return -1;
}
````

## BINARY SEARCH IN CODE

Binary Search in Python
````
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
    return -1
````

Binary Search in JavaScript
````
function binarySearch(array, key) {
    let left = 0;
    let right = array.length - 1;
    while (left <= right) {
        const mid = left + Math.floor((right - left) / 2);
        if (array[mid] === key) {
            return mid;
        }
        if (array[mid] < key) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}
````

## RECURSIVE BINARY SEARCH

Recursive Binary Search in Python
````
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
````

Recursive Binary Search (with start and end position values) in Python
````
def recursive_binary_search(list, target, start=0, end=None):
    if end is None:
        end = len(list) - 1
    if start > end:
        return -1

    mid = (start + end) // 2

    if target == list[mid]:
        return mid
    else:
        if target < list[mid]:
            return recursive_binary_search(list, target, start, mid-1)
        else:
            return recursive_binary_search(list, target, mid+1, end)
````
