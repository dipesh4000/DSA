class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig_color = image[sr][sc]
        def painter(row: int, col: int):
            if (not (0 <= row < len(image) and 0 <= col < len(image[0]))) or image[row][col] != orig_color:
                return
            image[row][col] = color
            [painter(row + x, col + y) for (x,y) in ((0,1), (1, 0), (0, -1), (-1, 0))]
        if orig_color != color:
            painter(sr, sc)
        return image