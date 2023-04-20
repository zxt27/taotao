age = input("age：")
age = int(age)
if age >= 18:
    print("go")
else:
    print("no")

cost = input("money：")
cost = float(cost)
vip = input("vip等级：")
vip = int(vip)
if cost > 10:
    print("go")
elif vip >= 3:
    print("go")
else:
    print("no")
