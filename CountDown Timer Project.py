from tkinter import *

class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.pack()
        self.createWidgets()
        self._alarm_id = None
        self._paused = False
        self._starttime = 00
        self.inp

    def createWidgets(self):
        self.someFrame = Frame(self)
        self.startButton = Button(self.someFrame, text="Start",command=self.startTime)
        self.startButton.pack(side=LEFT)

        self.stopButton = Button(self.someFrame, text="Stop", command=self.stopTime)
        self.stopButton.pack(side=LEFT)

        self.resetButton = Button(self.someFrame, text="Reset", command=self.resetTime)
        self.resetButton.pack(side=LEFT)
        self.someFrame.pack(side=TOP)

        self.secFrame = Frame(self)
        self.inpl=Label(self.secFrame,text = "Input Time (in seconds)",font=('Helvetica',10))
        self.inpl.pack(side=TOP)
        self.inp= Entry(self.secFrame)
        self.inp.pack(side=TOP)
        self.secFrame.pack(side=TOP)


        self.labelvariable = StringVar()
        self.labelvariable.set("00:00")

        self.thelabel = Label(self,textvariable = self.labelvariable,font=('Helvetica',50))
        self.thelabel.pack(side=BOTTOM)


    def startTime(self):
        """ Resume """
        self._paused = False
        self._starttime=int(self.inp.get())
        print(self._starttime)
        if self._alarm_id is None:
            self.countdown(self._starttime)

    def stopTime(self):
        """ Pause """
        if self._alarm_id is not None:
            self._paused = True

    def resetTime(self):
        """ Restore to last countdown value. """
        if self._alarm_id is not None:
            self.master.after_cancel(self._alarm_id)
            self._alarm_id = None
            self._paused = False
            self.countdown(self._starttime)
            self._paused = True

    def countdown(self, timeInSeconds, start=True):
        if start:
            self._starttime = timeInSeconds
        if self._paused:
            self._alarm_id = self.master.after(1000, self.countdown, timeInSeconds, False)
        else:
            mins, secs = divmod(timeInSeconds, 60)
            timeformat = "{0:02d}:{1:02d}".format(mins, secs)
            app.labelvariable.set(timeformat)
            self._alarm_id = self.master.after(1000, self.countdown, timeInSeconds-1, False)


if __name__ == '__main__':
    root = Tk()
    root.title("Timer")
    app = Application(root)
    root.mainloop()