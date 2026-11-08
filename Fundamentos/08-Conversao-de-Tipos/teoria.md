# 08 — Conversão de Tipos em Python

## 1. O que é conversão de tipos?

A conversão de tipos consiste em transformar um valor de um tipo de dado em outro.

Em Python, trabalhamos com diferentes tipos de dados, como:

- `int`: números inteiros.
- `float`: números decimais.
- `str`: textos.
- `bool`: valores booleanos (`True` ou `False`).

Em determinadas situações, precisamos converter um valor para realizar uma operação corretamente.

### Exemplo

```python
numero = "10"

print(numero)
print(type(numero))
```

**Saída:**

```text
10
<class 'str'>
```

Embora o valor pareça um número, ele está armazenado como texto porque foi declarado entre aspas.

---

## 2. Conversão para inteiro — `int()`

A função `int()` converte um valor compatível para um número inteiro.

### Exemplo 1 — Texto para inteiro

```python
numero = "10"

numero_convertido = int(numero)

print(numero_convertido)
print(type(numero_convertido))
```

**Saída:**

```text
10
<class 'int'>
```

### Exemplo 2 — Operações matemáticas

```python
numero1 = "10"
numero2 = "5"

resultado = int(numero1) + int(numero2)

print(resultado)
```

**Saída:**

```text
15
```

Sem a conversão, o operador `+` entre dois textos concatena os valores em vez de realizar uma soma matemática.

### Atenção

```python
numero = int("10.5")
```

Esse código gera um `ValueError`, pois o texto `"10.5"` não representa um inteiro válido diretamente.

Para converter um texto decimal, utilize `float()` primeiro, se fizer sentido descartar a parte decimal:

```python
numero = int(float("10.5"))

print(numero)
```

**Saída:**

```text
10
```

A conversão de `float` para `int` descarta a parte decimal, sem arredondar.

---

## 3. Conversão para decimal — `float()`

A função `float()` converte um valor compatível para um número de ponto flutuante.

### Exemplo 1 — Texto para decimal

```python
preco = "19.90"

preco_convertido = float(preco)

print(preco_convertido)
print(type(preco_convertido))
```

**Saída:**

```text
19.9
<class 'float'>
```

O Python pode exibir `19.9` em vez de `19.90`, pois zeros finais não são necessários para representar esse número.

### Exemplo 2 — Cálculo com decimais

```python
peso = "75.5"
altura = "1.80"

peso = float(peso)
altura = float(altura)

print(peso)
print(altura)
```

**Saída:**

```text
75.5
1.8
```

### Atenção ao separador decimal

Em Python, normalmente utilizamos o ponto como separador decimal:

```python
preco = float("19.90")
```

O código abaixo gera um erro:

```python
preco = float("19,90")
```

Para trabalhar com entradas que utilizam vírgula, é possível substituir a vírgula por ponto antes da conversão:

```python
preco = float("19,90".replace(",", "."))

print(preco)
```

**Saída:**

```text
19.9
```

---

## 4. Conversão para texto — `str()`

A função `str()` converte um valor para uma representação textual.

### Exemplo 1 — Inteiro para texto

```python
idade = 23

idade_texto = str(idade)

print(idade_texto)
print(type(idade_texto))
```

**Saída:**

```text
23
<class 'str'>
```

### Exemplo 2 — Concatenando textos

```python
idade = 23

mensagem = "Minha idade é " + str(idade) + " anos."

print(mensagem)
```

**Saída:**

```text
Minha idade é 23 anos.
```

Outra opção é utilizar uma f-string:

```python
idade = 23

print(f"Minha idade é {idade} anos.")
```

As f-strings permitem inserir valores em textos sem precisar converter cada valor manualmente para concatená-lo.

---

## 5. Conversão para booleano — `bool()`

A função `bool()` converte um valor para `True` ou `False`.

### Exemplo 1 — Números

```python
print(bool(1))
print(bool(0))
print(bool(-1))
```

**Saída:**

```text
True
False
True
```

Em Python, o número zero é considerado falso, enquanto números diferentes de zero são considerados verdadeiros.

### Exemplo 2 — Textos

```python
print(bool("Python"))
print(bool(""))
print(bool("0"))
```

**Saída:**

```text
True
False
True
```

Regras importantes:

- Texto não vazio: `True`.
- Texto vazio (`""`): `False`.
- O texto `"0"` não está vazio, portanto resulta em `True`.

### Exemplo 3 — Listas

```python
print(bool([1, 2, 3]))
print(bool([]))
```

**Saída:**

```text
True
False
```

Listas vazias são consideradas falsas, enquanto listas com elementos são consideradas verdadeiras.

---

## 6. Conversão de dados recebidos com `input()`

A função `input()` sempre retorna um texto (`str`), mesmo quando o usuário digita números.

### Exemplo sem conversão

```python
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

resultado = numero1 + numero2

print(resultado)
```

Se o usuário digitar `10` e `5`, a saída será:

```text
105
```

Isso acontece porque o operador `+` concatena os dois textos.

### Exemplo com conversão

```python
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = numero1 + numero2

print(f"A soma é: {resultado}")
```

Se o usuário digitar `10` e `5`, a saída será:

```text
A soma é: 15
```

### Quando utilizar `int()` ou `float()`?

Utilize `int()` quando precisar de números inteiros, como quantidades de produtos ou idades em anos completos.

Utilize `float()` quando precisar de valores que aceitem casas decimais, como pesos, alturas ou medidas.

---

## 7. Erros comuns na conversão

### Erro 1 — Converter um texto inválido para inteiro

```python
numero = int("Python")
```

Resultado: `ValueError`.

O texto não representa um número inteiro válido.

### Erro 2 — Somar texto e número

```python
numero = "10"

resultado = numero + 5
```

Resultado: `TypeError`.

O Python não permite somar diretamente uma string e um inteiro.

Correção:

```python
numero = "10"

resultado = int(numero) + 5

print(resultado)
```

**Saída:**

```text
15
```

### Erro 3 — Confundir conversão com arredondamento

```python
print(int(8.9))
```

**Saída:**

```text
8
```

A função `int()` descarta a parte decimal. Ela não arredonda o número.

Para arredondar, existe a função `round()`:

```python
print(round(8.9))
```

**Saída:**

```text
9
```

---

## 8. Resumo das principais funções

| Função | Finalidade | Exemplo |
|---|---|---|
| `int()` | Converter para inteiro | `int("10")` |
| `float()` | Converter para decimal | `float("3.5")` |
| `str()` | Converter para texto | `str(25)` |
| `bool()` | Converter para booleano | `bool(1)` |
| `type()` | Identificar o tipo de um valor | `type(10)` |
| `round()` | Arredondar um número | `round(8.9)` |

**Importante:** `type()` não converte valores. Ela apenas informa o tipo do objeto.

---

## 9. Exercícios práticos

Tente resolver os exercícios sem consultar as respostas imediatamente. Crie um arquivo `main.py` para praticar.

### Exercício 1 — Conversão para inteiro

Crie uma variável contendo o texto `"25"`, converta-a para inteiro e exiba o valor e seu tipo.

### Exercício 2 — Soma de números

Solicite dois números inteiros ao usuário e exiba a soma dos valores.

### Exercício 3 — Cálculo com decimais

Solicite o preço de um produto e a quantidade comprada. Converta os valores para os tipos adequados e calcule o preço total.

### Exercício 4 — Conversão para texto

Crie uma variável `idade` com um número inteiro. Converta-a para texto e exiba a mensagem:

`Tenho 23 anos.`

Utilize uma concatenação com `str()`.

### Exercício 5 — Booleanos

Sem executar o código, determine o resultado de cada expressão:

```python
print(bool(0))
print(bool(10))
print(bool(""))
print(bool("False"))
print(bool([]))
```

### Exercício 6 — Corrija o código

O código abaixo deve somar dois números, mas apresenta um problema. Corrija-o.

```python
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

resultado = numero1 + numero2

print(resultado)
```

### Exercício 7 — Desafio

Crie um programa que solicite:

- O nome de uma pessoa.
- A idade.
- A altura em metros.

Converta a idade para inteiro e a altura para decimal. Ao final, exiba uma mensagem contendo todas as informações.

---

## 11. Checklist de conclusão

Marque cada item depois de conseguir executá-lo sem ajuda.

- [ ] Entendo a diferença entre `int`, `float`, `str` e `bool`.
- [ ] Consigo converter textos numéricos para números.
- [ ] Entendo por que `input()` retorna uma string.
- [ ] Sei quando utilizar `int()` e `float()`.
- [ ] Consigo identificar erros comuns de conversão.
- [ ] Resolvi os exercícios 1 a 7.
- [ ] Revisei os exercícios em que tive dificuldade.

**Critério para avançar:** tente resolver os exercícios sem copiar o gabarito. Se errar, revise o conceito e tente novamente.

---