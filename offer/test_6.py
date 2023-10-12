"""编程：输入一个字符串，输出该字符串的所有组合。
例如：输入字符串“123”，则输出“1”,“2”，“3”，“12”，“13”，”23”, “123”(组合中不考虑顺序，所以”12”和”21”是等价的)"""


def generate_combinations(string, prefix=""):

    print(prefix)
    if len(string) == 0:
        return

    for i in range(len(string)):
        generate_combinations(string[i+1:], prefix+string[i])


# 测试代码
input_string = "123"
generate_combinations(input_string)
