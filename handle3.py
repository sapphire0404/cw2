import pandas as pd

# 加载 CSV 文件
data = pd.read_csv('Results_21Mar2022.csv')

# 选择相关的列
selected_data = data[['age_group', 'n_participants', 'diet_group']]  # X: age_group, U: n_participants, W: diet_group

# 分组数据以计算每个年龄组和饮食习惯组合的人数总和
grouped_data = selected_data.groupby(['age_group', 'diet_group']).sum()

# 重置索引使其更易于阅读
grouped_data_reset = grouped_data.reset_index()

# 打印结果以查看
print(grouped_data_reset)

# 如果需要，可以将结果保存到新的 CSV 文件
grouped_data_reset.to_csv('age_diet_distribution.csv', index=False)
