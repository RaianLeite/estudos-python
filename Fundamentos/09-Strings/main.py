#Exercício 1
nome = "Raian"
cidade = "Belo Horizonte"
linguagem = "Python"

print(type(nome), type(cidade), type(linguagem))

#Exercício 2
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

print(nome + " " + sobrenome)

#Exercício 3
palavra = input("Digite uma palavra: ")
palavra *= 5

print(palavra)

#Exercício 4
linguagem = "PYTHON"

print(linguagem[0])
print(linguagem[2])
print(linguagem[-1])
print(linguagem[-2])

#Exercício 5
frase = "ESTOU ESTUDANDO PYTHON"

print(frase[5:])
print(frase[6:0:-1])
print(frase[0:7])
print(frase[::-1])

#Exercício 6
frase = input("Digite uma frase: ")

print(frase)
print(len(frase))

#Exercício 7
nome_completo = input("Digite seu nome completo: ")

print(nome_completo.upper())          # Maiusculas
print(nome_completo.lower())          # Minusculas
print(nome_completo.capitalize())     # Apenas a primeira letra da string 
print(nome_completo.title())          # Primeira letra maiuscula de todas as palavras

#Exercício 8
nome_completo = input("Digite seu nome completo com espaços antes e depois do nome: ")

print(nome_completo)
print(nome_completo.strip())
print(nome_completo.lstrip())
print(nome_completo.rstrip())

#Exercício 9
frase = "Estou estudando Java"

print(frase)
print(frase.replace("Java", "Python"))

#Exercício 10
frase = "Python é uma linguagem poderosa. Python é muito utilizado."

print(frase.find("Python"))
print(frase.count("Python"))

#Exercício 11
frase = input("Digite uma frase: ")
frase = frase.lower()

print("python" in frase)

#Exercício 12
nome_arquivo = input("Digite o nome do arquivo: ")

print(nome_arquivo.endswith(".pdf"))

#Exercício 13
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print(f"Meu nome é {nome}, tenho {idade} anos e minha altura é {altura:.2f} metros.")

#Exercício 14
frase = input("Digite uma frase: ")

print(f"Frase original: {frase}")
print(f"Maiúsculas: {frase.upper()}")
print(f"Minúsculas: {frase.lower()}")
print(f"Quantidade de caracteres: {len(frase)}")
print(f"Quantidade de espaços: {frase.count(' ')}")
print(f"Quantidade da letra A: {frase.lower().count('a')}")
print(f"Frase invertida: {frase[::-1]}")