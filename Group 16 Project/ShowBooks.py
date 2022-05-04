from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def show_books():

    window = Tk()
    window.title("All Book")
    window.minsize(width=400, height=400)
    window.geometry("600x500")

    canvas = Canvas(window)
    canvas.config(bg="#008B8B")
    canvas.pack(expand=True, fill=BOTH)

    label = Frame(window, bg="#00008B")
    label.place(relx=0.1, rely=0.13, relwidth=0.8, relheight=0.7)

    #add a text label to LabeFrame
    columnText = Label(label, text="%10s %20s %40s %20s"%('Book ID','Title','Author','Status'),
                       bg="#00008B", fg="white")
    columnText.place(relx=0.08, rely=0.1)

    # enter table names here
    bookTable = "books"
    con = create_connection(r"library.db")
    cur = con.cursor()

    y = 0.15
    getBooks = "select * from "+ bookTable
    try:
        cur.execute(getBooks)
        con.commit()

        for i in cur:
            Label(label, text="%10s %20s %40s %30s"%(i[0],i[1],i[2],i[3]), bg="#00008B", fg="white")\
                .place(relx=0.08, rely=y)
            y += 0.1

    except:
        messagebox.showinfo("Error","Unable to access to database")

    closebtn = Button(window, text="Close", fg="black", command=window.destroy)
    closebtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    window.mainloop()
