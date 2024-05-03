import pandas as pd
import matplotlib.pyplot as plt
import squarify  # 用于生成树形图的库

# 读取数据
data = pd.read_csv('diet_group_averages.csv')

# 指标列表
metrics = ['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_ghgs_ch4', 
           'mean_ghgs_n2o', 'mean_bio', 'mean_watuse', 'mean_acid']

# 设置图形大小
plt.figure(figsize=(20, 12))

# 为每个指标创建一个树形图
for i, metric in enumerate(metrics, 1):
    plt.subplot(3, 3, i)  # 3行3列的子图
    sizes = data[metric].values  # 每个块的大小
    labels = [f'{diet}\n{size:.2f}' for diet, size in zip(data['diet_group'], sizes)]
    colors = plt.cm.tab20c(range(len(labels)))  # 创建一个颜色数组
    squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.8)
    plt.title(metric)
    plt.axis('off')  # 关闭坐标轴

# 调整子图间距
plt.tight_layout()
# 显示图形
plt.show()
