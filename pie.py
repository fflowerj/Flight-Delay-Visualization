import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('T_ONTIME_MARKETING.csv')

# 计算各原因的总延误时间
delay_columns = ['CARRIER_DELAY', 'WEATHER_DELAY', 'NAS_DELAY', 'SECURITY_DELAY', 'LATE_AIRCRAFT_DELAY']
total_delays = data[delay_columns].sum()

# 设置颜色方案（与条形图一致）
colors = {
    'CARRIER_DELAY': '#004488',        # Navy
    'WEATHER_DELAY': '#44AA99',        # Teal
    'NAS_DELAY': '#DDCC77',            # Goldenrod
    'SECURITY_DELAY': '#CC6677',       # Magenta
    'LATE_AIRCRAFT_DELAY': '#8899CC'   # Slate Blue
}

# 绘制饼状图
plt.figure(figsize=(8, 8))
plt.pie(
    total_delays,
    labels=delay_columns,
    autopct='%1.1f%%',
    startangle=140,
    colors=[colors[col] for col in delay_columns],
    textprops={'fontsize': 12}
)

# 图形美化
plt.title('Proportion of Delay Causes (July 2024)', fontsize=16)
plt.tight_layout()

# 保存图形
plt.savefig('delay_causes_pie_chart.png')
plt.show()
