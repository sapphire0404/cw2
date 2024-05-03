import pandas as pd

# 加载 CSV 文件
data = pd.read_csv('Results_21Mar2022.csv')

# 使用正确的列名筛选数据
selected_data = data[['sex', 'n_participants', 'diet_group']]  # sex: 性别, n_participants: 人数, diet_group: 饮食习惯

# 分组数据以计算每个性别和饮食习惯组合的人数总和
grouped_data = selected_data.groupby(['sex', 'diet_group']).sum()

# 重置索引使其更易于阅读
grouped_data_reset = grouped_data.reset_index()

# 打印结果以查看
print(grouped_data_reset)

# 如果需要，可以将结果保存到新的 CSV 文件
grouped_data_reset.to_csv('gender_diet_distribution.csv', index=False)
