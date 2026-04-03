"""
如果想要做出数据可视化效果图，可以借助pyecharts模块来完成
已安装完成pyecharts
"""
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
line = Line()  # 构建折线图对象
line.add_xaxis(["中国", "美国", "英国"])
line.add_yaxis("GDP", [30, 20, 10])
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)
line.render("基础折线图.html")
