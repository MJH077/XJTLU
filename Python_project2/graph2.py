from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
bar = Bar()
bar.add_xaxis(["中国", "美国"])
bar.add_yaxis("GDP", [30, 20], label_opts=LabelOpts(position='right'))
bar.reversal_axis()  # 反转xy轴
bar.render("基础柱状图.html")
