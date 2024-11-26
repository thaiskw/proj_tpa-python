from Pessoa import *

import os

def limpar():os.system('cls')

res = 0
limpar()
def pergunta():
    res = int(input("Deseja cadastrar uma nova pessoa? 1 - SIM ou 0 - NÃO: "))
    return res

cadastro = []

res = pergunta()
while(res == 1):
    nome = str(input("Digite o nome da pessoa: "))
    idade = int(input("Digite a idade da pessoa: "))
    cargo = str(input("Digite o cargo da pessoa: "))
    salario = float(input("Digite o salário da pessoa:"))
    
    cadastro.append(Pessoa(nome,idade,cargo,salario))

    res = pergunta()

def mostrar():
    print("{:<4}{:<10}{:<7}{:<10}{:<7}"
          .format("N°","Nome","Idade","Cargo","Salário"))

    y = 1
    for x in cadastro:
        print("{:<4}{:<10}{:<7}{:<10}{:<7}"
              .format(y,
                      x.get_nome(),
                      x.get_idade(),
                      x.get_cargo(),
                      x.get_salario()
                ))
        y =+ 1
        

def alterar():
    mostrar()
    linha = int(input("Digite a linha que deseja alterar: "))
    linha -= 1
    opcao = int(input("Escolha as opções: \n1 - Nome\n2 - Idade\n3 - Cargo\n4 - Salário\n"))
    if(opcao == 1):
        nome = str(input("Digite um novo nome: "))
        cadastro[linha].set_nome(nome)

    elif(opcao == 2):
        idade = int(input("Digite a nova idade: "))
        cadastro[linha].set_idade(idade)

    elif(opcao == 3):
        cargo = str(input("Digite o novo cargo: "))
        cadastro[linha].set_cargo(cargo)

    elif(opcao == 4):
        salario = float(input("Digite o novo salário: "))
        cadastro[linha].set_salario(salario)

    else:
        print("Valor incorreto!!!")
        alterar()
    mostrar()
def remover():
    linha = int(input("Digite a linha que deseja remover: "))
    linha -= 1
    res = int(input("Certeza que deseja remover a linha {linha}?\n1 - Sim\n2 - Não "))
if(res == 1):
    cadastro.pop(linha)
    print("Linha removida com sucesso!\n")
    mostrar()

alterar()
remover()
mostrar()
