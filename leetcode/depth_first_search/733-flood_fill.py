import sys


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        start_color = image[sr][sc]
        # while sr < len(image):
        self.helper(image, sr, sc, newColor, start_color)
            # sr += 1
        return image

    def helper(self, image, i, j, newColor, start_color):
        if i < 0 or j < 0 or i > len(image) - 1 or j > len(image[i]) - 1:
            return
        if image[i][j] != start_color or image[i][j] == newColor:
            return
        image[i][j] = newColor
        self.helper(image, i, j + 1, newColor, start_color)
        self.helper(image, i + 1, j, newColor, start_color)
        self.helper(image, i, j - 1, newColor, start_color)
        self.helper(image, i - 1, j, newColor, start_color)
        return


def main():

    """ Test cases """
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    print_image(Solution().floodFill(image, sr, sc, newColor))

    image = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    newColor = 2
    print_image(Solution().floodFill(image, sr, sc, newColor))

    image = [[8,4,5,3,2,2,2,6,9,5],[3,1,3,7,4,8,9,0,1,6],[0,7,1,7,5,2,2,8,6,9],[9,1,0,5,8,8,0,5,5,9],[3,4,9,5,4,8,0,2,7,5],[5,1,1,8,1,6,5,9,7,8],[9,7,9,4,5,3,4,1,8,2],[5,1,6,3,5,4,8,9,0,8],[8,8,6,1,0,8,0,6,9,9],[4,1,8,7,3,6,9,6,6,1]]
    sr = 8
    sc = 0
    newColor = 9
    print_image(Solution().floodFill(image, sr, sc, newColor))

    image = [[0, 0, 0], [0, 1, 1]]
    sr = 1
    sc = 1
    newColor = 1
    print_image(Solution().floodFill(image, sr, sc, newColor))

    image = [[5, 2, 1, 5, 6, 3, 2, 0, 6, 9], [0, 9, 5, 4, 2, 9, 5, 2, 0, 4], [0, 3, 3, 3, 1, 8, 1, 7, 3, 1],
     [0, 1, 1, 6, 8, 7, 4, 9, 1, 2], [1, 3, 4, 8, 2, 5, 1, 6, 2, 2], [5, 5, 8, 1, 2, 7, 2, 3, 9, 3],
     [2, 6, 2, 0, 1, 7, 0, 9, 4, 6], [9, 5, 0, 7, 6, 6, 7, 8, 4, 2], [3, 4, 9, 3, 4, 8, 2, 8, 9, 4],
     [4, 9, 1, 3, 9, 5, 4, 9, 1, 3]]
    sr = 3
    sc = 8
    newColor = 9
    print_image(Solution().floodFill(image, sr, sc, newColor))

def print_image(image):
    print('My Ouput:')
    for row in image:
        print(row)
    print()

if __name__ == '__main__':
    main()


# Instructions:
"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

"""