import pandas as pd
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt



#### 数据集包含两个自变量x和y，你可以使用pandas库提供的corr()函数计算它们之间的相关系数####
correlation = data['x'].corr(data['y'])
print('Correlation:', correlation)

####你可以使用matplotlib库绘制散点图来可视化两个自变量之间的关系###
plt.scatter(data['x'], data['y'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.show()



### 绘制分布图 可能
# 创建地理编码器对象
geolocator = Nominatim(user_agent='my_app')

# 获取城市的经纬度
cities = ['New York', 'London', 'Tokyo']
locations = []
for city in cities:
    location = geolocator.geocode(city)
    if location:
        locations.append(location)

# 绘制地理坐标点
lons = [location.longitude for location in locations]
lats = [location.latitude for location in locations]

# 创建地图对象
map = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')

# 绘制海岸线
map.drawcoastlines()

# 绘制经纬线
map.drawparallels(range(-90, 91, 30), labels=[1, 0, 0, 0])
map.drawmeridians(range(-180, 181, 60), labels=[0, 0, 0, 1])

# 绘制地理坐标点
x, y = map(lons, lats)
map.scatter(x, y, marker='o', color='r')

# 显示图形
plt.show()


###############散点分布图
# 创建地理编码器对象
geolocator = Nominatim(user_agent='my_app')

# 获取城市的经纬度
cities = ['New York', 'London', 'Tokyo']
locations = []
for city in cities:
    location = geolocator.geocode(city)
    if location:
        locations.append(location)

# 绘制经纬度散点分布图
lons = [location.longitude for location in locations]
lats = [location.latitude for location in locations]

plt.scatter(lons, lats, marker='o', color='r')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('City Coordinates')
plt.show()plt.show()