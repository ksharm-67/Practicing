
def findFirstOccurrence(nums, target):
    if len(nums) == 1 and nums[0] == target: return 0
    if len(nums) == 1 and nums[0] != target: return -1
     
    low, high = 0, len(nums) - 1
    possible = []
    
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            possible.append(mid)
            high = mid - 1
                    
        elif nums[mid] < target:
            low = mid + 1
            
        else:
            high = mid - 1
            
    if possible: return min(possible)
    return -1
