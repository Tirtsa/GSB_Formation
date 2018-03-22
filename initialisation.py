import requetes as re
import interface as co
from tkinter import messagebox

re.initialiser() #connexion base de données
co.initialiser_connexion()
co.remplir_pages()
co.mainloop_fin()
