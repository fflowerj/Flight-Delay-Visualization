import pandas as pd
from geopy.geocoders import Nominatim
import time

# 读取原始文件
df = pd.read_csv('T_ONTIME_REPORTING.csv')

# 提取唯一的城市
unique_cities = set(df['ORIGIN_CITY_NAME']).union(set(df['DEST_CITY_NAME']))

# 初始化地理编码器
geolocator = Nominatim(user_agent="city_coordinates_generator")

# 定义缓存字典
city_coords_cache = {}

# 获取城市坐标的函数
def get_coordinates(city):
    # 检查缓存
    if city in city_coords_cache:
        return city_coords_cache[city]
    try:
        # 获取坐标
        location = geolocator.geocode(city)
        if location:
            coords = (location.latitude, location.longitude)
            city_coords_cache[city] = coords  # 缓存结果
            return coords
    except Exception as e:
        print(f"Error fetching coordinates for {city}: {e}")
        return None, None
    # 避免过快请求，添加延迟
    time.sleep(1)
    return None, None

# 创建城市坐标列表
city_coordinates = []
for city in unique_cities:
    lat, lon = get_coordinates(city)
    if lat is not None and lon is not None:
        city_coordinates.append({'city_name': city, 'latitude': lat, 'longitude': lon})

# 转换为DataFrame
city_coords_df = pd.DataFrame(city_coordinates)

# 保存为CSV文件
city_coords_df.to_csv('city_coordinates.csv', index=False)

print("城市坐标文件已生成：city_coordinates.csv")
