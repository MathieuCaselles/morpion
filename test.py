from tkinter import *
 
liste = ["var"]*11
 
def changetext():
    for i in range(len(liste)):
        liste[i].config(text="NewBou")
 
fen = Tk()
can = Canvas(fen)
can.pack()
for i in range(len(liste)):
    liste[i] = Button(fen,text="var",command = changetext)
    liste[i].pack()
 
fen.mainloop()