from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
def create_connection(db_file):
    con = None
    try:
        con = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return con

def Show_Log():

    window = Tk()
    window.title("Logs")
    window.minsize(width=900, height=400)
    window.geometry("900x500")

    canvas = Canvas(window)
    canvas.config(bg="#008B8B")
    canvas.pack(expand=True, fill=BOTH)

    label = Frame(window, bg="#00008B")
    label.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.7)

    columnText = Label(label, text="%10s %15s %20s %30s %30s %30s"%('Book ID','Name','Issue Date','Expected return date','Return date','fine'),
                    bg="#00008B", fg="white")
    columnText.place(relx=0.07, rely=0.1)

    y = 0.25
    con = create_connection(r"library.db")
    cur = con.cursor()

    member = "memberInfo"
    try:
        getBooks = "select * from " + member
        cur.execute(getBooks)
        con.commit()

        for i in cur:
            Label(label, text="%10s %20s %23s %28s %37s %31s"%(i[0],i[1],i[2],i[3],i[4],i[5]),
                    bg="#00008B", fg="white").place(relx=0.07, rely=y)
            y += 0.1

    except:
        messagebox.showinfo("Error","Unable to access to database")

    closebtn = Button(window, text="Close", bg="white", fg="black", command=window.destroy)
    closebtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    window.mainloop()