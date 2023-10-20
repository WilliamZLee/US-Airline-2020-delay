import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


def delay_analysis_by_state(airline_delay_data, factors):
    ## total delay by state
    delay_serverity = airline_delay_data.groupby('state')
    delay_times_total = delay_serverity['arr_delay'].sum()
    print('the delay serverity sort by state: \n')
    print(delay_times_total.sort_values(ascending=False))
    print('-----------------------------------------------------------------------------------------------------------')

    '''Group and calculate the number of delays'''
    delay_by_state = airline_delay_data.groupby('state')
    delay_counts_total = delay_by_state['arr_del15'].sum()
    print('\nthe total delay sort by state: \n')
    print(delay_counts_total.sort_values(ascending=False))
    print('-----------------------------------------------------------------------------------------------------------')

    '''Sort by delay ratio'''
    delay_ratio = delay_by_state['arr_del15'].sum() / delay_by_state['arr_flights'].sum()
    sorted_delay_ratio = delay_ratio.sort_values(ascending=False)
    print('\n delay ratio sort by state: \n')
    print(sorted_delay_ratio)
    print('-----------------------------------------------------------------------------------------------------------')

    '''Calculate delay factors for each state separately'''
    delay_state_factor = delay_by_state[factors].sum()

    '''Calculate maximum factors and their indexes'''
    delay_state_factor['max'] = delay_state_factor.max(axis=1)
    delay_state_factor['max_idx'] = delay_state_factor.idxmax(axis=1)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    print("\n greatest delay factor in each state with their count: \n")
    print(delay_state_factor)
    print('-----------------------------------------------------------------------------------------------------------')

    '''Group and calculate the severity of delays caused by carrier sorted by state'''
    delay_counts_total_c = delay_by_state['carrier_ct'].sum()
    print("\n severity of delays caused by carrier by state: \n")
    print(delay_counts_total_c.sort_values(ascending=False))
    print('-----------------------------------------------------------------------------------------------------------')
    '''generate bar chart of these 7 factors'''
    for factor in factors:
        matplotlib.use("Qt5Agg")
        plt.figure(figsize=[15, 8])
        delay_factor_sort = delay_by_state[factor].sum().sort_values(ascending=False)
        delay_factor_sort.plot(kind='bar')
        plt.xticks(rotation=0)
        plt.title(f'{factor}_by_state')
        plt.savefig(f'plot/{factor}_by_state.png')
        plt.close()
