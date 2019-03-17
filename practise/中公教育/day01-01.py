num = int(input("请输入物品总数："))

u_time = int(input("请输入物品单价："))

total_price = num * u_time

price = int(input("给超市的总钱数："))

zhaoling = price - total_price

print("找零：{}".format(zhaoling))


"""
作业：
超市找零钱（比如学校只采购篮球）
使用input()方法，分别输入篮球个数和单价，计算要付的总价钱。
然后在使用input()输入总付金额，总付金额大于等于总价钱
然后输出找零多少钱，用代码实现。
"""



