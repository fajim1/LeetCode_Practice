class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(list(s))== sorted((t)):
            return True
        else:
            return False
        