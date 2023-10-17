import pandas as pd
import matplotlib.pyplot as plt

import main

filtered_airports_data = main.airports_data[(main.airports_data['lat'] >= 32) &
                                            (main.airports_data['lat'] <= 37) &
                                            (main.airports_data['long'] >= -100) &
                                            (main.airports_data['long'] <= -80)]

plt.figure(figsize = (10,6))
plt.scatter(filtered_airports_data.long, filtered_airports_data.lat,
            c = 'blue', marker= 'o', label = 'Airport')
plt.title('Airports within Latitude 32° to 37° and Longitude -100° to -80°')
plt.xlabel('long')
plt.ylabel('lat')
plt.grid(Ture)
plt.legend()
plt.show()