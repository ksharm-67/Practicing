class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res, curr = 1, 0
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                curr += 1
                res += curr
            else:
                curr = 0
            res += 1

        return res
