class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i,num in enumerate(nums):
            complement = target - num
            
            if complement in res:
                return [res[complement], i]
                
            res[num] = i