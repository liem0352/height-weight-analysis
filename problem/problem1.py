import numpy as np

# 创建一个10x10的全零数组
arr = np.zeros((10, 10))

# 设置边界元素为1
arr[0, :] = 1  # 第一行
arr[-1, :] = 1  # 最后一行
arr[:, 0] = 1  # 第一列
arr[:, -1] = 1  # 最后一列

print("10x10数组（边界为1，内部为0）：")
print(arr)