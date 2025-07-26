import json
from tkinter import *
from tkinter import messagebox
import random
from generator import letters, numbers, symbols, nr_letters, nr_symbols, nr_numbers
import pyperclip

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

def add_data():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website:{
            'email': email,
            'password':password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Ooops', message='Please do not leave any fields empty!')
    else:
        try:
            with open('data.json', 'r') as f:
                # Reading old data
                data = json.load(f)
        except FileNotFoundError:
            with open('data.json', 'w') as f:
                json.dump(new_data, f,indent=4)
        else:
                # Updating old data with new data
            data.update(new_data)

            with open('data.json', 'w')     as f:
                json.dump(data, f,indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

def search():
    website_searched = entry_website.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found')
    else:
        if data[website_searched]:
            messagebox.showinfo(f'{website_searched}',
                                f'Email: {data[website_searched]['email']}\nPassword: {data[website_searched]['password']}')
        else:
            messagebox.showinfo(f'{website_searched}', 'There is no such website stored.')

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text='Website')
label_website.grid(column=0, row=1 , sticky='e')

entry_website = Entry(width=21)
entry_website.grid(column=1, row=1, sticky='e')
entry_website.focus()

btn_website = Button(width=14, text='Search', command=search)
btn_website.grid(column=2, row=1, sticky='w')

label_email = Label(text='Email/Username')
label_email.grid(column=0, row=2 , sticky='e')


entry_email = Entry(width=39)
entry_email.grid(column=1, row=2, columnspan=2 , sticky='e')
entry_email.insert(END, 'name@sample.com')

label_password = Label(text='Password')
label_password.grid(column=0, row=3 , sticky='e')

entry_password = Entry(width=21)
entry_password.grid(column=1, row=3 , sticky='e')


btn_password = Button(text='Generate Password', command=generate_password)
btn_password.grid(column=2, row=3 , sticky='w')

btn_add = Button(width=33, text='Add', command=add_data)
btn_add.grid(column=1, row=4, columnspan=2 , sticky='e')

window.mainloop()