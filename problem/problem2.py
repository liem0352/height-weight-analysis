import numpy as np

# 创建矩阵A(2x3)和B(3x2)
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])

# 计算矩阵乘积
C = np.dot(A, B)

# 找出最大值和最小值
max_val = np.max(C)
min_val = np.min(C)

print("矩阵A：")
print(A)
print("\n矩阵B：")
print(B)
print("\n矩阵乘积C = A × B：")
print(C)
print(f"\n结果矩阵中的最大值：{max_val}")
print(f"\n结果矩阵中的最小值：{min_val}")
