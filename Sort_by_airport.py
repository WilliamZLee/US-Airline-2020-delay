import pandas as pd


def get_top_states(airline_delay_data):
    top_states = airline_delay_data.groupby('state')['late_aircraft_ct'].sum().nlargest(7).index
    return top_states


def filter_top_airports_by_state(airline_delay_data, top_states):
    ##  filtered data by top states
    filtered_data = airline_delay_data.loc[airline_delay_data['state'].isin(top_states)]

    '''Group by state and airport, and calculate the sum of late_aircraft_ct'''
    grouped_data = filtered_data.groupby(['state', 'airport_name'])['late_aircraft_ct'].sum().reset_index()

    '''Sort the data by state and late_aircraft_ct in descending order'''
    sorted_data = grouped_data.sort_values(['state', 'late_aircraft_ct'], ascending=[True, False])

    '''Get the top 2 airports for each state and output '''
    top_airports = sorted_data.groupby('state').head(1)

    print("Top affected airports by state: ")
    print(top_airports)

    return top_airports
