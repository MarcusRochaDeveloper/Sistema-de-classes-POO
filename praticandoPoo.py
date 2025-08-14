import time
import random

class Livro():
    def __init__(self, titulo, autor, nPaginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = nPaginas
        self.pagina_atual = 0

    def abrir_livro(self):
        self.pagina_atual = 1
        print(f"Livro aberto com sucesso! Página atual: {self.pagina_atual}")

    def ler_paginas(self, quantidade):
        if self.numero_paginas < quantidade:
            print("O livro não possui essa quantidade de páginas")
            return
        self.pagina_atual = quantidade

    def exibir_progresso(self):
        print("Analisando seu livro...")
        PaginasLidas = self.pagina_atual
        TotalPaginas = self.numero_paginas
        PaginasRestantes = TotalPaginas - PaginasLidas
        time.sleep(3)
        print(f"\nOlá! Analisei seu livro e descobri que ainda restam um total de {PaginasRestantes} páginas para ler")

class ContaBancaria():
    def __init__(self, titular="", saldo=0, nConta=0):
        self.titular = titular
        self.saldo = saldo
        self.numero_conta = nConta

    def userTitular(self):
        self.titular = input("Digite seu nome completo:  ")
        numeroRandomico = random.randint(100000, 999999)
        self.numero_conta = numeroRandomico
        print(f"Conta criada com sucesso!: {self.titular}, Numero da conta: {self.numero_conta}")

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Deposito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor inválido")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido")

    def consultar_saldo(self):
        print(f"Saldo atual da conta de {self.titular}: R${self.saldo:.2f}")

    def exibir_extrato(self):
        print(f"Extrato da conta {self.numero_conta} - Titular: {self.titular}")
        print(f"Saldo: R${self.saldo:.2f}")

def MenuLivro(livro):
    while True:
        print("\n//// Classe Livro ////")
        print("1. Abrir livro\n2. Ler paginas\n3. Exibir progresso\n4. Voltar")
        try:
            escolha = int(input("Sua escolha: "))
            if escolha == 1:
                livro.abrir_livro()
            elif escolha == 2:
                qtd = int(input("Quantas páginas você leu? "))
                livro.ler_paginas(qtd)
            elif escolha == 3:
                livro.exibir_progresso()
            elif escolha == 4:
                break
            else:
                print("Opção inválida")
        except ValueError:
            print("Opção inválida")
            time.sleep(2)

def MenuContaBancaria(conta):
    while True:
        print("\n//// Classe ContaBancaria ////")
        print("1. Criar conta\n2. Depositar\n3. Sacar\n4. Consultar saldo\n5. Exibir extrato\n6. Voltar")
        try:
            escolha = int(input("Sua escolha: "))
            if escolha == 1:
                conta.userTitular()
            elif escolha == 2:
                valor = float(input("Valor para depositar: "))
                conta.deposito(valor)
            elif escolha == 3:
                valor = float(input("Valor para sacar: "))
                conta.saque(valor)
            elif escolha == 4:
                conta.consultar_saldo()
            elif escolha == 5:
                conta.exibir_extrato()
            elif escolha == 6:
                break
            else:
                print("Opção inválida")
        except ValueError:
            print("Opção inválida")
            time.sleep(2)

def GerOpcoes(op):
    livro = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 96)
    conta = ContaBancaria()
    if op == 1:
        MenuLivro(livro)
    elif op == 2:
        MenuContaBancaria(conta)
    elif op == 3:
        print("Saindo do sistema...")
        return

def MainMenu():
    while True:
        print("\n//// Sistema de Classes ////")
        print("1. Classe Livro\n2. Classe ContaBancaria\n3. Sair do sistema")
        try:
            opcao = int(input("Sua escolha: "))
            if opcao == 3:
                print("\nEncerrando o sistema...")
                break
            GerOpcoes(opcao)
        except ValueError:
            print("Opção inválida")
            time.sleep(2)

MainMenu()
