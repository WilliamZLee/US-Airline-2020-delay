import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd


def Carrier_strategies(airline_delay_data,write_output_to_file,separator, factors):
    # Group and calculate the number of delays caused by carrier sorted by airline name
    delay_by_carrier = airline_delay_data.groupby('carrier_name')
    delay_counts_total_c = delay_by_carrier['carrier_ct'].sum()
    write_output_to_file("\n number of delays caused by carrier sort by carrier: \n")
    write_output_to_file(delay_counts_total_c.sort_values(ascending=False))
    write_output_to_file(separator)

    # plot carriers by delay factors in one combined plot
    fig,axes = plt.subplots(2,4,figsize = (100,20))
    images = []
    for i,factor in enumerate(factors):
        matplotlib.use("Qt5Agg")
        ax = axes[i // 4, i % 4]
        axes[i // 4, i % 4].set_title(f'carrier_delays_by_{factor}')
        ax.set_title(f'carrier_delays_by_{factor}')
        delay_factor_sort = delay_by_carrier[factor].sum().sort_values(ascending=False)
        delay_factor_sort.plot(kind='bar', ax=ax)
        xticks = np.arange(len(delay_factor_sort.index))

        # labels set to avoid overlaping
        every_nth = 4
        ax.set_xticks(xticks[::every_nth])
        ax.set_xticklabels(delay_factor_sort.index[::every_nth], rotation=-15)
        ax.autoscale(enable = True, axis = 'both', tight = True)
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        # set a pause for canvas to draw combied plot
        plt.pause(0.1)
        fig.canvas.draw()
        image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
        image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        images.append(image)

    rows = images[0].shape[0]
    cols = images[0].shape[1]
    combined_rows = rows * 2
    combined_cols = cols * 4

    combined_image = np.zeros((combined_rows, combined_cols, 3), dtype=np.uint8)

    for i, image in enumerate(images):
        row = i // 4
        col = i % 4
        combined_image[row * rows:(row + 1) * rows, col * cols:(col + 1) * cols, :] = image

    plt.imshow(combined_image)
    plt.axis('off')
    plt.tight_layout()

    output_filename = 'combined_carrier_delays.png'
    output_path = f'plot/{output_filename}'
    plt.savefig(output_path)
    plt.close(fig)

    # Sort best delay control carriers
    Carrier_control_level = delay_by_carrier['arr_del15'].sum() / delay_by_carrier['arr_flights'].sum()
    Sorted_control_level = Carrier_control_level.sort_values(ascending=False)
    write_output_to_file("\n delay control level sort by carrier: \n")
    write_output_to_file(Sorted_control_level)
    write_output_to_file(separator)

    # figure of Sorted control level
    matplotlib.use("Qt5Agg")
    plt.figure(figsize=[30, 20])
    ''' set ylab as percentage'''
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(1.0))

    bars = Sorted_control_level.plot(kind='bar')

    # add value to each bar
    for bar in bars.patches:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval: .2%}', ha='center', va='bottom')

    plt.xticks(rotation=-15)
    plt.title('Total_delay_control_level_of_all_17_airlines')
    plt.savefig('plot/Total_delay_control_level_of_all_17_airlines')
    plt.close()

    # detail of best6 delay control carriers
    filtered_carriers = airline_delay_data[airline_delay_data['carrier_name'].isin(Sorted_control_level.tail(6).index)]
    selected_columns = ['carrier_name', 'arr_flights','arr_del15','carrier_ct', 'weather_ct', 'nas_ct', 'security_ct',
                        'late_aircraft_ct', 'arr_cancelled', 'arr_diverted']
    filtered_carriers_selected = filtered_carriers[selected_columns].groupby('carrier_name').sum()

    filtered_carriers_selected['min_index'] = filtered_carriers_selected[selected_columns[1:]].idxmin(axis=1)
    filtered_carriers_selected['min_value'] = filtered_carriers_selected[selected_columns[1:]].min(axis=1)

    write_output_to_file("\n how these carriers control delay: \n")
    write_output_to_file(filtered_carriers_selected)
    write_output_to_file(separator)

    # figure of best delay control carriers
    matplotlib.use("Qt5Agg")
    plt.figure(figsize=[15, 8])
    ''' set ylab as percentage'''
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(1.0))

    bars = Sorted_control_level.tail(6).plot(kind='bar')

    # add value to each bar
    for bar in bars.patches:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval: .2%}', ha='center', va='bottom')

    plt.xticks(rotation=0)
    plt.title('Best_Delay_Control_Carriers')
    plt.savefig('plot/Best_6_delay_control_carriers')
    plt.close()


def Airport_strategies(airline_delay_data,write_output_to_file,separator):
    airport_delay = airline_delay_data.groupby('airport_name')
    airport_delay_ratio = airport_delay['arr_del15'].sum() / airport_delay['arr_flights'].sum()
    airport_delay_ratio_filtered = airport_delay_ratio[airport_delay['arr_flights'].sum() > 8000]
    sorted_airport_delay_ratio_filtered = airport_delay_ratio_filtered.sort_values(ascending=False)
    best6_airports = sorted_airport_delay_ratio_filtered.tail(6)
    write_output_to_file("\n best 6 delay control airports sort by delay ratio: \n")
    write_output_to_file(best6_airports)
    write_output_to_file(separator)

    # detail of best6 delay control carriers
    filtered_airports = airline_delay_data[airline_delay_data['airport_name'].isin(best6_airports.index)]
    selected_columns = ['airport_name', 'arr_flights','arr_del15','carrier_ct', 'weather_ct', 'nas_ct', 'security_ct',
                        'late_aircraft_ct', 'arr_cancelled', 'arr_diverted']
    filtered_airports_selected = filtered_airports[selected_columns].groupby('airport_name').sum()

    filtered_airports_selected['min'] = filtered_airports_selected[selected_columns[1:]].idxmin(axis=1)
    filtered_airports_selected['min_value'] = filtered_airports_selected[selected_columns[1:]].min(axis=1)

    write_output_to_file("\n how these airports control delay: \n")
    write_output_to_file(filtered_airports_selected)
    write_output_to_file(separator)

    # figure of best delay control carriers
    matplotlib.use("Qt5Agg")
    plt.figure(figsize=[15, 10])
    # set ylab as percentage
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mticker.PercentFormatter(1.0))

    bars = best6_airports.plot(kind='bar')

    # add value to each bar
    for bar in bars.patches:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval: .2%}', ha='center', va='bottom')

    plt.xticks(rotation=-15)
    plt.title('Best_Delay_Control_airports')
    plt.savefig('plot/Best_6_delay_control_airports')
    plt.close()
