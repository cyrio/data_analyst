#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 10:28:14 2023

@author: cyrilleedzang
"""

class Convertisseur:
    """ 
        Convertisseur de devise 
        
        functions : 
            convertir : effectue bla conversion d'un montant dans la devise demandé'
    
    """
    def __init__(self,devise1,devise2,taux):
        self.devise1 = devise1
        self.devise2 = devise2
        self.taux = taux
        
    def __str__(self):
        return f"Convertisseur de devise {self.devise1} vers {self.devise2} au taux de {self.taux}"
    
    def __repr__(self):
        
        return f"{self.__class__.__name__}(\"{self.devise1}\",\"{self.devise2}\",{self.taux})"
    
    def convertir(self,montant):
        return montant * self.taux
    
def main():
    monconvertisseur = Convertisseur("EUR", "USD", 1.12)
    print(monconvertisseur)
    print(repr(monconvertisseur))
    print(monconvertisseur.convertir(100))
    
if __name__ == '__main__':
    main()
    