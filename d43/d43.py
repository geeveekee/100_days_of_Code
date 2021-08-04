"""
--------------------------
BookStore Databse App
Author: Gayatri
Date:4/08/2021
--------------------------
User can do the following:

View all records
Search an entry
Add entry
Update entry
Delete 
Close
"""

from tkinter import *
import backend

#functions
def clear_input_fields():
    title_ip.delete(0, END)
    author_ip.delete(0, END)
    year_ip.delete(0, END)
    isbn_ip.delete(0, END)

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple = list1.get(index)
    print(selected_tuple)
    clear_input_fields()
    title_ip.insert(END, selected_tuple[1])
    author_ip.insert(END, selected_tuple[2])
    year_ip.insert(END, selected_tuple[3])
    isbn_ip.insert(END, selected_tuple[4])

def del_cmd():
    backend.delete(selected_tuple[0])

def view_cmd():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def search_cmd():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)
    clear_input_fields()

def add_cmd():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    clear_input_fields()

def update_cmd():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    print(selected_tuple)
    

root = Tk()
root.title("BookStore")

#Creating the labels
title_label = Label(root, text="Title").grid(row=0, column=0)
year_label = Label(root, text="Year").grid(row=1, column=0)
author_label = Label(root, text="Author").grid(row=0, column=2)
isbn_label = Label(root, text="ISBN").grid(row=1, column=2)

#Creating the entry boxes
title_text = StringVar()
title_ip = Entry(root, textvariable=title_text)
title_ip.grid(row=0, column=1)

year_text = StringVar()
year_ip = Entry(root, textvariable=year_text)
year_ip.grid(row=1, column=1)

author_text = StringVar()
author_ip = Entry(root, textvariable=author_text)
author_ip.grid(row=0, column=3)

isbn_text = StringVar()
isbn_ip = Entry(root, textvariable=isbn_text)
isbn_ip.grid(row=1, column=3)


#The main display (listbox)
list1 = Listbox(root, height=6, width=35)
list1.grid(row=2, column=0, columnspan=2, rowspan=6)

sb1 = Scrollbar(root)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

#User Buttons
view_btn = Button(root, width=12, text="View All", command=view_cmd)
view_btn.grid(row=2, column=3)
  
search_btn = Button(root, width=12, text="Search Entry", command=search_cmd)
search_btn.grid(row=3, column=3)
  
add_btn = Button(root, width=12, text="Add Entry", command=add_cmd)
add_btn.grid(row=4, column=3)
  
update_btn = Button(root, width=12, text="Update", command=update_cmd)
update_btn.grid(row=5, column=3)
  
delete_btn = Button(root, width=12, text="Delete", command=del_cmd)
delete_btn.grid(row=6, column=3)
  
close_btn = Button(root, width=12, text="Close", command=root.destroy)
close_btn.grid(row=7, column=3)
  


root.mainloop()