class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        if len(colors) == 1:
            return 0
        count, s, top = 0, 0, 0
        for i in range(1, len(colors)):
            s += neededTime[i-1]
            top = max(top, neededTime[i-1])
            if colors[i-1] != colors[i]:
                count += s - top
                s, top = 0, 0
        if colors[-2] == colors[-1]:
            s += neededTime[-1]
            top = max(top, neededTime[-1])
            count += s - top
        return count
        