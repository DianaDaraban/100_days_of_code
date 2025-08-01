import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card={}

try:
    data_csv = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data =  pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn=data_csv.to_dict(orient='records')



def random_french_words():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=f'{current_card['French']}', fill='black')
    canvas.itemconfig(card_background, image=image_card)
    flip_timer = window.after(3000, func=flip_card)



def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=f'{current_card['English']}', fill='white')
    canvas.itemconfig(card_background, image=image_back_card)


def is_known():
    to_learn.remove(current_card)
    csv = pandas.DataFrame(to_learn)
    csv.to_csv('words_to_learn.csv', index=False)
    random_french_words()

window = Tk()
window.title('Flash Cards Dictionary')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
image_card = PhotoImage(file='images/card_front.png')
image_back_card = PhotoImage(file='images/card_back.png')
image_cancel = PhotoImage(file='images/wrong.png')
image_confirm = PhotoImage(file='images/right.png')
card_background = canvas.create_image(400, 263, image=image_card)
card_title = canvas.create_text(400,150,text='Title', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400,263,text='Words', font=('Ariel', 60, 'bold'))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

button_cancel = Button(image=image_cancel, highlightthickness=0, command=random_french_words)
button_cancel.grid(row=1, column=0)
button_confirm = Button(image=image_confirm, highlightthickness=0, command=is_known)
button_confirm.grid(row=1, column=1)
random_french_words()







window.mainloop()

