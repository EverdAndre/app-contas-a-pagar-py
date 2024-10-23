from Botoes import *
from Frames import *
from Tela_secundaria import *
from Label import *
class App(ctk.CTk):        
     def __init__(self):   # contrutor da subclasse
          super().__init__()     # contrutor da classe pai
          ctk.set_appearance_mode("dark")
          self.title("Contas a Pagar")
          self.geometry("1000x500")
          self.minsize(width=450, height=350)
          # Frames
          self.frame_branco = Frames(self,"white", 630, 0.002, 0.01, 0.997, 0.988)
          self.frame = self.frame_branco.cria_frame()
          
          self.frame_botoes = Frames(self.frame, "black", 0, 0.004, 0.01, 0.991, 0.1)
          self.frame_btn = self.frame_botoes.cria_frame()
          
          self.frame_cinza = Frames(self.frame,"gray", 0, 0.006, 0.115, 0.987, 0.875)
          self.frame = self.frame_cinza.cria_frame()
          
          # Botões 
          self.botao_nova = Botao(self.frame_btn,"Cadastrar Nova", 10, 10, self.abre_tela02)
          self.btn_nova = self.botao_nova.cria_botao()
          
          self.botao_todas = Botao(self.frame_btn,"Listar Todas", 0, 10, None)
          self.btn_todas = self.botao_todas.cria_botao()
          
          self.botao_contas_dia = Botao(self.frame_btn,"Contas de Hoje", 10, 10, None)
          self.btn_contas_dia = self.botao_contas_dia.cria_botao()
          
          self.botao_vencer = Botao(self.frame_btn,"Contas a Vencer", 10, 10, None)
          self.btn_vencer = self.botao_vencer.cria_botao()
          
          self.botao_vencidas = Botao(self.frame_btn,"Contas Vencidas", 10, 10, None)
          self.btn_vencidas = self.botao_vencidas.cria_botao()
          
          self.botao_config = Botao(self.frame_btn,"Configurações", 10, 10, None)
          self.btn_config = self.botao_config.cria_botao()
        # Tela 02  
     def abre_tela02(self):
          tela02 = Tela_secundaria(self,"1000x500", "Nova Conta")
          nova_tela = tela02.cria_tela_secundaria()
          self.frame_branco = Frames(nova_tela,"white", 630, 0.002, 0.01, 0.997, 0.988)
          self.frame = self.frame_branco.cria_frame()
          # Botões de Opção
          self.frame_botoes = Frames(self.frame, "black", 0, 0.004, 0.01, 0.991, 0.1)
          self.frame_btn = self.frame_botoes.cria_frame()
          
          self.btn_salvar = Botao(self.frame_btn,"Salvar", 10, 10, None)
          self.btn_nova = self.btn_salvar.cria_botao()
          
          self.btn_Imprimir = Botao(self.frame_btn,"Imprimir", 10, 10, None)
          self.btn_imprimir = self.btn_Imprimir.cria_botao()
          
          self.btn_todas = Botao(self.frame_btn,"Listar Todas", 10, 10, None)
          self.btn_todas = self.btn_todas.cria_botao()
          
          # Tela de cadastro de contas
          self.frame_cinza = Frames(self.frame,"gray", 0, 0.006, 0.115, 0.987, 0.875)
          self.frame_cinza = self.frame_cinza.cria_frame()
          
          self.frame_botoes = Frames(self.frame_cinza, "transparent", 0, 0.004, 0.01, 0.991, 0.1)
          self.frame_btn = self.frame_botoes.cria_frame()
           
          self.id_conta = Label(self.frame_btn, "Id da Conta")
          self.label_1 = self.id_conta.cria_label()
          self.label_1.place(relx=0.0035, rely=0.1, relwidth=0.1, relheight=0.8)
          
          
    
          
          
          