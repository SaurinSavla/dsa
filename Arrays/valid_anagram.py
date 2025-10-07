class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count1 = dict.fromkeys(s, 0)
        count2 = dict.fromkeys(t, 0)
        for char in s:
            count1[char] += 1
        for char in t:
            count2[char] += 1
        for key in count1:
            if count1[key] != count2.get(key, 0):
                return False
        return True