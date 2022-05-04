from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def delete_book_query():
    bid = book_id.get()
    bookTable = "books"
    issue_Table = "books_issued"
    log_table = "memberInfo"
    con = create_connection(r"library.db")
    cur = con.cursor()
    try:
        deleteBk = "delete from " + bookTable + " where bid = '" + bid + "'"
        deleteIssue = "delete from " + issue_Table + " where bid = '" + bid + "' "
        deleteLog = "delete from " + log_table + " where bid = '" + bid + "' "
        cur.execute(deleteBk)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        cur.execute(deleteLog)
        con.commit()
        messagebox.showinfo("Success", "Book Deleted Successfully")

    except:
        messagebox.showinfo("Error", "Book Id not valid")


    book_id.delete(0, END)
    window.destroy()

def delete():
    global book_id, canvas, bookTable, window

    window = Tk()
    window.title("Delete Book")
    window.minsize(width=400, height=200)
    window.geometry("600x300")

    canvas = Canvas(window)
    canvas.config(bg="#008B8B")
    canvas.pack(expand=True, fill=BOTH)

    label = Frame(window, bg="#00008B")
    label.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)

    label1 = Label(label, text="Book Id: ", bg="#00008B", fg="white")
    label1.place(relx=0.05, rely=0.5)

    book_id = Entry(label)
    book_id.place(relx=0.3, rely=0.5, relwidth=0.62)

    deletebtn = Button(window, text="Delete", bg="white", fg="black", command=delete_book_query)
    deletebtn.place(relx=0.28, rely=0.8, relwidth=0.18, relheight=0.08)

    closebtn = Button(window, text="Close", bg="white", fg="black", command=window.destroy)
    closebtn.place(relx=0.53, rely=0.8, relwidth=0.18, relheight=0.08)

    window.mainloop()
