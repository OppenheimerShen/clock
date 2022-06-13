from string import hexdigits
import time  # 用于计时
import tkinter  # 用于创建GUI界面
from tkinter import *

from pyrsistent import m  # 用于创建各种控件

class Clock:
    """时间类"""

    def __init__(self):
        """初始化该类"""
        self.root = tkinter.Tk()  # 创建主屏幕

    def get_time(self):
        """用于获取实时时间"""
        timestr = time.strftime("%H:%M:%S")  # 获取当前的时间并转化为z字符串
        self.show_fact_time.configure(text=timestr)
        self.root.after(1000, self.get_time)

    def main(self):
        """主程序"""
        self.root.title("Clock")  # 设置主屏幕标题
        self.root.geometry("200x100")  # 设置尺寸
        self.root.resizable(False, False)  # 不可缩放

        # 定义计时器按钮
        self.timer_button = Button(text="Timer", command=lambda:self._timer_choose())
        self.timer_button.place(x=20, y=50, height=40, width=80)
        # 定义秒表按钮
        self.stopwatch = Button(text="Stopwatch", command=lambda:self._stopwatch_start())
        self.stopwatch.place(x=100, y=50, height=40, width=80)

        self.show_fact_time = tkinter.Label(text="", fg="black", font=("黑体", 40))
        # 初始化显示时间的标签
        self.show_fact_time.pack()  # 使用pack函数封装

        self.get_time()  # 调用更新时间函数

        self.root.mainloop()  # 进入循环

    def _timer_choose(self):
        self.root.geometry("200x140")

        self.choose_h=tkinter.Entry()
        self.choose_h.place(x=5, y=90, height=30, width=40)
        self.choose_m=tkinter.Entry()
        self.choose_m.place(x=50, y=90, height=30, width=40)
        self.choose_s=tkinter.Entry()
        self.choose_s.place(x=95, y=90, height=30, width=40)
        self.choose_hint=tkinter.Label(text="(H/M/S)")
        self.choose_hint.place(x=45, y=118)
        self.choose_ok=tkinter.Button(text='OK', command=self._timer_progress)
        self.choose_ok.place(x=135, y=90, height=45, width=60)

    def _timer_progress(self):
        self.h=int(self.choose_h.get())
        self.m=int(self.choose_m.get())
        self.s=int(self.choose_s.get())
        
        
        self.choose_h.destroy()
        self.choose_m.destroy()
        self.choose_s.destroy()
        self.choose_hint.destroy()
        self.choose_ok.destroy()

        self._timer_start()

    def _timer_start(self):
        now=time.time()
        now+=self.s+self.m*60+self.h*3600
        timeArray = time.localtime(now)
        self.checkpoint = time.strftime("%H:%M:%S", timeArray)
        self._timer_end()
        
    def _timer_end(self):
        time.sleep(self.s+self.m*60+self.h*3600)
        self.timer_end_hint=tkinter.Label(text="Finish!", font=("黑体", 30))
        self.timer_end_hint.place(x=15, y=90)
        self.timer_exit=tkinter.Button(text="Next", command=lambda: self._timer_exit())
        self.timer_exit.place(x=120, y=90)

    def _timer_exit(self):
        self.timer_exit.destroy()
        self.timer_end_hint.destroy()
        self.root.geometry("200x100")

    def _stopwatch_start(self):
        self.root.geometry("200x150")
        self.stopwatch_start_button=tkinter.Button(text="Start", command=lambda:self._stopwatch_timing())
        self.stopwatch_start_button.place(x=40, y=95, height=50, width=120)

    def _stopwatch_timing(self):
        self.stopwatch_start_button.destroy()
        self.start_time=time.time()
        now=time.strftime("%H:%M:%S")
        self.stopwatch_start_time=tkinter.Label(text=f"start time:{now}", font=("黑体", 20))
        self.stopwatch_start_time.place(x=15, y=87)
        self.stopwatch_end=tkinter.Button(text="END", command=lambda:self._stopwatch_end())
        self.stopwatch_end.place(x=50, y=115, height=30, width=100)
    def _stopwatch_end(self):
        self.stopwatch_end.destroy()
        self.stopwatch_start_time.destroy()
        
        end_time=time.time()
        time_difference=self.start_time-end_time

        self.stopwatch_time=tkinter.Label(text=abs(time_difference), font=("黑体", 17))
        self.stopwatch_time.place(x=10,  y=100, height=20)

        self.stopwatch_next=tkinter.Button(text="Next", command=lambda:self._stopwatch_del())
        self.stopwatch_next.place(x=65, y=120)

    def _stopwatch_del(self):
        self.root.geometry("200x100")
        self.stopwatch_next.destroy()
        self.stopwatch_time.destroy()
         

if __name__ == "__main__":
    Clock().main()