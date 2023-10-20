import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import folium
from folium.plugins import HeatMap

def plot_fiiltered_airports_heatmap(airports_data):
    ## filter of lat & long
    filtered_airports_data = airports_data.set_index('airport', drop=True)
    filtered_airports_data1 = pd.DataFrame(filtered_airports_data,
                                           columns=['lat', 'long'])[(filtered_airports_data['lat'] >= 32) &
                                                                    (filtered_airports_data['lat'] <= 37) &
                                                                    (filtered_airports_data['long'] >= -100) &
                                                                    (filtered_airports_data['long'] <= -80)]
    print(filtered_airports_data1)
    filtered_airports_data1.info()

    '''scatter_plot'''
    x = filtered_airports_data1.lat
    y = filtered_airports_data1.long

    print(len(x))
    print(len(y))
    matplotlib.use("Qt5Agg")
    plt.scatter(x, y, c='blue')
    plt.savefig('plot/filtered airports in scatter plot.png')
    plt.close()

    '''heatmap1'''
    plt.figure(figsize=(10, 6))
    plt.hexbin(y, x, gridsize=30, cmap='YlOrRd')
    plt.title('Airports within Latitude 32° to 37° and Longitude -100° to -80°')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.colorbar(label='Frequency')
    plt.grid(False)
    plt.show()
    plt.savefig('plot/filtered airports in hexagonal bin plot.png')
    plt.close()

    '''geographical heat map'''
    # Create a base map
    m = folium.Map(location=[34.5, -90], zoom_start=5)

    # Add the heatmap
    heat_data = [[row['lat'], row['long']] for index, row in filtered_airports_data1.iterrows()]
    HeatMap(heat_data).add_to(m)

    m.save('plot/heatmap.html')
