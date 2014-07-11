from math import pow
# -*- coding: utf-8 -*-
x = 5
y = 4

bienvenue = raw_input("Bienvenue dans le calculateur de puissances ! Appuie sur Entrée.")

def pow():
    x = int(raw_input("Entre la base : "))
    y = int(raw_input("Entre l\'exposant : "))
    resultat = x**y
    print "%s à la puissance %s vaut %s." % (x, y, resultat)

pow()