from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from sqlite3 import Error
from AddBook import *
from ShowBooks import *
from DeleteBook import *
from IssueBook import *
from ReturnBook import *
from SearchBook import *
from ShowLogs import *

#create a window and set its attributes
window = Tk()
window.title("Library Management System")
window.minsize(width=600, height=500)
window.geometry("600x500")

#Add background Image
class bg(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)
        self.image = Image.open("lib.jpg")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)
    def _resize_image(self,event):
        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)
e = bg(window)
e.pack(fill=BOTH, expand=YES)
#Create button for all features
button1 = Button(window, text="Add Book", bg="black", fg="white", command=addBook)
button1.place(relx=0.2, rely=0.15, relwidth=0.6, relheight=0.1)

button2 = Button(window, text="Delete Book", bg="black", fg="white", command=delete)
button2.place(relx=0.2, rely=0.25, relwidth=0.6, relheight=0.1)

button3 = Button(window, text="Show All Book", bg="black", fg="white", command=show_books)
button3.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.1)

button4 = Button(window, text="Issue Book", bg="black", fg="white", command=issueBook)
button4.place(relx=0.2, rely=0.45, relwidth=0.6, relheight=0.1)

button5 = Button(window, text="Return Book", bg="black", fg="white", command=returnBook)
button5.place(relx=0.2, rely=0.55, relwidth=0.6, relheight=0.1)

button6 = Button(window, text="Search Book", bg="black", fg="white", command=search)
button6.place(relx=0.2, rely=0.65, relwidth=0.6, relheight=0.1)

button7 = Button(window, text="Show Issue/Return Log", bg="black", fg="white", command=Show_Log)
button7.place(relx=0.2, rely=0.75, relwidth=0.6, relheight=0.1)

window.mainloop()
