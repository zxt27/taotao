name = "弱智传媒"
gugia = 1
cde = "0001"
cz = 1.5
day = 6
print(f"公司名称:{name}\n股票代码:{cde}\n当前股价:{gugia}元")
print("每日增长系数：%.2f，经过%d天增长后，股价达到了：%.2f" % (cz, day, (day*cz)))

