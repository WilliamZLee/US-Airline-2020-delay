import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
## import pacakge

airports_data = pd.read_csv('data/airports.csv')
airline_delay_data = pd.read_csv('data/airline_delay_causes_Feb2020.csv')

## airline_delay_data.info()
## airports_data.info()

delay_count = airline_delay_data[['state', 'carrier_ct', 'weather_ct',
                                  'nas_ct','security_ct', 'late_aircraft_ct',
                                  'arr_cancelled', 'arr_diverted']]

delay_time = airline_delay_data[['state', 'carrier_delay', 'weather_delay',
                                 'nas_delay', 'security_delay', 'late_aircraft_delay']]

flights_count = airline_delay_data[['arr_flights', 'arr_del15', 'arr_cancelled', 'arr_diverted']]

'''set index by state'''
delay_count_row = delay_count.set_index('state',drop = True)
delay_time_row = delay_time.set_index('state',drop = True)

'''change dataframe to dictionary for sort
delay_ct_dict = delay_count.set_index('state').to_dict()
print(delay_ct_dict)
'''
## delay_count_row.info()