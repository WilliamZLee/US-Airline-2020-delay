import pandas as pd
import importlib
import Relation_between_Geographical_factors_delay as rbgfd
import Filtered_airports_heatmap_plot as fahp
import Pie_chart_plot as pcp
import Sort_by_airport
import Sort_by_Carrier as sbc
import shutil

airports_data = pd.read_csv('data/airports.csv')
airline_delay_data = pd.read_csv('data/airline_delay_causes_Feb2020.csv')

# create file output.txt to save output
output_file = open("output.txt", "w")

# def a funtion to write in
def write_output_to_file(output):
    print(output)
    print(output, file=output_file)

# airline_delay_data.info()
# airports_data.info()

delay_count = airline_delay_data[['state', 'carrier_ct', 'weather_ct',
                                  'nas_ct', 'security_ct', 'late_aircraft_ct',
                                  'arr_cancelled', 'arr_diverted']]

delay_time = airline_delay_data[['state', 'carrier_delay', 'weather_delay',
                                 'nas_delay', 'security_delay', 'late_aircraft_delay']]

flights_count = airline_delay_data[['arr_flights', 'arr_del15', 'arr_cancelled', 'arr_diverted']]

# set index by state
delay_count_row = delay_count.set_index('state', drop=True)
delay_time_row = delay_time.set_index('state', drop=True)
# delay_count_row.info()

def run_analysis(airline_delay_data, delay_count, airports_data, flights_count):
    # get console width
    console_width = shutil.get_terminal_size().columns
    # generate equal length separator
    separator = '-' * console_width

    write_output_to_file("Delay analysis by state: ")
    Sort_by_state = importlib.import_module('Sort_by_state')
    factors = delay_count.columns.values.tolist()
    factors.remove('state')
    Sort_by_state.delay_analysis_by_state(airline_delay_data, factors, write_output_to_file,separator)

    write_output_to_file(separator)
    write_output_to_file("\nCarrier delay control analysis: ")
    sbc.Carrier_strategies(airline_delay_data, write_output_to_file,separator,factors)
    sbc.Airport_strategies(airline_delay_data, write_output_to_file,separator)

    write_output_to_file(separator)
    write_output_to_file("\nSort by Airports: ")
    top_states = Sort_by_airport.get_top_states(airline_delay_data)
    top_states = list(top_states)[:7]
    Sort_by_airport.filter_top_airports_by_state(airline_delay_data, top_states, write_output_to_file,separator)

    write_output_to_file(separator)
    write_output_to_file("\nRelation between Geographical factors delay: ")
    rbgfd.calculate_delay_correlation(delay_count, write_output_to_file,separator)

    write_output_to_file(separator)
    write_output_to_file("\nFiltered airports heatmap: ")
    fahp.plot_fiiltered_airports_heatmap(airports_data, write_output_to_file,separator)

    write_output_to_file(separator)
    write_output_to_file("\nPie charts will be stored in 'plot' folder")
    pcp.plot_pie_chart(flights_count, airline_delay_data)

    write_output_to_file(separator)
    write_output_to_file("\nAll the generated images throughout the process are stored in the 'plot' folder")

run_analysis(airline_delay_data, delay_count, airports_data, flights_count)

output_file.close()
