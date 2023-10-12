"""python3.x中a = [[1, 2], [3, 4], [5, 6]]，请用一行代码将a转换成[1, 2, 3, 4, 5, 6]"""

a = [[1, 2], [3, 4], [5, 6]]
print([num for sublist in a for num in sublist])
