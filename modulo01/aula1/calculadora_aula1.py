nome = (input('Digite o seu nome:'))
altura = float(input('Digite sua altura:'))
peso = input('Digite seu peso:')

imc = (altura*altura)/float(peso)
print('{} - {} - {} - {:.2f}'.format(nome, altura, peso, imc))