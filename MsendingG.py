import pyautogui
import pyperclip
import time
import os
import sys
import tkinter as tk

#设置发送内容
#设置发送次数
pp = 1
window = tk.Tk()
window.title(r"输入发送的内容和发送次数,\n用以分条,5T5啊啊啊啊啊啊哈哈哈哈哈哈哈5T5啊啊啊啊啊啊哈哈哈哈哈哈哈5T5啊啊啊啊啊啊哈哈哈哈哈哈哈5T5啊啊啊啊啊啊哈哈哈哈哈哈哈5T5啊啊啊啊啊啊哈哈哈哈哈哈哈")
window.geometry("614x214")
l1 = tk.Label(window,text="输入内容",font=('TimesNewRoman',10))
o = tk.Entry(window)
l2 = tk.Label(window,text="输入发送次数",font=('TimesNewRoman',10))
e = tk.Entry(window)
l1.pack()
o.pack()
l2.pack()
e.pack()
content_ = ""
def get():
    global pp
    pp = int(e.get())
    window.quit()
    global content_
    content_ = o.get() 
b = tk.Button(window, text="OK", command=get)
b.pack()
window.mainloop()

#UI
win = tk.Tk()
win.title("5T5啊啊啊啊啊啊哈哈哈哈哈哈哈")
win.geometry("1614x514")

# try:
#     with open("con.txt", "r", encoding='utf-8') as f:  #打开文本
#         content_  = f.read()
#     f.close()
# except IOError:
#     open("con.txt",'x')
#     sss = "未获取到内容，请往"
#     sss += "con.txt"
#     sss += "内添加文件内容！"
#     l2 = tk.Label(win,text=sss,font=('TimesNewRoman',20))
#     l2.pack()
#     win.mainloop()
#     sys.exit(0)

#发送消息
#准备时间
time.sleep(5)

#遍历内容
c = 0
ss = ""

while pp > 0:
    pp = pp-1
    for l in content_.split(r"\n"):#按行分割
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
            sss = "未获取到内容"
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
