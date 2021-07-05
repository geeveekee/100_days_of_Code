from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.geometry('300x150')
window.configure(bg='#FB7AFC', padx=30, pady=20)


def convert():
    mile = my_input.get()
    mile = float(mile)
    km = mile * 1.6093
    print(km)
    answer.configure(text=km)



my_input = Entry()
miles = Label(text='Miles', bg='#FB7AFC')
is_equal_to = Label(text="is equal to", bg='#FB7AFC')
answer = Label(text='0', bg='#FBC7F7')
km = Label(text='Km', bg='#FB7AFC')
my_btn = Button(text='Calculate', bg='#78DEC7', command=convert)





is_equal_to.grid(row=1, column=1)
my_input.grid(row=0, column=2, pady=5)
miles.grid(row=0, column=3)
answer.grid(row=1, column=2)
km.grid(row=1, column=3)
my_btn.grid(row=2, column=2, pady=10)












window.mainloop()