import matplotlib.pyplot as plt
import matplotlib


def plot_pie_chart(flights_count, airline_delay_data):
    ## as we are going to plot pie chart,
    ## here we don't use tolist() to generate list of columns' names
    ## define factors from main
    total_arr_flight = flights_count.arr_flights.sum()
    total_delay = flights_count.arr_del15.sum()
    total_carrier_delay = airline_delay_data.carrier_ct.sum()
    total_weather_delay = airline_delay_data.weather_ct.sum()
    total_NAS_delay = airline_delay_data.nas_ct.sum()
    total_security_delay = airline_delay_data.security_ct.sum()
    total_arriving_late_delay = airline_delay_data.late_aircraft_ct.sum()
    total_arr_cancelled = flights_count.arr_cancelled.sum()
    total_arr_diverted = flights_count.arr_diverted.sum()

    ## pie chart of delay / total arrive with hilighted part
    sizes = [total_delay, total_arr_flight - total_delay]
    labels = ['Delayed flights', 'Flights arrived on time']
    matplotlib.use("Qt5Agg")
    plt.pie(sizes, labels=labels, explode=(0.2, 0), autopct='%.2f%%')
    plt.title('Delay on-time rate')
    plt.savefig('plot/Delay on-time rate.png')
    plt.close()

    ## pie chart of table with hilighted three main porprotioin part
    sizes1 = [total_carrier_delay, total_weather_delay, total_NAS_delay,
              total_security_delay, total_arriving_late_delay, total_arr_cancelled,
              total_arr_diverted]
    labels1 = ['Air Carrier Delay', 'Weather Delay', 'NAS Delay',
               'Security Delay', 'Aircraft Arriving Late', 'Cancelled', 'Diverted']
    matplotlib.use("Qt5Agg")
    plt.pie(sizes1, labels=labels1, explode=(0.1, 0, 0.3, 0, 0.2, 0, 0), autopct='%.2f%%')
    plt.title('Delay factor proportion')
    plt.savefig('plot/Delay factor proportion pie chart.png')
    plt.close()
