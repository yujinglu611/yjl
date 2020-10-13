import random
import tkinter as tk  # 使用Tkinter前需要先导入
from tkinter import messagebox
number = random.randint(1,100)

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('猜数字')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x

label1 = tk.Label(window,fg='black',text="猜数字小游戏",font=('宋体',35,'bold'))
label1.grid(padx=75)                                    #

label2 = tk.Label(window,fg='black',text="游戏规则：\n从1到100中猜数字！！！",font=('宋体',15,'bold'))
label2.grid(padx=10,pady=10)

label3 = tk.Label(window,fg='black',text="请输入你所猜测的数字：",font=('宋体',15,'bold'))
label3.grid(padx=10,pady=10)

text = tk.Entry(window,width=30)
text.grid(padx=100)
# 建立一个按钮,command：通过按钮触发比较函数
def compare():
    use = int(text.get())
    if use == '':
        tk.messagebox.showerror('警告','输入不能让为空！！！')

    elif use > number:
        tk.messagebox.showinfo('不正确', '大了')

    elif use < number:
        tk.messagebox.showinfo('不正确', '小了')

    elif use == number:
        tk.messagebox.showinfo('正确', '恭喜你答对了')

    else :
        tk.messagebox.showerror('警告', '输入不正确！！！')
button1 = tk.Button(window, text='确定',command=compare, width=10, font=('微软雅黑', 10,))
# 设置按钮的位置
button1.grid(padx=10,pady=10)

# 建立一个按钮,command：通过按钮触发界面退出，bg是背景颜色
button2 = tk.Button(window, text='退出游戏',command=window.quit, width=10, bg='yellow', font=('微软雅黑', 10,))
button2.grid(padx=10,pady=10)
# 第6步，主窗口循环显示
window.mainloop()
