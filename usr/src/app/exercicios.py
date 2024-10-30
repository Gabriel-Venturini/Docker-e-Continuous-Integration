import datetime

# 1) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$)
# e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.

def cotacao(saldo:float):
    try:
        if saldo < 0:
            return 'Saldo insuficiente.'
        elif saldo > 0:
            dolar = saldo / 3.45
            return float(f'{dolar:.2f}')
        elif saldo == 0:
            return 'Não é possível dividir por zero.'
    except TypeError:
        return 'O valor precisa ser do tipo float.'

# 2) Desenvolva um programa que leia o nome de um funcionário, seu salário,
# quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
# acordo com a tabela a seguir:
# - Até 3 anos de empresa: aumento de 3%
# - entre 3 e 10 anos: aumento de 12.5%
# - 10 anos ou mais: aumento de 20%

def novoSalario(nome:str, salario:float, tempoServico:int):
    try:
        if isinstance(nome, str):
            if salario  < 0 or tempoServico < 0:
                return 'Valores negativos não são permitidos.'
            elif salario == 0 or tempoServico == 0:
                return 'Não é possível dividir por zero.'
        else:
            return 'Digite um nome válido.'
        if tempoServico <= 3:
            return salario * 1.03
        elif tempoServico > 3 and tempoServico < 10:
            return salario * 1.125
        elif tempoServico >= 10:
            return salario * 1.2
    except TypeError:
        return 'O valor precisa ser do tipo float.'
# 3)Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade
# dela e depois mostre se ela pode ou não votar.

def podeVotar(anoNasc:int):
    try:
        if anoNasc < 0:
            return 'Valores negativos são válidos.'
        elif anoNasc == 0:
            return 'Zero não é um ano válido.'
        today = datetime.date.today()
        year = today.year  # pega ano atual
        idade = year - anoNasc
        if idade >= 16:
                return 'Pode votar.'
        else:
            return 'Não pode votar.'
    except TypeError:
        return 'O valor precisa ser do tipo inteiro.'
        
    
    
if __name__ == '__main__':
    # ex1
    cota = cotacao(saldo=15000)
    print(cota)

    # ex2
    salario = novoSalario('José', 2000, 10)
    print(salario)

    # ex3
    idade = podeVotar(2010)
    print(idade)