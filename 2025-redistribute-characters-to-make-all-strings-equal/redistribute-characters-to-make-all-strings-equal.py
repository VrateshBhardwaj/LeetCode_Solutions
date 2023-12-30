class Solution(object):
    def makeEqual(self, words):
        
        nstr = ''.join(words)
        alphabet_set = set(nstr)

        for ch in alphabet_set:
            if nstr.count(ch) % len(words) != 0:
                return False
        return True