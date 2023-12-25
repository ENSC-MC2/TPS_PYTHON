from tkinter import *

MORABA3_SETTING = 300


window = Tk()
window.title("Example")
window.geometry("500x400")
window.resizable(False, False)
window.config(bg="red")

moraba3 = Canvas(window, width=MORABA3_SETTING, height=MORABA3_SETTING, bg="green" , bd=0 , highlightthickness=0)
moraba3.grid(column=0, row=0)

moraba4 = Canvas(window, width=MORABA3_SETTING-40, height=MORABA3_SETTING-30, bg="gray" , bd=0)
moraba4.place(x=0, y=0)
moraba4.create_oval(50, 50, 200, 200, fill="blue", outline="white", width=5)


window.mainloop()