from tkinter import *

fenetre = Tk()
fenetre.title("Test")
boutons = ["test"]*9
ordre = ['00', '01', '02', '10', '11', '12', '20', '21', '22']

def tour_joueur(marquage):
    if marquage == 'x':
        marquage = 'o'
    else:
        marquage = 'x'
        return marquage

def test(ligne, colonne):
    marquage = 'x'

    boutons[ordre.index(str(colonne) + str(ligne))].config(text = 'x')
    print(str(ligne) + str(colonne) + '   ' + marquage)


for ligne in range (3):
    for colonne in range (3):
        compteur = 0
        A = lambda colonne = colonne, ligne = ligne: test(ligne, colonne)
        boutons[ordre.index(str(colonne) + str(ligne))] = Button(fenetre, text="test", command= A, width = 7, height = 3)
        boutons[ordre.index(str(colonne) + str(ligne))].grid(row = ligne, column = colonne)
        compteur += 1

fenetre.mainloop()
