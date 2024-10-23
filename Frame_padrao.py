from abc import ABC, abstractmethod
import customtkinter as ctk

class Frame(ABC):
    def __init__(self, master, fg_color, height, relx, rely, relwidth, relheight):
        self.__master = master
        self.__fg_color = fg_color
        self.__height = height
        self.__relx = relx
        self.__rely = rely
        self.__relwidth = relwidth
        self.__relheight = relheight
        
    @property
    def master(self):
        return self.__master
    
    @master.setter
    def master(self,valor):
        self.__master = valor
    
    @property
    def fg_color(self):
        return self.__fg_color

    @fg_color.setter        
    def fg_color(self, valor):
        self.__fg_color = valor  
     
    @property
    def height(self):
        return self.__height

    @height.setter        
    def height(self, valor):
        self.__height = valor

    @property
    def relx(self):
        return self.__relx

    @relx.setter        
    def relx(self, valor):
        self.__relx = valor

    @property
    def rely(self):
        return self.__rely

    @rely.setter        
    def rely(self, valor):
        self.__rely = valor

    @property
    def relwidth(self):
        return self.__relwidth

    @relwidth.setter        
    def relwidth(self, valor):
        self.__relwidth = valor

    @property
    def relheight(self):
        return self.__relheight

    @relheight.setter        
    def relheight(self, valor):
        self.__relheight = valor

    
    @abstractmethod        
    def cria_frame(self):
          pass 