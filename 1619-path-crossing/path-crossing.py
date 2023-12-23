class Solution(object):
    def isPathCrossing(self, path):

        crossed = False
        visited_points = [[0, 0]]

        for i, direction in enumerate(path):

            if direction == 'N':
                visited_points.extend([[visited_points[i][0], visited_points[i][1]+1]])

            elif direction == 'S':
                visited_points.extend([[visited_points[i][0], visited_points[i][1]-1]])

            elif direction == 'E':
                visited_points.extend([[visited_points[i][0]+1, visited_points[i][1]]])

            elif direction == 'W':
                visited_points.extend([[visited_points[i][0]-1, visited_points[i][1]]])

        for coordinate in visited_points:
            if visited_points.count(coordinate) > 1:
                crossed = True
                break

        return crossed