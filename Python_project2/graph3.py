"""
Timeline()时间线：柱状图描述的是分类数据，解决的是每一个分类中有多少的问题。但是柱状图很难动态的描述一个趋势性的数据，时间线能够很好的解决
如果说一个bar、line对象是一张图表的话，时间线就是创建一个一维的x轴，轴上的每一个点就是一个图表对象
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
bar1 = Bar()
bar1.add_xaxis(["warriors", "lakers", "suns"])
bar1.add_yaxis("NBA23-24 season", [100, 100, 100], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()
bar2 = Bar()
bar2.add_xaxis(["warriors", "lakers", "suns"])
bar2.add_yaxis("NBA23-24 season", [50, 100, 100], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()
bar3 = Bar()
bar3.add_xaxis(["warriors", "lakers", "suns"])
bar3.add_yaxis("NBA23-24 season", [33.3, 100, 66.7], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()
bar4 = Bar()
bar4.add_xaxis(["warriors", "lakers", "suns"])
bar4.add_yaxis("NBA23-24 season", [50, 75, 50], label_opts=LabelOpts(position="right"))
bar4.reversal_axis()
bar5 = Bar()
bar5.add_xaxis(["warriors", "lakers", "suns"])
bar5.add_yaxis("NBA23-24 season", [40, 80, 80], label_opts=LabelOpts(position="right"))
bar5.reversal_axis()
bar6 = Bar()
bar6.add_xaxis(["warriors", "lakers", "suns"])
bar6.add_yaxis("NBA23-24 season", [30, 66.7, 66.7], label_opts=LabelOpts(position="right"))
bar6.reversal_axis()
timeline = Timeline()
timeline.add(bar1, "January")
timeline.add(bar2, "February")
timeline.add(bar3, "March")
timeline.add(bar4, "April")
timeline.add(bar5, "May")
timeline.add(bar6, "June")
timeline.add_schema(
    play_interval=500,    # 自动播放时间间隔，单位为毫秒
    is_timeline_show=True, # 是否在自动播放的时候显示时间线
    is_auto_play=True,     # 是否自动播放
    is_loop_play=True      # 是否循环自动播放
)
timeline.render("基础柱状时间图.html")