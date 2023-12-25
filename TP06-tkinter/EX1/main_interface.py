from tkinter import *
from DB import DB
from tkinter import messagebox


# Create a window
window = Tk()
window.title("Ex 1")
window.geometry("600x200")

def add_student():
    name = name_textbox.get()
    email = email_textbox.get()
    age = age_textbox.get()
    db = DB()
    db.insert_data(name, email, age)
    messagebox.showinfo("Info", "Student added successfully")

def quit():
    window.destroy()

def show_data():
    db = DB()
    data = db.get_data()
    win_2 = Toplevel(window)
    win_2.title("Students data")
    win_2.geometry("300x400")
    for i in range(len(data)):
        s = '''
            D : {}\n
            Name : {}\n
            Email : {}\n
            Age : {}\n
            ------------------------------
        '''.format(data[i][0], data[i][1], data[i][2], data[i][3])
        Label(win_2, text=s).grid(column=0, row=i)
    
    win_2.mainloop()
    


# Create a label
name_label = Label(window, text="name : ")
name_label.grid(column=0, row=0)

email_label = Label(window, text="email : ")
email_label.grid(column=0, row=1)

age_label = Label(window, text="age : ")
age_label.grid(column=0, row=2)

# Create a text box
name_textbox = Entry(window, width=40)
name_textbox.grid(column=1, row=0)

email_textbox = Entry(window, width=40)
email_textbox.grid(column=1, row=1)

age_textbox = Entry(window, width=40)
age_textbox.grid(column=1, row=2)

# create buttons

btn_add = Button(window, text="Ajouter", width=20, bg="green", fg="white", command=add_student)
btn_add.grid(column=0, row=4)

btn_quit = Button(window, text="Quiter", width=20, bg="red", fg="white", command=quit)
btn_quit.grid(column=3, row=4)

btn_del = Button(window, text="Afficher", width=20, bg="red", fg="white", command=show_data)
btn_del.grid(column=1, row=5)


window.mainloop()