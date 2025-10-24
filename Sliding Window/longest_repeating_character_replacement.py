class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset = set(s)
        res = 0

        for c in charset:
            l = 0
            count = 0
            for r in range (len(s)):
                if s[r] == c:
                    count += 1
                
                while (r-l+1) - k > count:
                    if s[l] == c:
                        count -= 1
                    l += 1
                res = max(r-l+1, res)
        return res