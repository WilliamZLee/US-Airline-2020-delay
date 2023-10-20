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

def Airport_strategies(airline_delay_data):
    airport_delay = airline_delay_data.groupby('airport_name')
    airport_delay_ratio = airport_delay['arr_del15'].sum() / airport_delay['arr_flights'].sum()
    airport_delay_ratio_filtered = airport_delay_ratio[airport_delay['arr_flights'].sum() > 8000]
    sorted_airport_delay_ratio_filtered = airport_delay_ratio_filtered.sort_values(ascending=False)
    best6_airports = sorted_airport_delay_ratio_filtered.tail(6)
    print("\n best 6 delay control airports sort by delay ratio: \n")
    print(best6_airports)
    print('-----------------------------------------------------------------------------------------------------------')

    ## figure of best delay control carriers
    matplotlib.use("Qt5Agg")
    plt.figure(figsize=[15,10])
    ''' set ylab as percentage'''
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(1.0))

    bars = best6_airports.plot(kind = 'bar')

    '''add value to each bar'''
    for bar in bars.patches:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval: .2%}', ha = 'center', va = 'bottom')

    plt.xticks(rotation = -15)
    plt.title('Best_Delay_Control_airports')
    plt.savefig('plot/Best_6_delay_control_airports')
    plt.close()


