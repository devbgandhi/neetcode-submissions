class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def house(houses):
            one_back = 0
            two_back = 0
            loot = 0

            for money in houses:
                rob = two_back + money
                skip = one_back
                current = max(rob, skip)

                two_back = one_back
                one_back = current

                
            return one_back

            
        return max(house(nums[1:]), house(nums[:-1]))

        
        