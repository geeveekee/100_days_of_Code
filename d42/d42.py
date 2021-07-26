import textwrap
from tkinter import *
from numpy import imag
import pandas as pd
from icecream import ic
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
my_data = {}

try:
    french_word = pd.read_csv('100_days_of_Code\d42\data\/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('100_days_of_Code\d42\data\/french_words.csv')
    df = pd.DataFrame(data=original_data)
    my_data = df.to_dict('records')
else:
    df = pd.DataFrame(data=french_word)
    my_data = df.to_dict('records')


def generate_new_word():
    global current_card, flip_timer
    root.after_cancel(flip_timer)
    current_card = random.choice(my_data)
    flash_card.itemconfig(my_title, text='French', fill='black')
    flash_card.itemconfig(my_word, text=current_card['French'], fill='black')
    flash_card.itemconfig(canvas_img, image=card_front_img)
    flip_timer = root.after(3000, func=flip_card)

def flip_card():
    flash_card.itemconfig(my_title, text='English', fill='white')
    flash_card.itemconfig(my_word, text=current_card['English'], fill="white")
    flash_card.itemconfig(canvas_img, image=card_back_img)

def is_known():
    my_data.remove(current_card)

    learnt_data = pd.DataFrame(my_data)
    learnt_data.to_csv('100_days_of_Code\d42\data\/words_to_learn.csv', index=False)

    generate_new_word()

root = Tk()
root.title = ("Flasshy")
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = root.after(3000, func=flip_card)


flash_card = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='100_days_of_Code\d42\images\card_front.png')
card_back_img = PhotoImage(file='100_days_of_Code\d42\images\card_back.png')

canvas_img = flash_card.create_image(400, 263, image=card_front_img)
flash_card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
my_title = flash_card.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
my_word = flash_card.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
flash_card.grid(row=0, columnspan=2, column=0)

cross_img = PhotoImage(file='100_days_of_Code\d42\images\wrong.png')
unknown_btn = Button(image=cross_img, highlightthickness=0, command=generate_new_word)
unknown_btn.grid(row=1, column=0)

check_img = PhotoImage(file='100_days_of_Code\d42\images\/right.png')
known_btn = Button(image=check_img, highlightthickness=0, command=is_known)
known_btn.grid(row=1, column=1)


generate_new_word()


root.mainloop()