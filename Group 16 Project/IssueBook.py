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

def issue_book_query():

    bid = book_id.get()        #take the book id with get()
    issueto = mem_name.get()    #take the name to whom it is issued

    #create connection
    con = create_connection(r"library.db")
    cur = con.cursor()
    # tables name
    issueTable = "books_issued"
    bookTable = "books"
    issueTo = "memberInfo"

    try:
        extractBid = "select bid from " + bookTable
        cur.execute(extractBid)
        con.commit()

        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'available':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book Id not present")

    except:
        messagebox.showinfo("Error", "Can't fetch the Book Id")



    try:
        issueLog = "insert into " + issueTo + " (bid,name) values ('" + bid + "', '" + issueto + "');"
        issueBk = "insert into " + issueTable + " values ('" + bid + "', '" + issueto + "');"
        updateStatus = "update " + bookTable + " set status = 'issued' where bid = '" + bid + "';"
        updateIssue = "update " + issueTo + " set issueDate = date('now') where bid = '" + bid + "';"
        updateEReturn = "update " + issueTo + " set e_returnDate = date('now','+7 days') " \
                                              "where bid = '" + bid + "';"
        if bid in allBid and status == True:
            cur.execute(issueBk)
            con.commit()
            cur.execute(issueLog)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            cur.execute(updateIssue)
            con.commit()
            cur.execute(updateEReturn)
            con.commit()
            messagebox.showinfo("Success", "Book Issued successfully")
            window.destroy()
        else:
            allBid.clear()
            messagebox.showinfo("Message", "Book is either NOT EXIST or ALREADY ISSUED")
            window.destroy()
            return

    except:
        messagebox.showinfo("Search Error", "Invalid Book ID")
        window.destroy()

    allBid.clear()

def issueBook():
    global book_id, mem_name, window, status

    window=Tk()
    window.title("Issue Book")
    window.minsize(width=400, height=400)
    window.geometry("600x500")

    canvas = Canvas(window)
    canvas.config(bg="#008B8B")
    canvas.pack(expand=True, fill=BOTH)

    label = Frame(window, bg="#00008B")
    label.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)

    #Book Id
    label1 = Label(label, text="Book ID", bg="#00008B", fg="white")
    label1.place(relx=0.05, rely=0.3)

    book_id = Entry(label)
    book_id.place(relx=0.3, rely=0.3, relwidth=0.62)

    #to whom book is issued/student name
    label2 = Label(label, text="Issue To", bg="#00008B", fg="white")
    label2.place(relx=0.05, rely=0.5)

    mem_name = Entry(label)
    mem_name.place(relx=0.3, rely=0.5, relwidth=0.62)

    #Buttons
    issuebtn = Button(window, text="Issue", bg="white", fg="black", command=issue_book_query)
    issuebtn.place(relx=0.28, rely=0.8, relwidth=0.18, relheight=0.08)

    closebtn = Button(window, text="Close", bg="white", fg="black", command=window.destroy)
    closebtn.place(relx=0.53, rely=0.8, relwidth=0.18, relheight=0.08)

    window.mainloop()

