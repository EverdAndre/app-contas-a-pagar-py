from Label_padrao import *
import customtkinter as ctk
class Label(Label_padrao):
    def __init__(self, master, text, height=40, fg_color="transparent",
                 text_color='white', font= ("Arial bold", 16), 
                 border_color="white", border_width=1):
        super().__init__(master, text, height, fg_color, text_color, font, border_color, border_width)
        
    def cria_label(self):
        label = ctk.CTkButton(master=self.master, text=self.text, 
                              height=self.height, fg_color=self.fg_color, text_color=self.text_color,
                              font=self.font,border_color=self.border_color,
                              border_width=self.border_width)
        label.configure(hover=False)
        return label