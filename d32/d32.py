from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from icecream import ic
from password_generator import generating_random_password
import pyperclip
root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_rand_pass():
    password_input.delete(0, END)
    rand_password = generating_random_password()
    password_input.insert(0, rand_password)
    pyperclip.copy(rand_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def sav_data():
    website_name = web_input.get()
    email_id = email_input.get()
    password_set = password_input.get()

    if len(website_name) == 0 or len(password_set) == 0:
        messagebox.showinfo(title="oops", message="Please make sure none of the fields are left empty!")

    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered: \nEmail: {email_id}\nPassword: {password_set}\n is it ok to save?")

        if is_ok:
            with open('100_days_of_Code\d32\my_data.txt', 'a') as file:
                file.write(f"{website_name} | {email_id} | {password_set} \n")
                web_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas(root, height=200, width=200)
img = ImageTk.PhotoImage(Image.open('100_days_of_Code\d32\logo.png'))
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website = Label(text='Website: ').grid(row=1, column=0)
email = Label(text='Email/Username: ').grid(row=2, column=0)
password = Label(text='Password: ').grid(row=3, column=0)

web_input = Entry(width=50)
web_input.grid(row=1, column=1, columnspan=2)
web_input.focus()

email_input = Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, 'xyz@gmail.com')

password_input = Entry(width=32)
password_input.grid(row=3, column=1)

generate_pass_btn = Button(text='Generate Password', command=generate_rand_pass)
generate_pass_btn.grid(row=3, column=2)

add_btn = Button(text='Add', width=42, command=sav_data)
add_btn.grid(row=4, column=1, columnspan=2)



root.mainloop()