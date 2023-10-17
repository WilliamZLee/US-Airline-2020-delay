import main
import pandas as pd
import numpy as np

'''sort by state'''
delay_by_state = main.airline_delay_data.groupby('state')
delay_counts = delay_by_state.arr_del15.sum()
print(delay_counts.sort_values(ascending=False))

'''each state factor sort '''



