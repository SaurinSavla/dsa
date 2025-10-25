from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        n = len(s1)

        for l in range(0, len(s2)-len(s1)+1):
            r = l + len(s1)
            subs = s2[l:r]
            if Counter(subs)==count_s1:
                return True
        return False