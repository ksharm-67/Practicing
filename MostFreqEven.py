class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        mp = {}
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                mp[nums[i]] = mp.get(nums[i], 0) + 1
            
        if not mp:
            return -1

        temp = (-1, -1)
        for key, val in mp.items():
            if val > temp[1]:
                temp = (key, val)
            elif val == temp[1] and temp[0] > key:
                temp = (key, val)
        
        return temp[0]
