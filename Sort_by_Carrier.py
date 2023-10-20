import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd

def Carrier_strategies(airline_delay_data):
    ## Group and calculate the number of delays caused by carrier sorted by airline name
    delay_by_carrier = airline_delay_data.groupby('carrier_name')
    delay_counts_total_c = delay_by_carrier['carrier_ct'].sum()
    print("\n number of delays caused by carrier sort by carrier: \n")
    print(delay_counts_total_c.sort_values(ascending=False))
    print('-----------------------------------------------------------------------------------------------------------')

    ## Sort best delay control carriers
    Carrier_control_level = delay_by_carrier['arr_del15'].sum() / delay_by_carrier['arr_flights'].sum()
    Sorted_control_level = Carrier_control_level.sort_values(ascending=False)
    print("\n delay control level sort by carrier: \n")
    print(Sorted_control_level)
    print('-----------------------------------------------------------------------------------------------------------')

    ## figure of best delay control carriers
    matplotlib.use("Qt5Agg")
    plt.figure(figsize=[15,8])
    ''' set ylab as percentage'''
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(1.0))

    bars = Sorted_control_level.tail(6).plot(kind = 'bar')

    '''add value to each bar'''
    for bar in bars.patches:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval: .2%}', ha = 'center', va = 'bottom')

    plt.xticks(rotation = 0)
    plt.title('Best_Delay_Control_Carriers')
    plt.savefig('plot/Best_6_delay_control_carriers')
    plt.close()