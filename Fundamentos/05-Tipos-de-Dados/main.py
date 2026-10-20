# Exercício 1
nome = "Python"
quantidade = 15
preco = 29.90
disponivel = True

print(type(nome))
print(type(quantidade))
print(type(preco))
print(type(disponivel))

# Exercício 2
a = 10
b = "10"

print(a + a)
print(b + b)

# Saidas:
# 20
# 1010

# Exercício 3
string_exemplo = "25"
string_exemplo = int(string_exemplo)
print(f"O resultado é: {string_exemplo} e o tipo é: {type(string_exemplo)}")

string_exemplo = "19.90"
string_exemplo = float(string_exemplo)
print(f"O resultado é: {(string_exemplo)} e o tipo é: {type(string_exemplo)}")

int_exemplo = 100
int_exemplo = str(int_exemplo)
print(f"O resultado é: {(int_exemplo)} e o tipo é: {type(int_exemplo)}")

int_exemplo = 0
int_exemplo = bool(int_exemplo)
print(f"O resultado é: {(int_exemplo)} e o tipo é: {type(int_exemplo)}")

# Exercício 4
preco = 150.00
desconto = 25.00

print(f"Preco final: {preco - desconto:.2f}")

# Exercício 5
# false
# true
# false
# true
# true

# Exercício 6

# idade = int("vinte e três")
# print(idade)

# O erro ocorre porque int não aceita caracter, apenas numeros inteiros

# O correto seria:
idade = int("23")
print(idade)
