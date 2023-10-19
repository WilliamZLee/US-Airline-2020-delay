import main
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame

'''delay serverity by state'''
delay_serverity = main.airline_delay_data.groupby('state')
delay_times_total = delay_serverity.arr_delay.sum()
print(delay_times_total.sort_values(ascending=False))

'''delay count by state'''
delay_by_state = main.airline_delay_data.groupby('state')
delay_counts_total = delay_by_state.arr_del15.sum()
print(delay_counts_total.sort_values(ascending=False))

#sort by state

#each state factor import,sort
delay_carrier_ct = delay_by_state.carrier_ct.sum()
Dcarrier_ct = pd.DataFrame(delay_carrier_ct,columns=['carrier_ct'])
delay_weather_ct = delay_by_state.weather_ct.sum()
Dweather_ct = pd.DataFrame(delay_weather_ct,columns=['weather_ct'])
delay_nas_ct = delay_by_state.nas_ct.sum()
Dnas_ct = pd.DataFrame(delay_nas_ct,columns=['nas_ct'])
delay_security_ct = delay_by_state.security_ct.sum()
Dsecurity_ct = pd.DataFrame(delay_security_ct,columns=['security_ct'])
delay_late_aircraft_ct = delay_by_state.late_aircraft_ct.sum()
Dlate_aircraft_ct = pd.DataFrame(delay_late_aircraft_ct,columns=['late_aircraft_ct'])
delay_arr_cancelled_ct = delay_by_state.arr_cancelled.sum()
Darr_cancelled_ct = pd.DataFrame(delay_arr_cancelled_ct,columns=['arr_cancelled'])
delay_arr_diverted_ct = delay_by_state.arr_diverted.sum()
Darr_diverted_ct = pd.DataFrame(delay_arr_diverted_ct,columns=['arr_diverted'])

## combine data to new dataframe
delay_state_factor = pd.concat([Dcarrier_ct,Dweather_ct,delay_nas_ct,
                                Dsecurity_ct,Dlate_aircraft_ct,Darr_cancelled_ct,
                                Darr_diverted_ct],axis = 1, sort = False)
#print(delay_state_factor)

## change factors all to float64
delay_state_factor['arr_cancelled'] = delay_state_factor['arr_cancelled'].astype(float)
delay_state_factor['arr_diverted'] = delay_state_factor['arr_diverted'].astype(float)
# delay_state_factor.info()

## add max factor of each row to dataframe in two column: max factor, index name
delay_state_factor_max = pd.DataFrame()
delay_state_factor_max['max'] = delay_state_factor.max(axis=1)
delay_state_factor_max['max_idx'] = delay_state_factor.idxmax(axis=1)
delay_state_factor1 = pd.concat([delay_state_factor,delay_state_factor_max],axis=1,
                               join='outer',ignore_index=False)
print(delay_state_factor1)

'''Sort by Carrier Name'''
delay_by_carrier = main.airline_delay_data.groupby('carrier_name')
delay_counts_total_c = delay_by_carrier.arr_del15.sum()
print(delay_counts_total_c.sort_values(ascending=False))
