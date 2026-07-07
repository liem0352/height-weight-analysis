import numpy as np

# 设置随机种子以确保结果可复现
np.random.seed(42)

# 创建包含20个0-100随机整数的数组
arr = np.random.randint(0, 101, 20)

# 找出所有大于50的元素
greater_than_50 = arr[arr > 50]

# 计算平均值
average = np.mean(greater_than_50)

print("生成的20个随机整数：")
print(arr)
print("\n大于50的元素：")
print(greater_than_50)
print(f"\n大于50的元素的平均值：{average:.2f}")