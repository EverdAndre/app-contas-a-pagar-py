from abc import ABC, abstractmethod

class Tela_sec_padrao(ABC):
    def __init__(self, master, geometry, title):
        self.__master = master
        self.__geometry = geometry
        #self.__attributes = attributes
        self.__title = title
        #self.__focus = focus
        #self.__after = after

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, valor):
        self.__master = valor

    @property
    def geometry(self):
        return self.__geometry

    @geometry.setter
    def geometry(self, valor):
        self.__geometry = valor

   
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, valor):
        self.__title = valor
    
@abstractmethod       
def cria_tela_secundaria(self):
    pass
