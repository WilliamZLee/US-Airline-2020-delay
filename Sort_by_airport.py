import pandas as pd


def get_top_states(airline_delay_data):
    top_states = airline_delay_data.groupby('state')['late_aircraft_ct'].sum().nlargest(7).index
    return top_states


def filter_top_airports_by_state(airline_delay_data, top_states,write_output_to_file,separator):
    # delay ratio by airport
    delay_by_airport = airline_delay_data.groupby('airport_name')
    delay_ratio = delay_by_airport['arr_del15'].sum() / delay_by_airport['arr_flights'].sum()
    delay_ratio_filtered = delay_ratio[delay_by_airport['arr_flights'].sum() > 10000]
    sorted_delay_ratio = delay_ratio_filtered.sort_values(ascending=False)
    write_output_to_file("\n top 10 most delayed airports sort by delay ratio: \n")
    write_output_to_file(sorted_delay_ratio.head(10))
    write_output_to_file(separator)

    # filtered top affected airports delay factor
    filtered_data = airline_delay_data[airline_delay_data['airport_name'].isin(sorted_delay_ratio.head(10).index)]
    selected_columns = ['airport_name', 'carrier_ct', 'weather_ct', 'nas_ct', 'security_ct',
                        'late_aircraft_ct', 'arr_cancelled', 'arr_diverted']
    filtered_data_selected = filtered_data[selected_columns].groupby('airport_name').sum()
    filtered_data_selected['max'] = filtered_data_selected[selected_columns[1:]].idxmax(axis=1)
    filtered_data_selected['max_value'] = filtered_data_selected[selected_columns[1:]].max(axis=1)
    write_output_to_file("\n how these airports been affected by delay factors: \n")
    write_output_to_file(filtered_data_selected)
    write_output_to_file(separator)

    # filtered data by top states
    filtered_data = airline_delay_data.loc[airline_delay_data['state'].isin(top_states)]

    '''Group by state and airport, and calculate the sum of late_aircraft_ct'''
    grouped_data = filtered_data.groupby(['state', 'airport_name'])['late_aircraft_ct'].sum().reset_index()

    '''Sort the data by state and late_aircraft_ct in descending order'''
    sorted_data = grouped_data.sort_values(['state', 'late_aircraft_ct'], ascending=[True, False])

    '''Get the top 2 airports for each state and output '''
    top_airports = sorted_data.groupby('state').head(1)

    write_output_to_file("\nTop affected airports by state: ")
    write_output_to_file(top_airports)
    write_output_to_file(separator)
    return top_airports
