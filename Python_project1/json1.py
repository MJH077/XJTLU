"""
json是一种轻量级的数据交互格式，可以按照json指定的格式去组织和封装数据
json本质上是一个带有特定格式的字符串
json是一种在各个编程语言中流通的数据格式，负责不同编程语言中的数据传递和交互
为了让不同的语言能够相互通用的相互传递数据，json就是一种非常良好的中转数据格式
json的格式可以为：
 {"name":"admin", "age":18} 或者 [{"name":"admin", "age":18}, {"name":"root", "age":16}]
 字典或者列表中套字典
"""

import json # 导入json模块
data = [{"name":"小马", "age":18}, {"name":"小鹿", "age":40}]  # 准备符合格式json格式要求的python数据
json_str = json.dumps(data)  # 通过该方法把python数据转化为了json数据
json_str1 = json.dumps(data, ensure_ascii=False)  # 意思是不使用ascii码来转义，得到的结果是正常的
print(json_str, type(json_str))
print(json_str1, type(json_str1))
data1 = {"name":"kobe", "age":40}
json_data1 = json.dumps(data1)  # 通过该方法把json数据转化为Python数据
l = json.loads(json_data1)
print(l, type(l))

