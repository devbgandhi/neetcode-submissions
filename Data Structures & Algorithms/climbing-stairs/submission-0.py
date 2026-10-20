class Solution:
    def climbStairs(self, n: int) -> int:
        two_back = 1
        one_back = 1
        for i in range(2, n+ 1):
            current = one_back+two_back
            two_back = one_back
            one_back = current

        return one_back
        