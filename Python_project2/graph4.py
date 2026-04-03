"""
sort方法：
之前的sorted方法可以对数据容器进行排序，但是对列表进行指定排序规则的话，sorted函数就无法完成了
使用方式：
列表.sort(key=选择排序依据的函数，reverse=Ture|False)
（1. 参数key，是要求传入一个函数，表示将列表的每一个元素都传入函数当中，返回排序的依据
  2. 参数reverse，是否反转排序结果，True表示降序，False表示升序）
"""
my_list = [['a', 33], ['b', 66], ['c', 99]]
def choose_sort_key(element):
    return element[1]
my_list.sort(key=choose_sort_key, reverse=True)
print(my_list)
# 也可以用lambda匿名函数
# my_list.sort(key=lambda element: element[1], reverse=True)

"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
# 读取数据
f = open("1960-2019全球数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
# 关闭文件
f.close()
# 删除第一条数据
data_lines.pop(0)
# 将数据转换为字段存储
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2]
    # 开始判断字典里面有没有指定的key
    try: data_dict[year].append([country, gdp])
    except KeyError: data_dict[year] = []  
                     data_dict[year].append([country, gdp])
# 创建时间对象
timeline =Timeline({"theme": ThemeType.LIGHT})
# 排序年份
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1]. reverse=True)
    # 取出年份前八的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1]/100000000)
    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right")
    # 反转xy轴
    bar.reverse_axis()
    # 设置每一年的图标的标题
    bar.set_global_opts(title_opts=TitleOpts(title=f"{year}年全球前8GDP数据"))
    timeline.add(bar, str(year))
# for循环每一年的数据，基于每一年的数据，创建每一年的bar对象
# 在for中，将每一年的bar对象添加到时间线当中
# 设置时间线自动播放
timeliness.add_schema(play_interval=1000,
                      is_timeline_show=True,
                      is_auto_play=True,
                      is_loop_play=False
)
# 绘图
timeline.render("1960-2019年全球GDP前八.html")
"""