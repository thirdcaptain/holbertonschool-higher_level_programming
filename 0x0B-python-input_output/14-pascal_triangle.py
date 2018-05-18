#!/usr/bin/python3
"""
module defines pascal triangle function
"""

def pascal_triangle(n):
    """
    prints pascal's triangle up to size n
    args:
        n (int): size of n
    """
    triangle = []
    value = 0
    if n <= 0:
        return triangle
    for row in range(n):
        temp = []
        for i in range (row + 1):
            if i == 0 or i == row:
                temp.append(1)
            else:
                value = (triangle[row - 1][i - 1] +
                         triangle[row - 1][i])
                temp.append(value)
        triangle.append(temp)
#        for i in range(row):
#            triangle[i].append(i)
    return triangle


if __name__ == "__main__":
    print(pascal_triangle(0))
