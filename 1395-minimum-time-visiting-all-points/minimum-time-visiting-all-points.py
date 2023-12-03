class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        total_time = 0
        for i in range(1, len(points)):
            total_time += max(abs(points[i-1][0] - points[i][0]),
                              abs(points[i][1] - points[i-1][1])
            )
            
        return total_time
        