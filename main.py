import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
## import pacakge

airports_data = pd.read_csv('D:/Duke/UWA/2023S2/5101/Team assignment/airports.csv')
airline_delay_data = pd.read_csv('D:/Duke/UWA/2023S2/5101/Team assignment/airline_delay_causes_Feb2020.csv')

'''
airline_delay_data.info()
airports_data.info()'''

delay_count = airline_delay_data[['arr_del15', 'carrier_ct', 'weather_ct',
                                  'nas_ct','security_ct', 'late_aircraft_ct']]

delay_time = airline_delay_data[['arr_delay', 'carrier_delay', 'weather_delay',
                                 'nas_delay', 'security_delay', 'late_aircraft_delay']]

flights_count = airline_delay_data[['arr_flights', 'arr_del15', 'arr_cancelled', 'arr_diverted']]