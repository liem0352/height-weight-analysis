import numpy as np

# 创建行索引数组和列索引数组
rows = np.arange(5).reshape(5, 1)
cols = np.arange(5)

# 使用广播机制创建矩阵
matrix = rows + cols

print("5x5矩阵（每个元素 = 行索引 + 列索引）：")
print(matrix)