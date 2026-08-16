class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        to_positive = 0
        arr = nums[:]

        for i in range(len(arr) - 1):
            if arr[i] == -1:
                to_positive += 1
                arr[i] = 1
                arr[i + 1] *= -1

        if arr[-1] == 1 and to_positive <= k:
            return True

        to_negative = 0
        arr = nums[:]

        for i in range(len(arr) - 1):
            if arr[i] == 1:
                to_negative += 1
                arr[i] = -1
                arr[i + 1] *= -1

        return arr[-1] == -1 and to_negative <= k
