# @Time : 2020/7/8 0008 10:08 
# @Author : liuxinxin885
# @File : 随机序列.py 
# @Software: PyCharm
import random
f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d=random.sample(f, 5)
d2=random.sample(f, len(f))

print(f)
print(d)
print(d2)