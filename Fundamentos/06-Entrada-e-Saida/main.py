# Exercício 1
nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Seja bem-vindo ao Python!")

# Exercício 2
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
print(f"A soma de {numero1} e {numero2} é: {numero1 + numero2}")

# Exercício 3
ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nascimento
print(f"Você tem {idade} anos.")

# Exercício 4
nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto (em %): "))
preco_final = preco_produto * (1 - desconto / 100)
print(f"O preço final do produto '{nome_produto}' é: R$ {preco_final:.2f}")

# Exercício 5
altura_metros = float(input("Digite a altura em metros: "))
altura_centimentos = altura_metros * 100
print(f"A altura {altura_metros:.2f}m é igual a {altura_centimentos:.2f}cm")

# Exercício 6
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f'A media das notas {nota1}, {nota2}, {nota3} é: {media:.2f}')