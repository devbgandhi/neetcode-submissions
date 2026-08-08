class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        have = {}
        
        required = len(need)
        formed = 0

        left = 0
        min_len = float("inf")
        result = [-1, -1]

        for right in range(len(s)):
            char = s[right]
            have[char] = have.get(char, 0) + 1

            if char in need and have[char] == need[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = [left, right]

                have[s[left]] -= 1

                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed -= 1

                left += 1

        l, r = result
        return s[l:r+1] if min_len != float("inf") else ""