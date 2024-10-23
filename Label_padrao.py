from abc import ABC, abstractmethod

class Label_padrao(ABC):
    def __init__(self, master, text, height, fg_color, text_color, font, border_color, border_width):
        self.__master = master
        self.__text = text
        self.__height = height
        self.__fg_color = fg_color
        self.__text_color = text_color
        self.__font = font
        self.__border_color = border_color
        self.__border_width = border_width
        
        
    @property
    def master(self):
        return self.__master
    @master.setter
    def master(self, valor):
        self.__master = valor
    
    @property
    def text(self):
        return self.__text
    @text.setter
    def text(self, valor):
        self.__text = valor
        
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, valor):
        self.__height = valor
        
    @property
    def fg_color(self):
        return self.__fg_color
    @fg_color.setter
    def fg_color(self, valor):
        self.__fg_color = valor
        
    @property
    def text_color(self):
        return self.__text_color
    @text_color.setter
    def text_color(self, valor):
        self.__text_color = valor
        
    @property
    def font(self):
        return self.__font
    @font.setter
    def font(self, valor):
        self.__font = valor
        
    @property
    def border_color(self):
        return self.__border_color
    @border_color.setter
    def border_color(self, valor):
        self.__border_color = valor
        
    @property
    def border_width(self):
        return self.__border_width
    @border_width.setter
    def border_width(self, valor):
        self.__border_width = valor
        
    
        
    @abstractmethod
    def cria_label(self):
        return