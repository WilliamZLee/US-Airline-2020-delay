import matplotlib
import matplotlib.pyplot as plt


def delay_analysis_by_state(airline_delay_data, factors):
    '''Group and calculate total delays'''
    delay_serverity = airline_delay_data.groupby('state')
    delay_times_total = delay_serverity['arr_delay'].sum()
    print(delay_times_total.sort_values(ascending=False))

    '''Group and calculate the number of delays'''
    delay_by_state = airline_delay_data.groupby('state')
    delay_counts_total = delay_by_state['arr_del15'].sum()
    print(delay_counts_total.sort_values(ascending=False))

    '''Calculate delay factors for each state separately'''
    delay_state_factor = delay_by_state[factors].sum()

    '''Calculate maximum factors and their indexes'''
    delay_state_factor['max'] = delay_state_factor.max(axis=1)
    delay_state_factor['max_idx'] = delay_state_factor.idxmax(axis=1)
    print(delay_state_factor)

    '''Group and calculate the number of delays sorted by airline name'''
    delay_by_carrier = airline_delay_data.groupby('carrier_name')
    delay_counts_total_c = delay_by_carrier['arr_del15'].sum()
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
