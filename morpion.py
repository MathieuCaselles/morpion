from tkinter import *

fenetre = Tk()
fenetre.title("Test")

def test():
    print('Hello World')

btn_test = Button(fenetre, text="test", command=test)
btn_test.pack()

fenetre.mainloop()