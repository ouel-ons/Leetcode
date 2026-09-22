def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    
    # Invalid inputs
    if n == 0 or k <= 0 or k > n:
        return []
    
    result = []
    
    # Deque stored as a list of indices, with a head pointer
    # to avoid pop(0) cost. Values in the deque are in decreasing order.
    deque = []
    head = 0
    
    for i in range(n):
        # Remove indices that have fallen out of the window
        if head < len(deque) and deque[head] <= i - k:
            head += 1
        
        # Remove indices whose values are smaller than nums[i]
        # (they can never be the max while nums[i] is in the window)
        while len(deque) > head and nums[deque[len(deque) - 1]] <= nums[i]:
            deque.pop()
        
        # Add the current index
        deque.append(i)
        
        # Once we've filled a full window, record the max (front of deque)
        if i >= k - 1:
            result.append(nums[deque[head]])
    
    return result

print(sliding_window_maximum([1, 2, 3, 4, 5], 2))