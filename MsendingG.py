import pyautogui
import pyperclip
import time
import os
import sys
import tkinter as tk

#设置发送次数
pp = 1
window = tk.Tk()
window.title("输入发送次数")
window.geometry("514x114")
e = tk.Entry(window)
e.pack()
def get():
    global pp
    pp = int(e.get())
    window.quit()
b = tk.Button(window, text="OK", command=get)
b.pack()
window.mainloop()

#UI
win = tk.Tk()
win.title("5T5啊啊啊啊啊啊哈哈哈哈哈哈哈")
win.geometry("1614x514")

#检查文件是否存在且创建内容文件并获取文件位置
# s = __file__
# s1 = ""
# for i in s[0:-9]:
#     s1=s1+i
# s1=s1+"con.txt"
a = 1
try:
    with open(r"C:\Users\con.txt", "r", encoding='utf-8') as f:  #打开文本
        content_  = f.read()
    f.close()
except IOError:
    a = 2
if a == 2:
    open(r"C:\Users\con.txt",'w')
    sss = "未获取到内容，请往"
    sss += r"C:\User\con.txt"
    sss += "内添加文件内容！"
    l2 = tk.Label(win,text=sss,font=('TimesNewRoman',20))
    l2.pack()
    win.mainloop()
    sys.exit(0)
else:
#读取内容文件
    with open(r"C:\Users\con.txt", "r", encoding='utf-8') as f:  #打开文本
        content_  = f.read()   #读取文本

#发送消息
#准备时间
time.sleep(5)

#遍历内容
c = 0
ss = ""

while pp > 0:
    pp = pp-1
    for l in content_.split('\n'):#按行分割
        if l:
        #成功获取内容
        #print("已成功获取内容，准备发送！内容为：",l,"\n")
            c = 1
            ss = ss+l+"\n"

        #复制
            pyperclip.copy(l)

        #复制到聊天窗口
            pyautogui.hotkey('ctrl','v')

        #按回车
            pyautogui.typewrite('\n')
        else:
            sss = "未获取到内容，请往"
            sss += r"C:\Users\con.txt"
            sss += "内添加文件内容！"
            l2 = tk.Label(win,text=sss,font=('TimesNewRoman',20))
            l2.pack()
            win.mainloop()
        #print("未获取到内容，请检查是否录入内容！")
if c == 1:
    win.geometry("1114x714")
    ssss = "获取内容为:"+ss+"已发送"
    l1 = tk.Message(win,text=ssss,font=('TimesNewRoman',20))
    l1.pack()
    l1.mainloop()

