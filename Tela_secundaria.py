import customtkinter as ctk
from tela_secundaria_padrao import *

class Tela_secundaria(Tela_sec_padrao):
    def __init__(self, master, geometry, title):
        super().__init__(master, geometry, title)
        
        
    def cria_tela_secundaria(self):
        tela = ctk.CTkToplevel(master=self.master)
        tela.geometry(self.geometry)
        tela.attributes("-topmost", True)
        tela.title(self.title)
        tela.focus()
        tela.after(500, lambda: tela.attributes("-topmost", False))
        tela.minsize(width=450, height=350)
        return tela
    
    
       