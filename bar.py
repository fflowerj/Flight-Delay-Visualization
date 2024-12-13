import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('T_ONTIME_MARKETING.csv')

# 计算不同公司的不同原因的平均延误时间
delay_columns = ['CARRIER_DELAY', 'WEATHER_DELAY', 'NAS_DELAY', 'SECURITY_DELAY', 'LATE_AIRCRAFT_DELAY']
average_delays = data.groupby('OP_UNIQUE_CARRIER')[delay_columns].mean().reset_index()

# 设置颜色方案（色盲友好）
colors = {
    'CARRIER_DELAY': '#004488',        # Navy
    'WEATHER_DELAY': '#44AA99',        # Teal
    'NAS_DELAY': '#DDCC77',            # Goldenrod
    'SECURITY_DELAY': '#CC6677',       # Magenta
    'LATE_AIRCRAFT_DELAY': '#8899CC'   # Slate Blue
}

# 设置图形样式
plt.figure(figsize=(14, 8))  # 调整宽度，给图例腾出空间
bar_width = 0.5

# 绘制堆积条形图
plt.bar(average_delays['OP_UNIQUE_CARRIER'],
        average_delays['CARRIER_DELAY'],
        width=bar_width,
        label='CARRIER_DELAY',
        color=colors['CARRIER_DELAY'])
plt.bar(average_delays['OP_UNIQUE_CARRIER'],
        average_delays['WEATHER_DELAY'],
        bottom=average_delays['CARRIER_DELAY'],
        width=bar_width,
        label='WEATHER_DELAY',
        color=colors['WEATHER_DELAY'])
plt.bar(average_delays['OP_UNIQUE_CARRIER'],
        average_delays['NAS_DELAY'],
        bottom=average_delays['CARRIER_DELAY'] + average_delays['WEATHER_DELAY'],
        width=bar_width,
        label='NAS_DELAY',
        color=colors['NAS_DELAY'])
plt.bar(average_delays['OP_UNIQUE_CARRIER'],
        average_delays['SECURITY_DELAY'],
        bottom=average_delays['CARRIER_DELAY'] + average_delays['WEATHER_DELAY'] + average_delays['NAS_DELAY'],
        width=bar_width,
        label='SECURITY_DELAY',
        color=colors['SECURITY_DELAY'])
plt.bar(average_delays['OP_UNIQUE_CARRIER'],
        average_delays['LATE_AIRCRAFT_DELAY'],
        bottom=average_delays['CARRIER_DELAY'] + average_delays['WEATHER_DELAY'] + average_delays['NAS_DELAY'] + average_delays['SECURITY_DELAY'],
        width=bar_width,
        label='LATE_AIRCRAFT_DELAY',
        color=colors['LATE_AIRCRAFT_DELAY'])

# 图形美化
plt.title('Average Delay Time by Cause for Different Carriers (July 2024)', fontsize=16)
plt.xlabel('Unique Carrier', fontsize=14)
plt.ylabel('Average Delay Time (minutes)', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)

# 图例调整到右上角
plt.legend(title='Delay Causes', fontsize=12, title_fontsize=14, loc='upper left', bbox_to_anchor=(1, 1))

# 调整布局以避免重叠
plt.tight_layout()

# 保存图形
plt.savefig('average_delay_by_cause.png', bbox_inches='tight')  # 确保图例在导出时不被裁剪
plt.show()

# 输出统计数据
print(average_delays)
