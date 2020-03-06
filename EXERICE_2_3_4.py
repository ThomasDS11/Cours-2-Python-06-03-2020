# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
"""
EXERCICE 2
"""

"""
fichier = open("C:\\Users\\jlalv\\OneDrive\\Bureau\\exercice.py","a")
fichier.write("bonjour monde")
fichier.close()
fichier = open("C:\\Users\\jlalv\\OneDrive\\Bureau\\exercice.py","r")
fichier.read()
fichier.close()
"""

"""
exercice 3 et 4
"""
def lire():
    fichier = open("C:\\Users\\jlalv\\OneDrive\\Bureau\\exercice.py","r")
    print (fichier.read())
    fichier.close()
  
def ecrire():
    fichier = open("C:\\Users\\jlalv\\OneDrive\\Bureau\\exercice.py","a")
    fichier.write("bonjour monde")
    fichier.close()
    
__name__ == "__main__"

lire()
ecrire()