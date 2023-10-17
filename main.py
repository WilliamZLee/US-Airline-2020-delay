import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
## import pacakge

airports_data = pd.read_csv('D:/Duke/UWA/2023S2/5101/Team assignment/airports.csv')
airline_delay_data = pd.read_csv('D:/Duke/UWA/2023S2/5101/Team assignment/airline_delay_causes_Feb2020.csv')

airline_delay_data.info()
airports_data.info()