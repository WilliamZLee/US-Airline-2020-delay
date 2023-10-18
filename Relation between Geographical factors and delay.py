import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import main

#sort by state

delay_by_state = main.airline_delay_data.groupby('state')
delay_counts_total = delay_by_state.arr_del15.sum()
print(delay_counts_total.sort_values(ascending=False))


# 选择所需的列
columns = ['state', 'carrier_ct', 'weather_ct', 'nas_ct', 'security_ct', 'late_aircraft_ct', 'arr_cancelled', 'arr_diverted']

# 创建新的DataFrame来存储所需列的数据
selected_airline_delay_data = main.airline_delay_data[columns]

# 根据地理因素对数据进行分组
grouped_airline_delay_data = selected_airline_delay_data.groupby(['state'])

# 计算每个地点的平均延误数据
mean_delays = grouped_airline_delay_data.mean()

# 进行相关性分析
correlation = mean_delays.corr()

# 将对角线元素设置为白色
np.fill_diagonal(correlation.values, np.nan)

# 打印相关性矩阵的数值
print(correlation)

# 可视化相关性矩阵
matplotlib.use("Qt5Agg")
plt.figure(figsize=(10, 8))
plt.imshow(correlation, cmap='rainbow', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(columns) - 2), columns[2:])
plt.yticks(range(len(columns) - 2), columns[2:])
plt.title('Correlation Matrix of Delay Types')
plt.show()
plt.savefig("figure_correlation_matrix.png")