# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  ClockBeta.py
@Time    :  2022/5/31 08:03
@Author  :  OppenheimerShen
@Contact :  sya_123123@outlook.com
@License :  (C)Copyright 2022-2023
@version :  0.0.2
@mainIdea:
"""

import time  # 用于计时
import tkinter  # 用于创建GUI界面
from tkinter import *  # 用于创建各种控件


class Clock:
    """时间类"""

    def __init__(self):
        """初始化该类"""
        self.stopwatch = None
        self.timer_button = None
        self.input_h = None
        self.show_fact_time = None

        self.show_timer_sec=None
        self.show_timer_min=None
        self.show_timer_h=None
        self.root = tkinter.Tk()  # 创建主屏幕

    def get_time(self):
        """用于获取实时时间"""
        timestr = time.strftime("%H:%M:%S")  # 获取当前的时间并转化为z字符串
        self.show_fact_time.configure(text=timestr)
        self.root.after(1000, self.get_time)

    def timer(self):
        """计时器"""
        self.root.geometry("200x150")

        self.input_h = Entry()
        self.input_h.place(x=10, y=90, height=30, width=40)

        self.input_min = Entry()
        self.input_min.place(x=50, y=90, height=30, width=40)

        self.input_s = Entry()
        self.input_s.place(x=90, y=90, height=30, width=40)

        self.typing_hint = Label(text="HOUR/MIN/SEC", fg="blue", font=("黑体", 15))
        self.typing_hint.place(x=20, y=120)

        self.timer_ok = Button(text="OK", command=lambda: self._timer_ok())
        self.timer_ok.place(x=140, y=90, height=30, width=50)
        self.time_cancel = Button(text="Cancel", command=lambda: self._timer_cancel())
        self.time_cancel.place(x=140, y=120, height=25, width=50)

    def _timer_ok(self):
        """开始倒计时"""

        self.timer_sec = int(self.input_s.get())
        self.timer_min = int(self.input_min.get())
        self.timer_h = int(self.input_h.get())

        self.del_timer_choice()

        self.show_timer_fact_time_all=Label(text="")
        self.show_timer_fact_time_all.pack(side='top',fill='y',expand=True)

        self._timer_ok_progress()

    def _timer_ok_progress(self):
        """倒计时处理区"""

        self.timer_sec = self.timer_sec - 1
        if self.timer_sec == 0 and self.timer_min != 0:
            self.timer_sec = 60
            self.timer_min = self.timer_min - 1
        if self.timer_min == 0 and self.timer_h != 0:
            self.timer_min = 60
            self.timer_h = self.timer_h - 1
        if self.timer_h == 0 and self.timer_min == 0 and self.timer_sec == 0:
            pass

        if self.timer_sec < 10:
            self.show_timer_sec = f"0{self.timer_sec}"

        if self.timer_min < 10:
            self.show_timer_min = f"0{self.timer_min}"

        if self.timer_h < 10:
            self.show_timer_h = f"0{self.timer_h}"

        self.show_timer_fact_time=f"{self.show_timer_h}:{self.show_timer_min}:{self.timer_h}"

        self.show_timer_fact_time_all.configure(text=self.show_timer_fact_time)

        self.root.after(1000, self._timer_ok_progress)

    def _timer_cancel(self):
        """在倒计时选择界面退出"""

        # 删除timer下的控件并还原尺寸
        self.root.geometry("200x100")
        self.del_timer_choice()

    def del_timer_choice(self):
        """删除倒计时选择界面的控件"""
        self.input_s.destroy()
        self.input_min.destroy()
        self.input_h.destroy()
        self.typing_hint.destroy()
        self.timer_ok.destroy()
        self.time_cancel.destroy()

    def main(self):
        """主程序"""
        self.root.title("时钟")  # 设置主屏幕标题
        self.root.geometry("200x100")  # 设置尺寸
        self.root.resizable(False, False)  # 不可缩放

        # 定义计时器按钮
        self.timer_button = Button(text="计时器", command=lambda: self.timer())
        self.timer_button.place(x=20, y=50, height=40, width=80)
        # 定义秒表按钮
        self.stopwatch = Button(text="秒表")
        self.stopwatch.place(x=100, y=50, height=40, width=80)

        self.show_fact_time = tkinter.Label(text="", fg="black", font=("黑体", 40))
        # 初始化显示时间的标签
        self.show_fact_time.pack()  # 使用pack函数封装

        self.get_time()  # 调用更新时间函数

        self.root.mainloop()  # 进入循环


if __name__ == "__main__":
    Clock().main()
