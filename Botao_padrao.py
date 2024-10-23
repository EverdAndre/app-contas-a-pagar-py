from abc import ABC, abstractmethod

class Botao_padrao(ABC):
    def __init__(self,master, text, width, height, fg_color, side, padx, pady, fill, expand, command):
        self.__master = master
        self.__text = text
        self.__width = width
        self.__height = height
        self.__fg_color = fg_color
        self.__side = side
        self.__padx = padx
        self.__pady = pady
        self.__fill = fill
        self.__expand = expand
        self.__command = command
       
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
    def width(self):
        return self.__width
        
    @width.setter
    def width(self, valor):
        self.__width = valor
        
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
    def side(self):
        return self.__side
        
    @side.setter
    def side(self, valor):
        self.__side = valor
        
    @property
    def padx(self):
        return self.__padx
        
    @padx.setter
    def padx(self, valor):
        self.__padx = valor
        
    @property
    def pady(self):
        return self.__pady
        
    @pady.setter
    def pady(self, valor):
        self.__pady = valor
        
    @property
    def fill(self):
        return self.__fill
        
    @fill.setter
    def fill(self, valor):
        self.__fill = valor
        
    @property
    def expand(self):
        return self.__expand
        
    @expand.setter
    def expand(self, valor):
        self.__expand = valor
        
    @property
    def command(self):
        return self.__command
    
    @command.setter
    def command(self, valor):
        self.__command = valor
 
@abstractmethod        
def cria_botao(self):
    return     
     