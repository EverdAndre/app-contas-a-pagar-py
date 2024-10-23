from Frame_padrao import *

class Frames(Frame):
    def __init__(self, master, fg_color, height, relx, rely, relwidth, relheight):
        super().__init__(master, fg_color, height, relx, rely, relwidth, relheight)
        
        
    def cria_frame(self):
        frame = ctk.CTkFrame(master= self.master, fg_color=self.fg_color, height=self.height)
        frame.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)
        
        return frame  
    
      