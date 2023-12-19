class Solution(object):
    def imageSmoother(self, img):

        rows = len(img)
        cols = len(img[0])

        updated_img = [[0]* cols for _ in range(rows)]

        dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

        for i in range(rows):
            for j in range(cols):
                sum = 0
                pixel_count = 0

                for k in range(9):
                    new_i, new_j = i + dx[k], j + dy[k]

                    if 0 <= new_i < rows and 0 <= new_j < cols:
                        sum += img[new_i][new_j]
                        pixel_count += 1

                updated_img[i][j] = sum / pixel_count

        return updated_img
        