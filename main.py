'''
1. 各州导致最严重延误的主要因素是什么？将各州的延误严重程度从高到低排序，
     并深入分析延误类型、延误频率以及受这些延误影响最大的航空公司。
2.  找出一贯采取有效延误管理策略的航空公司或机场。从他们的实践中可以汲取哪些经验教训？
3. 分析航班延误的地理分布。调查某些类型的延误是否与特定的地理因素（如机场规模、位置）相关。
    是否存在表明需要改善基础设施等的模式？
4. 确定纬度范围在 32° 至 37° 之间和经度范围在 -100° 至 -80° 之间的机场，
    并使用热图将其可视化。并使用热图将其可视化。
5. 使用饼图显示航班准点率以及上表中列出的项目。
6. 假设您是一名航空分析师，负责提高美国航空旅行的整体效率和可靠性。使用所提供的航班延误数据集，
    设计一种新颖的策略或方法来减少航班延误并改善乘客体验。
    解释您提出的战略、支持该战略的数据驱动见解以及实施该战略的潜在挑战和益处。要有创意，
    并考虑对美国航空业的短期和长期影响。
'''

'''
year：数据年份（所有条目均为 2020 年）。
month：数据的月份（所有条目均为二月份）。
carrier：航空公司代码。
carrier_name：航空公司的名称。
airport: 机场代码。
airport_name: 机场名称。
arr_flights：到达航班的数量。
arr_del15：延误15分钟及以上的航班数量。
carrier_ct：因航空公司原因造成的航班延误数量。
weather_ct：由于天气原因造成的航班延误数量。
nas_ct：由于国家空域系统 (NAS) 造成的航班延误数量。
security_ct：由于安全问题导致的航班延误数量。
late_aircraft_ct：由于飞机迟到而导致的航班延误数量。
arr_cancelled：被取消的抵达航班数量。
arr_diverted：改道的抵达航班数量。
arr_delay：到达延误的总分钟数。
carrier_delay：归因于航空公司的延误总分钟数。
weather_delay：由于天气原因造成的延误总分钟数。
nas_delay：由于 NAS 问题导致的延迟总分钟数。
security_delay：由于安全问题导致的延迟总分钟数。
late_aircraft_delay：由于飞机迟到而造成的延误总分钟数。
'''




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
## import pacakge

airports_data = pd.read_csv('D:/Duke/UWA/2023S2/5101/Team assignment/airports.csv')
airline_delay_data = pd.read_csv('D:/Duke/UWA/2023S2/5101/Team assignment/airline_delay_causes_Feb2020.csv')




## 1.1 for loop