import tkinter as tk
import random

# 创建主窗口
root = tk.Tk()
root.title("生日快乐")

# 设置窗口大小和背景颜色
root.geometry("500x400")
root.configure(bg="black")

# 创建画布
canvas = tk.Canvas(root, width=500, height=400, bg="black")
canvas.pack()

# 定义烟花效果函数
def firework():
    x = random.randint(0, 500)
    y = random.randint(0, 400)
    canvas.create_oval(x, y, x+10, y+10, fill="white")
    canvas.after(50, firework)

# 创建生日快乐的标签
label = tk.Label(root, text="祝你生日快乐！", font=("Arial", 30), bg="black", fg="white")
label.pack()

# 开始烟花效果
firework()

# 进入主循环
root.mainloop()
