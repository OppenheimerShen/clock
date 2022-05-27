import time
import tkinter
from tkinter import *

CountDownTime=''

def getTime():

	timestr = time.strftime("%H:%M:%S") # 获取当前的时间并转化为字符串
	lb.configure(text = timestr)
	root.after(1000, getTime)

def countdown():

    root = tkinter.Tk()
    root.title("输入时间")
    input = tkinter.Entry(root)
    input.pack()

    def getCountDown():
        global CountDownTime
        CountDownTime = input.get()

    enter = tkinter.Button(root, text="确定", command=lambda:getCountDown())
    enter.pack()



root = tkinter.Tk()

root.title(CountDownTime)

root.title('时钟')
root.geometry("200x100")

timer = Button(root, text='计时器', command=lambda:countdown())
timer.place(x=20, y=50, height=40, width=80)


stopwatch = Button(root, text='秒表')
stopwatch.place(x=100, y=50, height=40, width=80)

lb = tkinter.Label(text = '', fg = 'black', font = ('黑体', 40))

lb.pack()

getTime()

root.mainloop()
