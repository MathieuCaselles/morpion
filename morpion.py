from tkinter import *

fenetre = Tk()
fenetre.title("Test")

def test(i, j):
    print(i, ' ' ,j)

for i in range (3):
    for j in range (3):
        A = lambda i= i, j=j: test(i, j)
        btn_test = Button(fenetre, text="test", command=test(i, j), width = 7, height = 3)
        btn_test.grid(row = i, column = j)

fenetre.mainloop()
