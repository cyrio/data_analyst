#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 14:22:30 2023

@author: cyrilleedzang
"""
import re
import time

class ImcModel:
    
    ERROR_FORMAT =" nombre de caractere maximum 3 :"
    ERROR__TYPE ="Erreur ! c' est un entier :"
    
    def __init__(self,poids,taille):
        self.set_poids(poids)
        self.set_taille(taille)
    
    def get_poids(self) :
        """
            retourne le poids
            :param : 
            :return :
        """
        return self.__poids
    
    def set_poids(self, unpoids:int):
        """
            valide un poids avant d'en affecter ou de modifier la valeur
            :param : unpoids
            :return :
        """
        pattern_poids = r'^[0-9]{1,3}'
        type_permis = (int,)
        if re.fullmatch(pattern_poids,str(unpoids)):
            self.__poids = unpoids
        elif type(unpoids) not in type_permis:
            raise TypeError(f'{ImcModel.ERROR_TYPE} {unpoids} ' )
        else :
            raise ValueError(f' {ImcModel.ERROR_FORMAT} {unpoids} ')
            
    def get_taille(self):
        """
            retourne la taille
            :param : 
            :return :
        """
        return self.__taille
    
    def set_taille(self,unetaille:int):
        """
            valide une taille avant d'en affecter ou de modifier la valeur
            :param : unetaille
            :return :
        """
        pattern_taille = r'^[0-9]{1,3}'
        type_permis = (int,)
        if re.fullmatch(pattern_taille,str(unetaille)):
            self.__taille = unetaille
        elif type(unetaille) not in type_permis:
            raise TypeError(f'{ImcModel.ERROR_TYPE} {unetaille}' )
        else :
            raise ValueError(f'{ImcModel.ERROR_FORMAT} {unetaille}')
        
    poids = property(get_poids, set_poids)
    taille = property(get_taille, set_taille)
    
    def calculer(self):
        """
            effectue le calcul de l'imc'
            :param :
            :return :
        """
        return self.poids/(self.taille**2)
    
    def sauvegarder(self):
        """
            je sauvegarde les valeurs entrées dans un fichier
            :param :
            :return :
        """
        with open('imc.txt', 'a') as f:
            f.write(f" date: {time.ctime(time.time())} -  poids : {self.poids} - taille : {self.taille}  \n")