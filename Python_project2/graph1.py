"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts
# 处理数据
f_us = open("美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()
# 得到美国的全部内容
f_jp = open("日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()
# 得到日本的全部内容
f_in = open("印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()
# 得到印度的全部内容
us_data = us_data.replace("json_1629344292311_69436(", "")
jp_data = jp_data.replace("json_1629350871167_29498(", "")
in_data = in_data.replace("json_1629350745930_63180(", "")
# 去掉不合json规范的开头
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]
# 去掉不合json规范的结尾
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# json转python字典
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']
# 获取trend key
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]
# 获取日期数据，用于x轴，取2020年（到下标314结束）
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]
# 获取确定数据，用于y轴，取2020年（到下标314结束）
line = Line()
# 生成图表
line.add_xaxis(us_x_data)
# 添加x轴数据
line.add_yaxis("美国确诊人数", us_y_data)
line.add_yaxis("日本确诊人数", jp_y_data)
line.add_yaxis("印度确诊人数", in_y_data)
# 添加y轴数据
line.set_global_opts(title_opts=TitleOpts(title="美日印三国确诊人数", pos_left="center", pos_bottom="1%")
# 设置全局选项
line.render()
# 调动render方法，生成图表
f_us.close()
f_jp.close()
f_in.close()
# 关闭文件对象
"""