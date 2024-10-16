import unittest
from exercicios import cotacao, novoSalario, podeVotar

class TestExercicios(unittest.TestCase):

    def test_ex1(self):
        # teste positivo - dá positivo
        positivo = cotacao(saldo=2000) # 579
        self.assertEqual(positivo, 579.71)
        # teste negativo - dá errado
        negativo = cotacao(saldo=(-15886)) # -4604
        self.assertEqual(negativo, 'Saldo insuficiente.')
        # teste que quebra - usa string ou algo que quebra a lógica
        quebra = cotacao(saldo='a') # TypeError
        self.assertEqual(quebra, 'O valor precisa ser do tipo float.')
        # teste divisao por zero
        zero = cotacao(saldo=0) # 'Não é possível dividir por zero.'
        self.assertEqual(zero, 'Não é possível dividir por zero.')

    def test_ex2(self):
        # teste positivo
        positivo = novoSalario(nome='Ricardo',salario=10000,tempoServico=15) # 12000
        self.assertEqual(positivo, 12000)
        # teste negativo
        negativo = novoSalario(nome='Jéssica',salario=(-2000),tempoServico=2) # 'Valores negativos não são permitidos.'
        self.assertEqual(negativo, 'Valores negativos não são permitidos.')
        # # teste quebra
        quebra = novoSalario(nome='Pedro',salario='a',tempoServico='b') # TypeError
        self.assertEqual(quebra, 'O valor precisa ser do tipo float.')
        # teste zero
        zero = novoSalario(nome='Pedro',salario=1200,tempoServico=0) # 'Não é possível dividir por zero.'
        self.assertEqual(zero, 'Não é possível dividir por zero.')
        # teste nome errado
        nome = novoSalario(nome=12,salario=10000,tempoServico=15) # 'Digite um nome válido.'
        self.assertEqual(nome, 'Digite um nome válido.')


    def test_ex3(self):
        # teste positivo
        positivo = podeVotar(2003) # 'Pode votar.'
        self.assertEqual(positivo, 'Pode votar.')
        # teste negativo
        negativo = podeVotar((-2015)) # 4039
        self.assertEqual(negativo, 'Valores negativos são válidos.')
        # teste quebra
        quebra = podeVotar('a')
        self.assertEqual(quebra, 'O valor precisa ser do tipo inteiro.')
        # teste zero
        zero = podeVotar(0)
        self.assertEqual(zero, 'Zero não é um ano válido.')

if __name__ == '__main__':
    unittest.main()