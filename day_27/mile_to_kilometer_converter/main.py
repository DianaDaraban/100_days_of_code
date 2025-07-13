import tkinter

window = tkinter.Tk()
# window.minsize(width=250, height=150)
window.title('Mile to Km Converter')
window.config(padx=20,pady=20)

equal_label = tkinter.Label(text='is equal to')
equal_label.grid(column=0, row=1)

input_mile = tkinter.Entry(width=7)
input_mile.grid(column=1, row=0)

miles_label = tkinter.Label(text='miles')
miles_label.grid(column=2, row=0)

result_label = tkinter.Label(text=0)
result_label.grid(column=1, row=1)

km_label = tkinter.Label(text='km')
km_label.grid(column=1, row=2)

def convert():
    result_label.config(text=round(int(input_mile.get()) * 1.60934))

button = tkinter.Button(text='Calculate', command=convert)
button.grid(column=1, row=2)









window.mainloop()