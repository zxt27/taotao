i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j}*{i}={i * j}\t', end=" ")
        j += 1
    print()
    i += 1

x = 1
while x <= 9:#次循环控制 行数9
    y = 1                                                   #也就是x控制y
    while y <= x:    #此循环限制 列数9
        print(f'{y}*{x}={y * x}', end=',')
        y += 1
    print("b")
    x += 1


print("我叫张先韬", end='')
print(1)
print("你好", end='')#end后接print重置换行
print(1)
