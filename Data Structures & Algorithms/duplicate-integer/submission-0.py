class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for n in nums:
            if n in num_dict.keys():
                return True
            num_dict[n] = 0
    
        return False