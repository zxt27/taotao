company_name = "传媒有限公司"
print(f"公司名称：{company_name}")
name1 = input("股价：")
name1 = float(name1)

name = input("增长系数为:")
name = float(name)

name2 = input("持有天数：")
name2 = int(name2)
print(f"您的收益：{name * name2 * name1}元")
