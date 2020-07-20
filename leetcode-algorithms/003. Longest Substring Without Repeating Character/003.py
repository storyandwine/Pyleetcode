class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def not_dup(strs):
            for ch in strs:
                if strs.count(ch)>1:
                    return False
            return True
        gap = 0
        left = 0
        while left<len(s)-gap:
            right  = left + gap+1
            if not_dup(s[left:right]):
                gap = gap+1
                continue
            else:
                left += 1
        return gap
S = Solution()
s = "au"
print(S.lengthOfLongestSubstring(s))