class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for ch in s:
            pos = t.find(ch)
            if pos == -1:
                return False
            else:
                t = t[pos+1:]
        return True