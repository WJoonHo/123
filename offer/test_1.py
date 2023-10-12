
"""
1、定义一个列表info_list = [{“name”: “小明”, “age”: 5}, {“name”: “小刚”, “age”: 8},
{“name”: “大明”, “age”: 3}，{“age”: 6}]，按照列表中的字典的age的大小，由小到大进行排序。
"""

info_list = [{"name": "小明", "age": 5}, {"name": "小刚", "age": 8},
             {"name": "大明", "age": 3}, {"age": 6}]

print(sorted(info_list, key=lambda x: x["age"]))
