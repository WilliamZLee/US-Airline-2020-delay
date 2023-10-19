import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import main

#sort by state
delay_by_state = main.airline_delay_data.groupby('state')
delay_counts_total = delay_by_state.arr_del15.sum()
print(delay_counts_total.sort_values(ascending=False))

## groupby state
grouped_airline_delay_data = main.delay_count.groupby(['state'])

## calculate mean
mean_delays = grouped_airline_delay_data.mean()

## calculate correlation
correlation = mean_delays.corr()

np.fill_diagonal(correlation.values, np.nan)

## output correlation matrix
print(correlation)

## visualization of correlation matrix
matplotlib.use("Qt5Agg")
plt.figure(figsize=(10, 8))
plt.imshow(correlation, cmap='rainbow', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(columns) - 2), columns[2:])
plt.yticks(range(len(columns) - 2), columns[2:])
plt.title('Correlation Matrix of Delay Types')
plt.show()
plt.savefig("figure_correlation_matrix.png")