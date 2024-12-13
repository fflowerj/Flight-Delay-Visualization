import pandas as pd
import folium

# 读取航班数据
df = pd.read_csv('T_ONTIME_REPORTING.csv')

# 读取城市坐标数据
city_coords = pd.read_csv('city_coordinates.csv')

# 合并延误数据和城市坐标
df = df.merge(city_coords, left_on='ORIGIN_CITY_NAME', right_on='city_name', how='left')
df.rename(columns={'latitude': 'ORIGIN_LAT', 'longitude': 'ORIGIN_LON'}, inplace=True)

# 合并终点城市坐标
df = df.merge(city_coords, left_on='DEST_CITY_NAME', right_on='city_name', how='left')
df.rename(columns={'latitude': 'DEST_LAT', 'longitude': 'DEST_LON'}, inplace=True)

# 计算每个航班的延误总时间
df['TOTAL_DELAY'] = df[['CARRIER_DELAY', 'WEATHER_DELAY', 'NAS_DELAY', 'SECURITY_DELAY', 'LATE_AIRCRAFT_DELAY']].sum(axis=1)

# 计算每个城市的平均延误情况
city_delay = df.groupby(['ORIGIN_CITY_NAME', 'ORIGIN_LAT', 'ORIGIN_LON']).agg(
    total_delay=('TOTAL_DELAY', 'mean'),
    carrier_delay=('CARRIER_DELAY', 'mean'),
    weather_delay=('WEATHER_DELAY', 'mean'),
    nas_delay=('NAS_DELAY', 'mean'),
    security_delay=('SECURITY_DELAY', 'mean'),
    late_aircraft_delay=('LATE_AIRCRAFT_DELAY', 'mean')
).reset_index()

# 定义函数获取主要延误原因
def get_primary_delay(row):
    # 获取最大延误的列
    delay_types = ['carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay']
    max_delay_type = max(delay_types, key=lambda x: row[x])
    if row[max_delay_type] > 0:
        # 返回主要延误原因的名称
        return max_delay_type.replace('_', ' ').title()
    return 'No significant delay'

# 计算每个城市的主要延误原因
city_delay['primary_delay'] = city_delay.apply(get_primary_delay, axis=1)

# 创建基础地图
map_center = [39.8283, -98.5795]  # 美国中心位置
my_map = folium.Map(location=map_center, zoom_start=5)

# 在地图上添加城市信息
for _, row in city_delay.iterrows():
    delay = row['total_delay']
    primary_delay = row['primary_delay']
    color = 'green' if delay < 20 else '#F4C542' if delay < 50 else 'red'  # 根据延误时间设置颜色

    # 定义弹出框HTML内容，设置宽度并不换行
    popup_html = f"""
    <b>City:</b> {row['ORIGIN_CITY_NAME']}<br>
    <b>Avg Delay:</b> {delay:.2f} min<br>
    <b>Main Delay Cause:</b> {primary_delay}
    """
    popup = folium.Popup(popup_html, max_width=300, min_width=250)  # 设置宽度限制

    # 添加圆圈标记
    folium.CircleMarker(
        location=[row['ORIGIN_LAT'], row['ORIGIN_LON']],
        radius=6,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
        popup=popup
    ).add_to(my_map)

# 保存地图为HTML文件
my_map.save('average_flight_delays_map_with_custom_popup.html')

print("地图已成功生成并保存为 'average_flight_delays_map_with_custom_popup.html'")
