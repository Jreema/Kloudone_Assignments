import time
from tkinter import *
from playsound import playsound

my_window = Tk()
my_window.title("Alarm Clock")

def display_time():
    current_time = time.strftime("%H:%M:%S:%p")
    l1['text'] = current_time
    #l1.configure(text=current_time)
    my_window.after(1000,display_time)

def check_alarm(h,m,d):
    if d=="pm" or d=="PM":
        h =h +12
    while True:
        if(h ==time.localtime().tm_hour and m == time.localtime().tm_min):
            l1['text'] = "Alarm went on"
            playsound("/Users/jasmathi/Documents/KloudOne/Python/Class5Assignment/alarm.mp3")
            break

def set_alarm(event):
    global str_day,str_hr,str_min
    res1=""
    str_time=t1.get()
    res = "Alarm has been set to " + str_time
    try:
        str_day=str_time[-2:]
        str_min=int(str_time[3:5])
        str_hr=int(str_time[:2])
    except:
        res1 = "The time should be in hh:mm am or hh:mm pm format"
        l2['text'] =res1
    if res1=="":
        l1['text']=res
    check_alarm(str_hr, str_min, str_day)


str_hr=str_min=0
str_day=""

l1= Label(my_window,text ="Enter the Time",font=("Arial",12),fg="blue")
l1.pack(ipady=10)
t1 =Entry(my_window,width=10)
t1.pack(ipady=10)
l2 =Label(my_window,text="")
l2.pack(ipady=10)
b1 = Button(my_window, text="Set Alarm",bg="skyblue",fg="white")
b1.bind("<Button-1>",set_alarm)
b1.pack(ipady=10)
my_window.mainloop()