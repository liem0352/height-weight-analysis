import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 实验数据
height = np.array([165, 172, 168, 175, 170, 169, 173, 171, 167, 174, 166, 176, 164, 177, 172, 169, 175, 170, 168, 173, 171, 165, 174, 167, 178, 170, 166, 172, 169, 171])
weight = np.array([52, 65, 58, 70, 62, 59, 68, 63, 56, 67, 54, 72, 51, 75, 64, 60, 71, 61, 57, 66, 62, 53, 68, 55, 76, 61, 54, 65, 59, 63])

# 创建数据框
data = pd.DataFrame({'身高(cm)': height, '体重(kg)': weight})

print("="*50)
print("实验实训：身高与体重的相关性分析")
print("="*50)

# 1. 正态性检验 - Shapiro-Wilk检验
print("\n1. 正态性检验 (Shapiro-Wilk Test)")
print("-"*30)

# 身高的正态性检验
shapiro_height = stats.shapiro(height)
print(f"身高数据：")
print(f"  统计量(W) = {shapiro_height.statistic:.4f}")
print(f"  p值 = {shapiro_height.pvalue:.4f}")
if shapiro_height.pvalue > 0.05:
    print("  结论：身高数据服从正态分布 (p > 0.05)")
else:
    print("  结论：身高数据不服从正态分布 (p ≤ 0.05)")

# 体重的正态性检验
shapiro_weight = stats.shapiro(weight)
print(f"\n体重数据：")
print(f"  统计量(W) = {shapiro_weight.statistic:.4f}")
print(f"  p值 = {shapiro_weight.pvalue:.4f}")
if shapiro_weight.pvalue > 0.05:
    print("  结论：体重数据服从正态分布 (p > 0.05)")
else:
    print("  结论：体重数据不服从正态分布 (p ≤ 0.05)")

# 2. 相关性分析
print("\n2. 相关性分析")
print("-"*30)

# 判断是否满足正态性条件
height_normal = shapiro_height.pvalue > 0.05
weight_normal = shapiro_weight.pvalue > 0.05

if height_normal and weight_normal:
    print("由于两组数据均服从正态分布，采用Pearson相关分析")
    corr_result = stats.pearsonr(height, weight)
    corr_method = "Pearson"
else:
    print("由于至少一组数据不服从正态分布，采用Spearman秩相关分析")
    corr_result = stats.spearmanr(height, weight)
    corr_method = "Spearman"

print(f"\n{corr_method}相关分析结果：")
print(f"  相关系数 = {corr_result[0]:.4f}")
print(f"  p值 = {corr_result[1]:.4f}")

# 相关性强度判断
r = corr_result[0]
r_abs = abs(r)
if r_abs < 0.3:
    strength = "极弱相关"
elif r_abs < 0.5:
    strength = "弱相关"
elif r_abs < 0.7:
    strength = "中等相关"
elif r_abs < 0.9:
    strength = "强相关"
else:
    strength = "极强相关"

# 相关性显著性判断
if corr_result[1] < 0.01:
    significance = "极显著相关 (p < 0.01)"
elif corr_result[1] < 0.05:
    significance = "显著相关 (p < 0.05)"
else:
    significance = "无显著相关 (p ≥ 0.05)"

print(f"  相关性强度：{strength}")
print(f"  显著性：{significance}")

# 3. 数据可视化 - 散点图
print("\n3. 数据可视化")
print("-"*30)
print("绘制身高与体重的散点图...")

plt.figure(figsize=(10, 6))
sns.scatterplot(x='身高(cm)', y='体重(kg)', data=data, s=100, color='#1f77b4', alpha=0.8)
sns.regplot(x='身高(cm)', y='体重(kg)', data=data, scatter=False, color='#ff7f0e', line_kws={'alpha': 0.7})

plt.title(f'身高与体重的散点图及回归线\n({corr_method}相关系数: {corr_result[0]:.4f}, p值: {corr_result[1]:.4f})', fontsize=14, pad=20)
plt.xlabel('身高(cm)', fontsize=12)
plt.ylabel('体重(kg)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# 保存图表
plt.savefig('height_weight_scatter.png', dpi=300, bbox_inches='tight')
print("散点图已保存为 'height_weight_scatter.png'")

# 4. 统计结论
print("\n4. 统计结论")
print("-"*30)
print("正态性检验总结：")
print(f"  身高数据：{'服从' if height_normal else '不服从'}正态分布 (p = {shapiro_height.pvalue:.4f})")
print(f"  体重数据：{'服从' if weight_normal else '不服从'}正态分布 (p = {shapiro_weight.pvalue:.4f})")

print(f"\n相关性分析总结：")
print(f"  使用方法：{corr_method}相关分析")
print(f"  相关系数：{corr_result[0]:.4f}，表明{strength}{'正相关' if r > 0 else '负相关'}")
print(f"  显著性：{significance}")

print("\n最终结论：")
if corr_result[1] < 0.05:
    print(f"  统计结果表明，身高与体重之间存在{strength}的{significance}。")
    print(f"  身高越高，体重{'倾向于' if r > 0 else '不倾向于'}{'增加' if r > 0 else '减少'}。")
else:
    print(f"  统计结果表明，身高与体重之间无显著相关关系 (p ≥ 0.05)。")

print("\n" + "="*50)
print("实验完成！")
print("="*50)
