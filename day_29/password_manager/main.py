from tkinter import *
from tkinter import messagebox
import random
from generator import letters, numbers, symbols, nr_letters, nr_symbols, nr_numbers
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))
    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)
    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Ooops', message='Please do not leave any fields empty!')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \n Email:{email}\nPassword: {password} \nIs it ok to save?')

        if is_ok:
            with open('data.txt', 'a') as f:
                f.write(f'{website} |  {email} | {password} \n' )
                entry_website.delete(0, END)
                entry_password.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text='Website')
label_website.grid(column=0, row=1)

entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()

label_email = Label(text='Email/Username')
label_email.grid(column=0, row=2)


entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(END, 'name@sample.com')

label_password = Label(text='Password')
label_password.grid(column=0, row=3)

entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)


btn_password = Button(text='Generate Password', command=generate_password)
btn_password.grid(column=2, row=3)

btn_add = Button(width=36, text='Add', command=add_data)
btn_add.grid(column=1, row=4, columnspan=2)

window.mainloop()