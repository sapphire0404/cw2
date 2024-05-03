import pandas as pd
import matplotlib.pyplot as plt
import squarify  # 用于生成树形图的库
import numpy as np  # 导入 numpy 库，并赋予别名 np

# 读取分组数据
data = pd.read_csv('gender_diet_distribution.csv')

# 创建一个新的列用于树形图的大小，这里使用人数 'n_participants'
sizes = data['n_participants'].values
# 创建标签，结合性别、饮食习惯和人数
labels = [f"{row['sex']} - {row['diet_group']}\n{row['n_participants']}" for index, row in data.iterrows()]

# 选择颜色
colors = plt.cm.Spectral(np.linspace(0, 1, len(labels)))

# 绘制树形图
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.7)
plt.title('People Distribution by Sex and Diet Group')
plt.axis('off')  # 关闭坐标轴

# 显示图形
plt.show()
