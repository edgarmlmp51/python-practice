from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orginal_color = image[sr][sc]

        if orginal_color == color:
            return image
        
        def fill(row, col):
            if row < 0 or row >= len(image):
                return
            if col < 0 or col >= len(image[0]):
                return
            if image[row][col] != orginal_color:
                return
            
            image[row][col] = color

            fill(row + 1, col)
            fill(row, col + 1)
            fill(row - 1, col)
            fill(row, col - 1)

        fill(sr, sc)
        return image