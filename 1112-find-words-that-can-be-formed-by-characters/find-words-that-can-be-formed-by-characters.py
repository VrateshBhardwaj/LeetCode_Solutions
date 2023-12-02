class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        length = 0
        for word in words:
            for char in word:
                if word.count(char) > chars.count(char):
                    break
            else:
                length += len(word)
        return length
