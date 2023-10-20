import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pandas as pd

def calculate_delay_correlation(delay_count, airline_delay_data):
    columns = delay_count.columns.values.tolist()

    '''sort by state'''
    delay_by_state = airline_delay_data.groupby('state')
    delay_counts_total = delay_by_state.arr_del15.sum()
    print(delay_counts_total.sort_values(ascending=False))

    '''use delay_count dataframe for correlation calculation'''
    grouped_airline_delay_data = delay_count.groupby(['state'])

    '''calculate mean for calculate correlation and set diagonal as white in convinent of visualization'''
    mean_delays = grouped_airline_delay_data.mean()
    correlation = mean_delays.corr()
    np.fill_diagonal(correlation.values, np.nan)
    pd.set_option('display.max_columns',None)
    print(correlation)

    '''visualization of correlation matrix'''
    matplotlib.use("Qt5Agg")
    plt.figure(figsize=(10, 8))
    plt.imshow(correlation, cmap='rainbow', vmin=-1, vmax=1)
    plt.colorbar()
    plt.xticks(range(len(columns) - 2), columns[2:])
    plt.yticks(range(len(columns) - 2), columns[2:])
    plt.title('Correlation Matrix of Delay Types')
    plt.savefig("plot/figure_correlation_matrix.png")
    plt.show()
    plt.close()


