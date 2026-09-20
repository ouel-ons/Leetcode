


def list_intersection_finder(lists: list[list[int]]) -> list[int]:

    if not lists:
        return []
    for lst in lists:
        if not lst:
            return []
    
    common = set(lists[0])
    
    for lst in lists[1:]:
        common &= set(lst)
        if not common:
            return []
    print("he")
    return sorted(common)

def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists or any(not lst for lst in lists):
        return []
    common = set.intersection(*(set(lst) for lst in lists))
    return sorted(common)

def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists or any(not lst for lst in lists):
        return []
    common = set(lists[0])
    for lst in lists[1:]:
        common &= set(lst)
    print("me")
    return sorted(common)



def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    
    if len(lists) == 0:
        return []
    for lst in lists:
        if len(lst) == 0:
            return []
        
    common = []
    for x in lists[0]:
        found = False
        for y in common:
            if y == x:
                found = True
                break
        if not found:
            common.append(x)
            
    result = []
    for x in common:
        in_all = True
        for lst in lists[1:]:
            found = False
            for y in lst:
                if y == x:
                    found = True
                    break
            if not found:
                in_all = False
                break
        if in_all:
            result.append(x)
    
    n = len(result)
    
    for i in range(n):
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    
    return result
    
    
    
    

print(list_intersection_finder([[9, 2, 3], [9, 3, 4], [9, 3, 5]]))
print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))
print(list_intersection_finder([[1, 2, 3], [2, 3, 4], []]))