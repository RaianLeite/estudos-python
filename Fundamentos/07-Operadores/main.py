# Exercício 1
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print(f'A soma de {numero1} e {numero2} é: {soma}')
print(f'A subtração de {numero1} e {numero2} é: {subtracao}')
print(f'A multiplicação de {numero1} e {numero2} é: {multiplicacao}')
print(f'A divisão de {numero1} e {numero2} é: {divisao}')

# Exercício 2
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

divisao = numero1 // numero2
resto = numero1 % numero2

print(f'A divisão de {numero1} e {numero2} é: {divisao} e o resto é: {resto}')

# # Exercício 3
base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))

potencia = base ** expoente

print(f'A potencia é: {potencia}')

# Exercício 4
#11
#21
#7.0
#16

# Exercício 5
saldo = 200
print(f'Saldo = {saldo}')
saldo += 50
print(f'Saldo = {saldo}')
saldo -= 30
print(f'Saldo = {saldo}')
saldo *= 2
print(f'Saldo = {saldo}')

# Exercício 6
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

iguais = numero1 == numero2
diferentes = numero1 != numero2
maior = numero1 > numero2
menor_igual = numero1 <= numero2 

print(iguais)
print(diferentes)
print(maior)
print(menor_igual)

# Exercício 7
idade = int(input("Digite sua idade: "))
resposta = input("Tem ingresso? [true/false]: ")

ingresso = resposta == "true"

if idade >= 18 and ingresso:
    print("Maior de idade e tem ingresso")
else:
    print("Não atende às duas condições")

# Exercício 8
numero = int(input("Digite o número: "))
if numero % 2 == 0:
    print('numero par')
else:
    print('numero ímpar')

# Exercício 9
valor_produto = float(input('Valor do produto: '))
desconto = float(input('desconto do produto (%): '))

valor_final = valor_produto * (1 - desconto / 100)
valor_desconto = valor_produto * (desconto / 100)

print(f'Valor do produto: {valor_produto:.2f}')
print(f'Valor do desconto: R$ {valor_desconto:.2f}')
print(f'Valor a pagar: R$ {valor_final:.2f}')