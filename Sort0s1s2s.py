class Solution:
    def sort012(self, arr):
        
        left, i, right = 0, 0, len(arr) - 1
        
        while i <= right:
            if arr[i] == 0:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
                i += 1
                
            elif arr[i] == 1:
                i += 1
                
            else:
                arr[i], arr[right] = arr[right], arr[i]
                right -= 1
            
        return arr
