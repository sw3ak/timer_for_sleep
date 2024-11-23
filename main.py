import time
from tkinter import *
import os

run_timer = True


def start():
    global run_timer
    run_timer = True
    btn_start.pack_forget()
    btn_stop.pack()
    duration = int(time_on_min.get())
    duration = duration*60
    os.system(f'shutdown -s -f -t {duration}')
    while run_timer:
        if duration > 0:
            m, s = divmod(int(duration), 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            count_time['text'] = min_sec_format
            count_time.update()
            time.sleep(1)
            duration -= 1
        if duration == 0:
            run_timer = False


def stop():
    global run_timer
    btn_start.pack()
    btn_stop.pack_forget()
    count_time['text'] = "00:00"
    count_time.update()
    run_timer = False
    os.system('shutdown -a')



app = Tk()
app.title('Таймер сна')
app.geometry('500x300')
app.geometry(f"+{(app.winfo_screenwidth() - 500) // 2}+{(app.winfo_screenheight() - 300) // 2}")
count_time = Label(app, text='--:--', font='Arial 20 bold')
count_time.pack(pady=[50, 25])
time_on_min = Entry(app, font='Arial 20 bold', width=5, justify=CENTER)
time_on_min.pack(pady=[0, 25])
btn_start = Button(app, text='Запустить таймер', font='Arial 12', width=15, command=start)
btn_start.pack()
btn_stop = Button(app, text='Остановить', font='Arial 12', width=15, command=stop)
btn_stop.pack()
app.mainloop()