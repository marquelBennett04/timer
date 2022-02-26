import time
from tkinter import *
from tkinter import font
#Creating window
clockWindow = Tk()
clockWindow.title = ("Countdown Timer")
clockWindow.geometry("500x500")
clockWindow.configure(background = "blue")
##Declaring variables
hourString = StringVar()
minuteString = StringVar()
secondString = StringVar()
##Setting strings to defualt value
hourString.set("00")
minuteString.set("00")
secondString.set("00")
##Getting user input
hourTextbox = Entry(clockWindow, width = 4, font = ("Ariel", 20, ""), textvariable = hourString )
minuteTextbox = Entry(clockWindow, width = 4, font = ("Ariel", 20, ""), textvariable = minuteString )
secondTextbox = Entry(clockWindow, width = 4, font = ("Ariel", 20, ""), textvariable = secondString )
##Centering textboxes
hourTextbox.place(x = 170, y = 180)
minuteTextbox.place(x = 220, y = 180)
secondTextbox.place(x = 270, y = 180)
#Functions
def runTimer():
    try:
        clockTime = int(hourString.get() * 3600) + int(minuteString.get() * 60 ) + int(secondString.get())
    except:
        print("Incorrect Values")

    while(clockTime > -1):
        totalMinutes, totalSeconds = divmod(clockTime, 60)

        totalHours = 0
        if(totalMinutes > 60):
            totalHours, totalMinutes = divmod(totalMinutes, 60)
        
        hourString.set("{0:2d}".format(totalHours))
        minuteString.set("{0:2d}".format(totalMinutes))
        secondString.set("{0:2d}".format(totalSeconds))

        ##Updating the interface
        clockWindow.update()
        time.sleep(1)

        ##Letting the user know if the timer has expired
        if(clockTime == 0):
            messagebox.showinfo("", "Your timer is done!")

        clockTime -= 1
#Buttons
setTimeButton = Button(clockWindow, text = "Set Time", bd = "5", command = runTimer)
setTimeButton.place(relx = 0.5, rely = 0.5, anchor = CENTER)

#Keep looping
clockWindow.mainloop()




