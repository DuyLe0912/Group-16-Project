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

allBid = []

def return_book_query():

    b_id = book_id.get()
    con = create_connection(r"library.db")
    cur = con.cursor()
    issueTable = "books_issued"
    bookTable = "books"
    member = "memberInfo"
    try:
        extractBid = "select bid from " + issueTable
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if b_id in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+b_id+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'issued':
                status = True
            else:
                status = False
        
        else:
            messagebox.showinfo("Error", "Book Id is NOT FOUND")

    except:
        messagebox.showinfo("Error", "Can't Access to database")

    try:
        delIssue = "delete from " + issueTable + " where bid = '" + b_id + "';"
        updateStatus = "update " + bookTable + " set status = 'available' where bid='" + b_id + "';"
        setReturn = "update " + member + " set returnDate = date('now') where bid='" + b_id + "';"
        setFine = "update " + member + " set fine = (select julianday(returnDate) - " \
                                       "julianday(e_returnDate) from memberInfo)" \
                                       "*2 where bid='" + b_id + "';"
        checkFine = "update " + member + " set fine = case when fine < 0 then 0 " \
                                         "else fine end where bid='" + b_id + "';"
        if b_id in allBid and status == True:
            cur.execute(delIssue)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            cur.execute(setReturn)
            con.commit()
            cur.execute(setFine)
            con.commit()
            cur.execute(checkFine)
            con.commit()
            messagebox.showinfo('Success', "Book returned successfully")
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Book is either NOT EXIST or ALREADY RETURNED")
            window.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "Invalid Book ID")

    allBid.clear()
    window.destroy()

def returnBook():
    global window, book_id

    window = Tk()
    window.title("Return Book")
    window.minsize(width=400, height=200)
    window.geometry("500x300")

    canvas = Canvas(window)
    canvas.config(bg="#008B8B")
    canvas.pack(expand=True, fill=BOTH)

    label = Frame(window, bg="#00008B")
    label.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)

    #book id
    label1 = Label(label, text="Book ID", bg="#00008B", fg="white")
    label1.place(relx=0.05, rely=0.5)

    book_id = Entry(label)
    book_id.place(relx=0.3, rely=0.5, relwidth=0.62)

    #submit Button
    returnbtn = Button(window, text="Return", bg="white", fg="black", command=return_book_query)
    returnbtn.place(relx=0.28, rely=0.8, relwidth=0.18, relheight=0.08)

    closebtn = Button(window, text="Close", bg="white", fg="black", command=window.destroy)
    closebtn.place(relx=0.53, rely=0.8, relwidth=0.18, relheight=0.08)

    window.mainloop()
