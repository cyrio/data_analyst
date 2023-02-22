#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 18:04:17 2023

@author: cyrilleedzang
"""
import logging

class ImcController:
    def __init__(self, model, vue):
        self.model = model
        self.vue = vue
        
    def calculer(self, unpoids, unetaille):
        """
            effectue le calcul de l'imc
        """
        try:
            self.model.poids = unpoids
            self.model.taille = unetaille
            
            # calcul de la valeur
            self.vue.value_imc_label['text'] = str(self.model.calculer())
            
            #sauvegarde
            self.model.sauvegarder()
            
            # affiche un message de success
            self.vue.show_message_success(f" {unpoids} et {unetaille} sont correctes ")
        except ValueError :
            self.vue.show_message_error(f'{self.model.ERROR_FORMAT} {unpoids} - {unetaille}')
            logging.exception(f'{self.model.ERROR_FORMAT} {unpoids} - {unetaille}')
    
        except  TypeError:
            self.vue.show_message_error(f'{self.model.ERROR_TYPE} {unpoids} - {unetaille}')
            logging.exception(f'{self.model.ERROR_TYPE} {unpoids} - {unetaille}')
            
        except IOError:
            logging.exception("ne peut lire ou sauvegarder dans le fichier de sauvegarde imc.txt")
            