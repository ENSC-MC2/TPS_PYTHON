from tkinter import *

global formul

formul = ""

def equalclick():
    equation.delete(0,END)
    equation.insert(0,eval(formul))


def effacer():
    global formul
    formul = ""
    equation.delete(0,END)


def click(s):
    global formul

    if s == "Efface":
        effacer()

    elif s == "=":
        equalclick()
    
    else:
        formul += s
        equation.insert(END,s)


window = Tk()
window.title("Calculatrice")
window.geometry("300x300")
window.resizable(False, False)

equation = Entry(window, width=40)
equation.grid(column=0, row=0, columnspan=4)

l = ["1", "2", "3", "+", "4", "5", "6", "-", "7", "8", "9", "*", "0", ".", "%", "/", "Efface", "="]

for i in range(len(l)):
    btn = Button(window, text=l[i], width=8, height=3)
    btn.grid(column=i % 4, row=i // 4 + 1 )
    btn["command"] = lambda btn=btn: click(btn["text"])

window.mainloop()