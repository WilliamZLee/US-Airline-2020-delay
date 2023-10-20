import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


def delay_analysis_by_state(airline_delay_data, factors):
    ## total delay by state
    delay_serverity = airline_delay_data.groupby('state')
    delay_times_total = delay_serverity['arr_delay'].sum()
    print(delay_times_total.sort_values(ascending=False))

    '''Group and calculate the number of delays'''
    delay_by_state = airline_delay_data.groupby('state')
    delay_counts_total = delay_by_state['arr_del15'].sum()
    print(delay_counts_total.sort_values(ascending=False))


    '''Sort by delay ratio'''
    delay_ratio = delay_by_state['arr_del15'].sum() / delay_by_state['arr_flights'].sum()
    sorted_delay_ratio = delay_ratio.sort_values(ascending=False)
    print(sorted_delay_ratio)

    '''Calculate delay factors for each state separately'''
    delay_state_factor = delay_by_state[factors].sum()

    '''Calculate maximum factors and their indexes'''
    delay_state_factor['max'] = delay_state_factor.max(axis=1)
    delay_state_factor['max_idx'] = delay_state_factor.idxmax(axis=1)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    print(delay_state_factor)

    '''Group and calculate the number of delays caused by carrier sorted by airline name'''
    delay_by_carrier = airline_delay_data.groupby('carrier_name')
    delay_counts_total_c = delay_by_carrier['carrier_ct'].sum()
    print(delay_counts_total_c.sort_values(ascending=False))

    '''Group and calculate the severity of delays caused by carrier sorted by airline name'''
    delay_by_carrier = airline_delay_data.groupby('carrier_name')
    delay_counts_total_c = delay_by_carrier['carrier_delay'].sum()
    print(delay_counts_total_c.sort_values(ascending=False))

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
