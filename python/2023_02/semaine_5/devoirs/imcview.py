#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 16:24:56 2023

@author: cyrilleedzang
"""
import tkinter as tk
from tkinter import ttk

class ImcView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #creation de widget
        # label poids
        self.poids_label = ttk.Label(self, text = "Poids kg")
        self.poids_label.grid(row=1, column=0)
        
        #poids
        self.poids_var = tk.StringVar()
        self.poids_saisie = ttk.Entry(self, textvariable=self.poids_var, width=15)
        self.poids_saisie.grid(row=1, column=1, sticky=tk.NSEW) # ou NUMERIC
        
        #label message pour le poids
        self.message_poids_label = ttk.Label(self, text='', foreground='red')
        self.message_poids_label.grid(row=2, column=1, sticky=tk.W)
        
        #label taille
        self.taille_label = ttk.Label(self, text = "Taille cm")
        self.taille_label.grid(row=3, column=0)
        
        #taille
        self.taille_var = tk.StringVar()
        self.taille_saisie = ttk.Entry(self, textvariable=self.taille_var, width=15)
        self.taille_saisie.grid(row=3, column=1, sticky=tk.NSEW) # ou NUMERIC
        
        #label message pour la taille
        self.message_taille_label = ttk.Label(self, text='', foreground='red')
        self.message_taille_label.grid(row=4, column=1, sticky=tk.W)
        
        #label imc
        self.imc_label = ttk.Label(self, text="IMC")
        self.imc_label.grid(row=5, column=0)
        
        #label message pour la taille
        self.value_imc_label = ttk.Label(self, text='valeur', foreground='black')
        self.value_imc_label.grid(row=5, column=1, sticky=tk.W)
        
        
        #bouton calculer
        self.calculer_bouton = ttk.Button(self, text='Calculer', command= self.calculer_bouton_cliquer)
        self.calculer_bouton.grid(row=9, column=0, padx=10)
        
        #bouton quitter
        #self.quitter_bouton = ttk.Button(self, text='Quitter', command= self.destroy).pack()
        self.quitter_bouton = ttk.Button(self, text='Quitter', command= self.destroy)
        self.quitter_bouton.grid(row=11, column=0, padx=10)
        
       
        #bouton RAZ
        self.raz_bouton = ttk.Button(self, text='Quitter', command= self.raz_bouton_cliquer)
        self.raz_bouton.grid(row=13, column=0, padx=10)
        
        #controller
        self.controller = None
        
    def set_controller(self,controller):
        """
            met à jour le controller
            :param controller:
            :return :
        """
        self.controller = controller
        
    def calculer_bouton_cliquer(self):
        """
            effectue le calcul une fois le bouton cliqué
            :param : 
            :return :
        """
        if self.controller:
            self.controller.calculer(self.poids_var.get(), self.taille_var.get())
    
    
    def show_message_error(self, message):
        self.message_poids_label['text']= message
        self.message_poids_label['foreground'] = 'red'
        self.message_poids_label.after(3000,self.message_cacher)
        
        self.poids_saisie['foreground'] = 'red'
    
    def show_message_success(self, message):
        """
            Montre un message en cas de success
            :param message: 
            :return :
        """
        self.message_poids_label['text']= message
        self.message_poids_label['foreground'] = 'green'
        self.message_poids_label.after(3000,self.message_cacher)
        
        self.poids_saisie['foreground'] = 'black'
        self.poids_var.set('')
        
    def message_cacher(self):
        """
            efface les message
            :param : 
            :return :
        """
    
        self.message_poids_label['text']=''
        self.message_taille_label['text']=''
        
        
    def raz_bouton_cliquer(self):
        """
            efface le contenu du formulaire
            :param : 
            :return :
        """
        self.value_imc_label['text']='valeur'
        
        # efface les saisie
        self.taille_saisie.delete(0, 'end')
        self.poids_saisie.delete(0, 'end')
        self.poids_var.set('')
        self.taille_var.set('')
        
        
    