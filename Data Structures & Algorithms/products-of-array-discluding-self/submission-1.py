class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
        ans = []
        for i in range(len(nums)):
            if nums[i] != 0:
                ans.append(int(prod / nums[i]))
            else:
                prod_0 = 1
                for j in range(len(nums)):
                    if j != i:
                        prod_0 *= nums[j]
                ans.append(prod_0)
        return ans
