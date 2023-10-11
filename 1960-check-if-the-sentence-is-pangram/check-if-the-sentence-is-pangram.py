class Solution(object):
    def checkIfPangram(self, sentence):
        unique_string = len(set(sentence))
        if unique_string == 26:
            return True
        else:
            return False
        