from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    con = None
    try:
        con = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return con

def search_book_query():
    window = Tk()
    window.title("Result")
    window.minsize(width=400, height=400)
    window.geometry("600x500")

    canvas = Canvas(window)
    canvas.config(bg="#008B8B")
    canvas.pack(expand=True, fill=BOTH)

    label = Frame(window, bg="#00008B")
    label.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)

    # add a text label to LabeFrame
    columnText = Label(label, text="%10s %20s %40s %20s" % ('Book ID', 'Title', 'Author', 'Status'),
                      bg="#00008B", fg="white")
    columnText.place(relx=0.06, rely=0.1)

    y = 0.25


    bid = bookInfo1.get()
    #create connection to database
    con = create_connection(r"library.db")
    cur = con.cursor()

    # declare the name of tables
    bookTable = "books"


    try:
        # query to retrieve details from books table
        searchSql = "select * from " + bookTable + " where bid = '" + bid + "'"
        cur.execute(searchSql)
        con.commit()

        for i in cur:
            Label(label, text="%10s %20s %40s %30s" % (i[0], i[1], i[2], i[3]),
                  bg="#00008B", fg="white").place(relx=0.07, rely=y)

    except:
        messagebox.showinfo("Error", "Failed to Fetch files from database")

    closebtn = Button(window, text="Close", bg="white", fg="black", command=window.destroy)
    closebtn.place(relx=0.4, rely=0.8, relwidth=0.18, relheight=0.08)

    window.mainloop()

def search():
    global bookInfo1, window

    window = Tk()
    window.title("Search Book")
    window.minsize(width=400, height=300)
    window.geometry("600x300")

    canvas = Canvas(window)
    canvas.config(bg="#008B8B")
    canvas.pack(expand=True, fill=BOTH)

    label = Frame(window, bg="#00008B")
    label.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)

    #take a book ID to delete
    label1 = Label(label, text="Book ID: ", bg="#00008B", fg="white")
    label1.place(relx=0.05, rely=0.4)

    bookInfo1 = Entry(label)
    bookInfo1.place(relx=0.3, rely=0.4, relwidth=0.62)

    #submit button
    searchbtn = Button(window, text="Search", bg="white", fg="black", command=search_book_query)
    searchbtn.place(relx=0.28, rely=0.8, relwidth=0.18, relheight=0.08)

    closebtn = Button(window, text="Close", bg="white", fg="black", command=window.destroy)
    closebtn.place(relx=0.53, rely=0.8, relwidth=0.18, relheight=0.08)

    window.mainloop()
