from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error
#function to connect to db
def create_connection(db_file):
    con = None
    try:
        con = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return con

def add_book_query():
    b_id = book_id.get()
    title = book_title.get()
    author = book_author.get()
    status = book_status.get()
    status = status.lower()
    if status != "available" and status !="issued":
        messagebox.showinfo('Error', "Status must be either avaiable or issued!")
        return

    bookTable = "books"
    issueTable = "books_issued"
    con = create_connection(r"library.db")
    cur = con.cursor()

    try:
        insertBooks = "insert into " + bookTable + " values ('" + b_id + "','" + title + "','" \
                      + author + "','" + status + "')"
        cur.execute(insertBooks)
        con.commit()
        if status == "issued":
            addIssuedBook = "insert into " + issueTable + "(bid) values ('" + b_id + "')"
            cur.execute(addIssuedBook)
            con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showinfo('Error', "Invalid or duplicated ID")

    window.destroy()

def addBook():
    global book_id, book_title, book_author, book_status,window

    window = Tk()
    window.title("Add Book")
    window.minsize(width=400, height=500)
    window.geometry("600x400")

    #create the canvas for info
    canvas = Canvas(window)
    canvas.config(bg="#008B8B")
    canvas.pack(expand=True, fill=BOTH)

    label = Frame(window, bg="#00008B")
    label.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.6)

    #book ID
    label1 = Label(label, text="Book Id: ", bg="#00008B", fg="white")
    label1.place(relx=0.05, rely=0.2, relheight=0.08)
    book_id = Entry(label)
    book_id.place(relx=0.35, rely=0.2, relwidth=0.62, relheight=0.08)

    #title
    label2 = Label(label, text="Title: ", bg="#00008B", fg="white")
    label2.place(relx=0.05, rely=0.35, relheight=0.08)
    book_title = Entry(label)
    book_title.place(relx=0.35, rely=0.35, relwidth=0.62, relheight=0.08)

    #author
    label3 = Label(label, text="Author: ", bg="#00008B", fg="white")
    label3.place(relx=0.05, rely=0.50, relheight=0.08)
    book_author = Entry(label)
    book_author.place(relx=0.35, rely=0.50, relwidth=0.62, relheight=0.08)

    #Status
    label4 = Label(label, text="Status(available/issued): ", bg="#00008B", fg="white")
    label4.place(relx=0.05, rely=0.65, relheight=0.08)
    book_status = Entry(label)
    book_status.place(relx=0.35, rely=0.65, relwidth=0.62, relheight=0.08)
    
    #Buttons
    addbtn = Button(window, text="Add", bg="white", fg="black", command=add_book_query)
    addbtn.place(relx=0.28, rely=0.82, relwidth=0.18, relheight=0.08)

    closebtn = Button(window, text="Close", bg="white", fg="black", command=window.destroy)
    closebtn.place(relx=0.53, rely=0.82, relwidth=0.18, relheight=0.08)

    window.mainloop()