# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:05:29 2020

@author: jlalv
"""

class animal :
      def __init__(self,nombre,regime_alimentaire,quantité_nourriture):
          self.nombre = nombre
          self.regime_alimentaire = regime_alimentaire
          self.quantité_nourriture = quantité_nourriture
          
class Mammifere(animal) :
    
   def __init__(self,nombre,regime_alimentaire,quantité_nourriture,nombre_pattes ):
        super().__init__(nombre,regime_alimentaire,quantité_nourriture)
        self.nombre_pattes = nombre_pattes
        
   def __str__(self):
       return ", Cette animal est stocké en quantité de  " + str(self.nombre) + ", il est " + self.regime_alimentaire + ", il consomme" + str(self.quantité_nourriture) +" et il a " +str(self.nombre_pattes)+ " pattes"

       
class Domestique(animal) :
            
    def __init__(self,nombre,regime_alimentaire,quantité_nourriture,nombre_pattes ):
         super().__init__(nombre,regime_alimentaire,quantité_nourriture)
         self.nombre_pattes = nombre_pattes
         
    def __str__(self):
       return ", Cette animal est stocké en quantité de  " + str(self.nombre) + ", il est " + self.regime_alimentaire + ", il consomme" + str(self.quantité_nourriture) +" et il a " +str(self.nombre_pattes)+ " pattes"
              
class Animal_marin(animal) :
               
     def __init__(self,nombre,regime_alimentaire,quantité_nourriture,nombre_pattes = 0):
         super().__init__(nombre,regime_alimentaire,quantité_nourriture)
         self.nombre_pattes = 0
         
     def __str__(self):
       return ", Cette animal est stocké en quantité de  " + str(self.nombre) + ", il est " + self.regime_alimentaire + ", il consomme" + str(self.quantité_nourriture) +" et il a " +str(self.nombre_pattes)+ " pattes"
        
if __name__ == "__main__":
    zoo = {}
    zoo["humain"] = Mammifere(2,'omnivore',600,2)
    zoo["lion"] = Mammifere(1,'carnivore',3,4)
    zoo["lapin"] = Domestique(7,'vegetarien',100,4)
    zoo["mouton"] = Domestique(5,'vegetarien',500,4)
    zoo["chien"] = Domestique(2,'omnivore',500,4)
    zoo["pieuvre"] = Animal_marin(1,'carnivore',200)
    zoo["serpent"] = animal(2,'carnivore',200)
    zoo["autruche"] = animal(4,'omnivore',1)
    zoo["poule"] = Mammifere(8,'omnivore',200,2)
    
    for clef in zoo:
        print (clef+""+str(zoo[clef]))