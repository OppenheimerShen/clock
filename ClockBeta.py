import time
import tkinter
from tkinter import *

class clock:

    def __init__(self) -> None:
        self.root = tkinter.Tk()

    def getTime(self):

        timestr = time.strftime("%H:%M:%S") # 获取当前的时间并转化为字符串
        self.lb.configure(text = timestr)
        self.root.after(1000, self.getTime)

    def countdownStarts(self):
        allTimeSec=self.hour*3600+self.min*60+self.sec
        while allTimeSec==0:
            self.sec=self.sec-1
            if self.sec==0:
                self.min-1
                self.sec=60
            if self.min==0:
                self.hour-1
                self.min=60
            text=f'{self.hour}:{self.min}:{self.sec}'
            CountDownTime=time+allTimeSec.strftime("%H:M%:S%")
            self.endCountDownTime=Label(text="{CountDownTime}")
            self.endCountDownTIme.place(x=20, y=120)

    def timeProcessing(self, time):

        newTime=[]
        for i in time:
            i=int(i)
            newTime.append(i)
        B_hour=newTime[0:2]
        B_min=newTime[2:4]
        B_sec=newTime[4:6]

        self.hour=B_hour[0]*10+B_hour[1]
        self.min=B_min[0]*10+B_min[1]
        self.sec=B_sec[0]*10+B_sec[1]

        self.startOperation()




    def CountDown(self):
        self.root.geometry("200x180")
        self.enter_CountDown = tkinter.Entry()
        self.enter_CountDown.place(x=5, y=90)

        self.hint_CountDown = tkinter.Label(text="XXXXXX\n(h/min/s)",
                    font=('', 15))

        self.hint_CountDown.place(x=12, y=120)

        self.OK_CountDown = tkinter.Button(text="OK",
                    command=lambda:self.startOperation(self.timeProcessing(self.enter_CountDown.get())),
                    width=5)

        self.OK_CountDown.place(x=110, y=118)
        self.Cancel_CountDown = tkinter.Button(text="Cancel", width=5)
        self.Cancel_CountDown.place(x=110, y=145)

    def startOperation(self):


        self.enter_CountDown.destroy()
        self.hint_CountDown.destroy()
        self.OK_CountDown.destroy()
        self.Cancel_CountDown.destroy()
        self.root.geometry('200x140')

        self.hint_start_CountDown = Label(text=f"倒计时{self.hour}时{self.min}分{self.sec}秒")
        self.hint_start_CountDown.place(x=30, y=115)





    def main(self):

        self.root.title("时钟")
        self.root.geometry("200x100")
        self.lb = tkinter.Label(text = '', fg = 'black', font = ('黑体', 40))

        timer = Button(self.root, text='计时器', command=lambda:self.CountDown())
        timer.place(x=20, y=50, height=40, width=80)


        stopwatch = Button(self.root, text='秒表')
        stopwatch.place(x=100, y=50, height=40, width=80)

        self.lb.pack()

        self.getTime()

        self.root.mainloop()

if __name__ == "__main__":

    clock().main()
