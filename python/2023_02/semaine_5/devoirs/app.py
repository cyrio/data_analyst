#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 21:37:08 2023

@author: cyrilleedzang
"""
from imcmodel import ImcModel
from imcview import ImcView
from imccontroller import ImcController
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title('IMC - Formulaire de Calcul')
        
        model = ImcModel(0,0)
        
        vue = ImcView(self)
        vue.grid(row=0, column=0, padx=20, pady=20)
        
        controller = ImcController(model, vue)

        vue.set_controller(controller)

if __name__ == '__main__':
    app = App()
    app.mainloop()        
        