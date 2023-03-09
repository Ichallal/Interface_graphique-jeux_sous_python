import tkinter as CTk
import datetime
import platform
import os
import random

# Générer un nombre aléatoire entre 0 et 50
nombre = random.randint(0, 50)

# Créer une classe pour la fenêtre personnalisée
class CustomWindow(CTk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Créer un label pour afficher la date et l'heure actuelles
        aujourdhui = datetime.datetime.now()
        self.aujourdhui = CTk.Label(self, text="Date et heure actuelles : " + str(aujourdhui))
        self.aujourdhui.pack()

        # Créer des labels pour afficher les informations système
        self.system = CTk.Label(self, text="Système d'exploitation : " + platform.system())
        self.system.pack()

        self.version = CTk.Label(self, text="Version de Python : " + platform.python_version())
        self.version.pack()

        # Créer un champ de saisie pour deviner le nombre
        self.input = CTk.Entry(self)
        self.input.pack()

        # Créer un bouton pour soumettre la saisie
        self.button = CTk.Button(self, text="Soumettre", command=self.submit)
        self.button.pack()

        # Créer un label pour afficher le résultat de la saisie
        self.output = CTk.Label(self, text="")
        self.output.pack()

    def submit(self):
        # Récupérer la valeur saisie dans le champ de saisie
        value = int(self.input.get())
        # Vérifier si la valeur saisie est égale à la valeur aléatoire
        if value == nombre:
            message = "Bravo, vous avez deviné le nombre !"
        else:
            message = "Dommage, le nombre à deviner était {}".format(nombre)

        # Afficher le message dans le label
        self.output.config(text=message)

# Créer une instance de la classe CustomWindow
root = CTk.Tk()
app = CustomWindow(master=root)
app.mainloop()
