






def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    a = []
    for lst in lists:
        a = a + lst
        
    n = len(a)
    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] =  a[j + 1], a[j]
    return a




def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    # Track current index for each list
    indices = []
    for _ in lists:
        indices.append(0)
    print(indices)
    result = []
    
    while True:
        # Find the list with the smallest current head
        best_val = None
        best_list = -1
        
        for i in range(len(lists)):
            if indices[i] < len(lists[i]):
                val = lists[i][indices[i]]
                if best_val is None or val < best_val:
                    best_val = val
                    best_list = i
        
        # If no list had remaining elements, we're done
        if best_list == -1:
            break
        
        result.append(best_val)
        indices[best_list] += 1
    
    return result



# import heapq

# def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
#     heap = []
#     result = []

#     for i, lst in enumerate(lists):
#         if lst:
#             heapq.heappush(heap, (lst[0], i, 0))

#     while heap:
#         value, list_index, element_index = heapq.heappop(heap)
#         result.append(value)

#         next_index = element_index + 1
#         if next_index < len(lists[list_index]):
#             heapq.heappush(
#                 heap,
#                 (lists[list_index][next_index], list_index, next_index)
#             )

#     return result

# print(merge_sorted_lists([[10], [10], [10]]))



def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    
    n = []
    for i in lists:
         n = n + i
    res = []
    for i in range(len(n)):
        r = min(n)
        res.append(r)
        n.remove(r)
    
    return res


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    result = []
    indexes = [0] * len(lists)
    
    while True:
        smallest = None
        smallest_index = -1
        
        for i in range(len(lists)):
            if indexes[i] < len(lists[i]):
                value = lists[i][indexes[i]]
                if smallest is None or value < smallest:
                    smallest = value
                    smallest_index = i
        if smallest_index == -1:
            break
        
        result.append(smallest)
        indexes[smallest_index] += 1
        
    return result

print(merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]]))