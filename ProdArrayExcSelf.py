class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod = 1
        products = []

        for i in range(len(nums)):
            if i == 0:
                products.append(1)    
            else:
                prod *= nums[i - 1]
                products.append(prod)

        prod = 1
        for j in range(len(nums) - 1, -1, -1):
            products[j] *= prod
            prod *= nums[j]
        
        return products
