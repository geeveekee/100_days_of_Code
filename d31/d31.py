from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')


def forward(img_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[img_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(img_number+1))
    button_back = Button(root, text="<<",command= lambda: back(img_number-1))

    if img_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text=f"Image {img_number} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, columnspan=3, column=0, sticky=W+E)

    

def back(img_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[img_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(img_number+1))
    button_back = Button(root, text="<<",command= lambda: back(img_number-1))

    if img_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text=f"Image {img_number} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, columnspan=3, column=0, sticky=W+E)




#Loading the images 
my_img1 = ImageTk.PhotoImage(Image.open('100_days_of_Code\d31\images\img1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('100_days_of_Code\d31\images\img2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('100_days_of_Code\d31\images\img3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('100_days_of_Code\d31\images\img4.png'))
my_img5 = ImageTk.PhotoImage(Image.open('100_days_of_Code\d31\images\img5.jpg'))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text=f"Image 1 of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
#Saving the images
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


button_back = Button(root, text="<<",command=back, state=DISABLED)
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, columnspan=3, column=0, sticky=W+E)







root.mainloop()