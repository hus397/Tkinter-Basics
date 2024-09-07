import tkinter

screen = tkinter.Tk()
screen.geometry('800x600')
screen.title('Hello World')

label = tkinter.Label(screen, text = 'hi', fg = 'green', bg = 'yellow')
label.place(x=20,y=300)
label2 = tkinter.Label(screen, text = 'hii')
label2.place(x=200,y=3)

button = tkinter.Button(screen, text = 'click me')
button.place(x=200,y=200)

entry = tkinter.Entry(screen)
entry.pack()

listbox = tkinter.Listbox(screen)
listbox.insert(0,'hello')
listbox.pack()

#geometry managers function to place widgets on the screen
screen.mainloop()
