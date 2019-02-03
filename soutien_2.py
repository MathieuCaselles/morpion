from tkinter import *

fenetre = Tk()
fenetre.title("Bidule")

dimensions = 800
dimensions_carré = 20

canevas = Canvas(fenetre, width=dimensions, height=dimensions, bg="black")
canevas.pack()


carre = canevas.create_rectangle(dimensions / 2 - dimensions_carré, dimensions - 60 / 2 - dimensions_carré, dimensions / 2 + dimensions_carré, dimensions - 60 / 2 + dimensions_carré, fill="white")


def bouger_carre_left(event):
    vitesse = -10
    canevas.move(carre, vitesse, 0)

def bouger_carre_right(event):
    vitesse = 10
    canevas.move(carre, vitesse, 0)

fenetre.bind("<Left>", bouger_carre_left)
fenetre.bind("<Right>", bouger_carre_right)

obstacles = []

def deplacement_obstacle():
    for obstacle in obstacles:
        canevas.move(obstacle, 0, 10)
    canevas.after(20, deplacement_obstacle)


def spawn_obstacle():
    obstacles.append(canevas.create_rectangle(dimensions / 2 - dimensions_carré, 0 - dimensions_carré, dimensions / 2 + dimensions_carré, 0 + dimensions_carré, fill="white"))
    canevas.after(200, spawn_obstacle)






spawn_obstacle()
deplacement_obstacle()
fenetre.mainloop()