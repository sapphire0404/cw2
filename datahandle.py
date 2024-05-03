import pandas as pd

# 加载 CSV 文件，假设列名在第一行
data = pd.read_csv('Results_21Mar2022.csv')
selected_data = data.loc[:, 'mean_ghgs':'mean_acid']
selected_data['diet_group'] = data['diet_group']

# 根据饮食习惯分组，并计算每组的平均值
grouped_averages = selected_data.groupby('diet_group').mean()

# 打印每种饮食习惯下的各项指标平均值
print("各种饮食习惯下的环境影响指标平均值：")
print(grouped_averages)

# 如果需要，可以将结果保存到新的 CSV 文件
grouped_averages.to_csv('diet_group_averages.csv')