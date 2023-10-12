"""将分数：“3/5”转换成小数0.6，并打印输出"""

from fractions import Fraction

fraction_str = "3/5"
decimal = float(Fraction(fraction_str))

print(decimal)
