from Botao_padrao import *
import customtkinter as ctk

class Botao(Botao_padrao):
    def __init__(self, master, text, padx, pady, command, fill="x", expand=True, width=150, height=40, fg_color="blue", side="left"):
        super().__init__(master, text, width, height, fg_color, side, padx, pady, fill, expand, command)
              
    def cria_botao(self):
        botao = ctk.CTkButton(master=self.master, text=self.text, width=self.width, height=self.height,fg_color=self.fg_color, command=self.command)
        botao.pack(side=self.side, padx=self.padx, pady=self.pady, fill=self.fill, expand=self.expand)
        
        return botao
    
    