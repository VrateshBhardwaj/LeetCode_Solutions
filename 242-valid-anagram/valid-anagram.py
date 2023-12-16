class Solution(object):
    def isAnagram(self, s, t):
       return sorted(t) == sorted(s)