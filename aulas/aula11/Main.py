import Pessoa

import os

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
    
    cadastro.append(Pessoa.Pessoa(nome,idade,cargo,salario))

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
        y += 1
        mostrar()
    