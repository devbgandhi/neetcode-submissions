class Solution:
    def rob(self, nums: List[int]) -> int:
        one_back = 0
        two_back = 0
        loot = 0
    
        for money in nums:
            rob = two_back + money
            skip = one_back
            loot = max(rob, skip)

            #increment
            two_back = one_back
            one_back = loot

        return one_back