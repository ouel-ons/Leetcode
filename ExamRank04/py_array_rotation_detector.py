




def array_rotation_detector2(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    if len(arr1) == 0:
        return True
    return any(arr1[i:] + arr1[:i] == arr2 for i in range(len(arr1)))

def array_rotation_detector1(arr1: list, arr2: list) -> bool:
    if  len(arr1) != len(arr2):
        return False
    
    if len(arr1) == 0:
        return True
    
    doubled = arr1 + arr2
    n = len(doubled)
    
    for i in range(n):
        if doubled[i:i+n] == arr2:
            return True
    return False

def array_rotation_detector0(arr1: list, arr2: list) -> bool:
    if  len(arr1) != len(arr2):
        return False
    
    if len(arr1) == 0:
        return True
    
    doubled = arr1 + arr1
    n = len(arr1)
    
    for i in range(n):
        if doubled[i:i+n] == arr2:
            return True
    return False

# print(array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))
# print(array_rotation_detector([1, 2, 3], [3, 2, 1]))
# print(array_rotation_detector([1, 2, 3], [1, 2, 3]))
def array_rotation_detector3(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    return arr2 in (arr1 + arr1)

def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False

    if len(arr1) == 0:
        return True

    l = arr1 * 2
    n = len(arr1)
    for i in range(n):
        if l[i:i+n] == arr2:
            return True

    return False

print(array_rotation_detector([1, 2, 3, 6, 9], [6, 9, 1, 2, 3]))