class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_al = [ch for ch in s if ch.isalnum()]

        l=0
        r=len(only_al)-1

        while l<r:
            if only_al[l].lower() != only_al[r].lower():
                return False
            l +=1
            r -=1
        
        return True