import tkinter

window = tkinter.Tk()

window.title('My first GUI program')
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.grid(column=1, row=1)
my_label['text'] = 'New text'





def button_clicked():
    my_label.config(text=input_item.get())

# Entry component
input_item = tkinter.Entry(width=10)
input_item.grid(column=4, row=3)
# Button
button = tkinter.Button(text='click me', command=button_clicked)
button.grid(column=2, row=2)

button = tkinter.Button(text='click me', command=button_clicked)
button.grid(column=3, row=1)








window.mainloop()