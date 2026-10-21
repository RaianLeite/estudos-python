# 07 — Operadores em Python

## 1. O que são operadores?

Operadores são símbolos ou palavras utilizados para realizar operações com valores e variáveis.

Por exemplo:

```python
numero1 = 10
numero2 = 5

print(numero1 + numero2)
```

Saída:

```text
15
```

Nesse exemplo, o operador `+` realiza a soma dos dois números.

Em Python, existem diferentes categorias de operadores. Neste tópico, estudaremos:

- Operadores aritméticos.
- Ordem de precedência.
- Operadores de atribuição.
- Operadores de comparação.
- Operadores lógicos.
- Operadores de identidade.
- Operadores de associação.

Esses conceitos são importantes para criar cálculos, comparar valores e controlar o comportamento dos programas.

## 2. Operadores aritméticos

Os operadores aritméticos permitem realizar operações matemáticas.

| Operador | Operação | Exemplo | Resultado |
|---|---|---|---:|
| `+` | Adição | `10 + 5` | `15` |
| `-` | Subtração | `10 - 5` | `5` |
| `*` | Multiplicação | `10 * 5` | `50` |
| `/` | Divisão | `10 / 5` | `2.0` |
| `//` | Divisão inteira | `10 // 3` | `3` |
| `%` | Resto da divisão | `10 % 3` | `1` |
| `**` | Potenciação | `2 ** 3` | `8` |

### Adição (`+`)

Soma dois valores numéricos.

```python
resultado = 10 + 5
print(resultado)
```

Saída:

```text
15
```

O operador `+` também pode concatenar strings, isto é, unir textos:

```python
nome = "Raian"
sobrenome = "Leite"

print(nome + " " + sobrenome)
```

Saída:

```text
Raian Leite
```

Atenção: somar números e textos diretamente pode causar um `TypeError`.

```python
# Este código gera um erro:
# print(10 + "5")
```

### Subtração (`-`)

Subtrai o segundo valor do primeiro.

```python
resultado = 20 - 7
print(resultado)
```

Saída:

```text
13
```

### Multiplicação (`*`)

Multiplica dois valores.

```python
resultado = 6 * 4
print(resultado)
```

Saída:

```text
24
```

O operador também pode repetir uma string:

```python
print("Python! " * 3)
```

Saída:

```text
Python! Python! Python!
```

### Divisão (`/`)

Realiza uma divisão e retorna um resultado do tipo `float`, mesmo quando a divisão é exata.

```python
resultado = 10 / 2

print(resultado)
print(type(resultado))
```

Saída:

```text
5.0
<class 'float'>
```

Não é possível dividir um número por zero. Essa operação gera um `ZeroDivisionError`.

### Divisão inteira (`//`)

Retorna o quociente da divisão arredondado para baixo, em direção ao menor inteiro.

```python
print(10 // 3)
print(9 // 2)
```

Saída:

```text
3
4
```

Atenção: “divisão inteira” não significa simplesmente remover a parte decimal em todos os casos. O resultado é arredondado para baixo. Por exemplo:

```python
print(-10 // 3)
```

Saída:

```text
-4
```

### Resto da divisão (`%`)

Retorna o resto de uma divisão.

```python
print(10 % 3)
print(12 % 4)
```

Saída:

```text
1
0
```

Esse operador é útil para verificar se um número é par ou ímpar:

```python
numero = 8

print(numero % 2)
```

Saída:

```text
0
```

Quando o resto da divisão de um inteiro por `2` é `0`, ele é par. Quando é `1`, ele é ímpar.

### Potenciação (`**`)

Eleva um número a uma potência.

```python
print(2 ** 3)
print(5 ** 2)
```

Saída:

```text
8
25
```

`2 ** 3` significa \(2^3\), ou seja, `2 * 2 * 2`.

## 3. Ordem de precedência

Quando uma expressão contém vários operadores, o Python segue uma ordem para decidir quais operações executar primeiro.

Em geral, para os operadores que estamos estudando:

1. Parênteses: `()`.
2. Potenciação: `**`.
3. Sinais unários, como `-x` e `+x`.
4. Multiplicação, divisão, divisão inteira e resto: `*`, `/`, `//`, `%`.
5. Adição e subtração: `+`, `-`.
6. Comparações.
7. Operador lógico `not`.
8. Operador lógico `and`.
9. Operador lógico `or`.

Essa lista é uma referência para os operadores abordados neste material; existem outras regras e detalhes na precedência completa do Python.

Exemplo sem parênteses:

```python
resultado = 2 + 3 * 4
print(resultado)
```

Saída:

```text
14
```

A multiplicação é realizada antes da adição: `3 * 4 = 12`; depois, `2 + 12 = 14`.

Exemplo com parênteses:

```python
resultado = (2 + 3) * 4
print(resultado)
```

Saída:

```text
20
```

Os parênteses fazem a soma acontecer primeiro.

**Boa prática:** utilize parênteses quando ajudarem a deixar uma expressão mais clara, mesmo quando não forem obrigatórios.

## 4. Operadores de atribuição

O operador `=` atribui um valor a uma variável.

```python
saldo = 100
```

Isso significa que a variável `saldo` passa a armazenar o valor `100`. O sinal `=` não é o mesmo que o operador de comparação `==`.

Os operadores de atribuição combinada permitem realizar uma operação e atualizar a variável.

| Operador | Exemplo | Equivale a |
|---|---|---|
| `=` | `numero = 10` | Atribui `10` |
| `+=` | `numero += 5` | `numero = numero + 5` |
| `-=` | `numero -= 3` | `numero = numero - 3` |
| `*=` | `numero *= 2` | `numero = numero * 2` |
| `/=` | `numero /= 4` | `numero = numero / 4` |
| `//=` | `numero //= 2` | `numero = numero // 2` |
| `%=` | `numero %= 3` | `numero = numero % 3` |
| `**=` | `numero **= 2` | `numero = numero ** 2` |

Exemplo:

```python
saldo = 100

saldo += 50
print(saldo)

saldo -= 30
print(saldo)
```

Saída:

```text
150
120
```

O valor é atualizado a cada operação. A atribuição combinada não apenas calcula um resultado para exibição: ela modifica o valor armazenado na variável.

## 5. Operadores de comparação

Os operadores de comparação verificam a relação entre dois valores. O resultado de uma comparação é um booleano: `True` ou `False`.

| Operador | Significado | Exemplo | Resultado |
|---|---|---|---|
| `==` | Igual a | `10 == 10` | `True` |
| `!=` | Diferente de | `10 != 5` | `True` |
| `>` | Maior que | `10 > 5` | `True` |
| `<` | Menor que | `3 < 5` | `True` |
| `>=` | Maior ou igual a | `10 >= 10` | `True` |
| `<=` | Menor ou igual a | `5 <= 3` | `False` |

Exemplo:

```python
idade = 23

print(idade >= 18)
print(idade < 18)
```

Saída:

```text
True
False
```

A primeira comparação verifica se a idade é maior ou igual a `18`. A segunda verifica se é menor que `18`.

### Diferença entre `=` e `==`

- `=` atribui um valor a uma variável.
- `==` compara dois valores para verificar se são iguais.

```python
numero = 10

print(numero == 10)
```

Saída:

```text
True
```

Um erro comum é utilizar `=` quando a intenção era comparar valores. Em uma expressão de comparação, utilize `==`.

## 6. Operadores lógicos

Os operadores lógicos combinam ou invertem condições booleanas.

| Operador | Funcionamento |
|---|---|
| `and` | Retorna `True` quando as duas condições são verdadeiras. |
| `or` | Retorna `True` quando pelo menos uma das condições é verdadeira. |
| `not` | Inverte o valor lógico: `True` vira `False` e vice-versa. |

### Operador `and`

As duas condições precisam ser verdadeiras para que o resultado seja verdadeiro.

```python
idade = 23
tem_carteira = True

print(idade >= 18 and tem_carteira)
```

Saída:

```text
True
```

Se uma das condições for falsa, o resultado será `False`.

```python
print(idade >= 18 and False)
```

Saída:

```text
False
```

### Operador `or`

Basta que pelo menos uma condição seja verdadeira.

```python
tem_cartao = False
tem_dinheiro = True

print(tem_cartao or tem_dinheiro)
```

Saída:

```text
True
```

### Operador `not`

Inverte o resultado lógico.

```python
ativo = True

print(not ativo)
```

Saída:

```text
False
```

Os operadores lógicos serão especialmente úteis quando estudarmos as estruturas condicionais com `if`, `elif` e `else`.

## 7. Operadores de identidade

Os operadores `is` e `is not` verificam se duas referências apontam para o mesmo objeto, e não simplesmente se os valores são iguais.

```python
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(lista1 == lista2)
print(lista1 is lista2)
print(lista1 is lista3)
```

Saída:

```text
True
False
True
```

Entenda:

- `lista1 == lista2` retorna `True` porque as listas têm o mesmo conteúdo.
- `lista1 is lista2` retorna `False` porque são objetos diferentes.
- `lista1 is lista3` retorna `True` porque ambas as variáveis referenciam o mesmo objeto.

O operador `is not` verifica o contrário: se as referências apontam para objetos diferentes.

Para comparar valores comuns, normalmente utilize `==` e `!=`. O operador `is` é usado com frequência para verificar valores como `None`.

```python
resultado = None

print(resultado is None)
```

Saída:

```text
True
```

## 8. Operadores de associação

Os operadores `in` e `not in` verificam se um elemento está presente em uma sequência ou coleção, como uma string, lista ou tupla.

### Operador `in`

```python
linguagens = ["Python", "Java", "JavaScript"]

print("Python" in linguagens)
print("C++" in linguagens)
```

Saída:

```text
True
False
```

Também funciona com strings:

```python
frase = "Estou estudando Python"

print("Python" in frase)
print("Java" in frase)
```

Saída:

```text
True
False
```

### Operador `not in`

Verifica se um elemento não está presente.

```python
linguagens = ["Python", "Java", "JavaScript"]

print("C++" not in linguagens)
```

Saída:

```text
True
```

Atenção: a verificação em strings diferencia letras maiúsculas de minúsculas. Por exemplo, `"python" in "Python"` retorna `False`.

## 9. Erros comuns

### Erro 1 — Confundir `=` com `==`

```python
idade = 18
print(idade == 18)
```

Use `=` para atribuir e `==` para comparar.

### Erro 2 — Dividir por zero

```python
# Gera ZeroDivisionError:
# resultado = 10 / 0
```

Antes de dividir, verifique se o divisor não é zero. Aprenderemos a organizar esse tipo de verificação com estruturas condicionais.

### Erro 3 — Esquecer a ordem das operações

```python
print(2 + 3 * 4)      # 14
print((2 + 3) * 4)    # 20
```

Os parênteses mudam a ordem de execução.

### Erro 4 — Comparar tipos incompatíveis

```python
# Gera TypeError:
# print(10 > "5")
```

Compare valores de tipos compatíveis. Se o dado vier de `input()` e representar um número, converta-o antes da comparação.

### Erro 5 — Usar `is` para comparar valores

```python
nome = "Python"

print(nome == "Python")
```

Para verificar igualdade de valores, prefira `==`. Não dependa de `is` para comparar textos ou números.

## 10. Boas práticas

- Escolha nomes de variáveis que deixem claro o que elas armazenam.
- Utilize parênteses para tornar cálculos complexos mais legíveis.
- Converta entradas de `input()` para o tipo adequado antes de calcular ou comparar.
- Diferencie atribuição (`=`) de comparação (`==`).
- Verifique se o divisor pode ser zero antes de realizar uma divisão.
- Utilize `==` para comparar valores e `is None` para verificar se algo é `None`.
- Teste as expressões com valores diferentes, inclusive limites como zero e números negativos.
- Leia os resultados e as mensagens de erro para entender o comportamento do programa.

## 11. Exercícios de fixação

Resolva os exercícios no arquivo `main.py`. Tente escrever o código antes de consultar os exemplos deste material.

### Exercício 1 — Calculadora básica

Solicite dois números inteiros ao usuário. Exiba:

- A soma.
- A subtração.
- A multiplicação.
- A divisão.

Utilize `input()` e `int()` ou `float()`. Para este exercício, considere que o segundo número não será zero.

### Exercício 2 — Divisão e resto

Solicite dois números inteiros e exiba o resultado da divisão inteira (`//`) e o resto (`%`).

Teste com `17` e `5`.

Resultado esperado:

```text
Divisão inteira: 3
Resto: 2
```

### Exercício 3 — Potenciação

Solicite a base e o expoente ao usuário. Calcule e exiba a potência utilizando `**`.

Exemplo: base `2` e expoente `4` devem resultar em `16`.

### Exercício 4 — Ordem de precedência

Sem executar primeiro, tente prever o resultado de cada expressão. Depois, escreva cada uma no Python e confira.

```python
print(5 + 2 * 3)
print((5 + 2) * 3)
print(20 / 4 + 2)
print(2 ** 3 * 2)
```

### Exercício 5 — Atualizando um saldo

Comece com `saldo = 200`. Em seguida:

1. Adicione `50` usando `+=`.
2. Subtraia `30` usando `-=`.
3. Multiplique o saldo por `2` usando `*=`.
4. Exiba o saldo após cada operação.

### Exercício 6 — Comparando números

Solicite dois números e exiba o resultado das comparações:

- Se são iguais.
- Se são diferentes.
- Se o primeiro é maior que o segundo.
- Se o primeiro é menor ou igual ao segundo.

Os resultados devem ser `True` ou `False`.

### Exercício 7 — Operadores lógicos

Solicite a idade de uma pessoa e se ela possui ingresso (`True` ou `False`, conforme a forma que você implementar). Exiba uma expressão que indique se ela tem pelo menos 18 anos **e** possui ingresso.

Dica: converta a idade para `int()` e use `and`.

### Exercício 8 — Verificando par ou ímpar

Solicite um número inteiro e utilize `%` para descobrir se ele é par ou ímpar.

Dica: se `numero % 2 == 0`, o número é par; caso contrário, é ímpar. Neste exercício, você pode utilizar `if` e `else`, mesmo que o tópico de estruturas condicionais seja estudado depois.


### Exercício 9 — Desafio: preço com desconto

Solicite o preço de um produto e o percentual de desconto. Calcule o valor do desconto e o preço final.

Fórmulas:

```text
valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto
```

Exiba o preço original, o desconto em reais e o preço final com duas casas decimais.

## 12. Revisão

Ao concluir este tópico, você deverá saber:

- [ ] Utilizar operadores aritméticos.
- [ ] Diferenciar `/`, `//` e `%`.
- [ ] Calcular potências com `**`.
- [ ] Entender a ordem de precedência e o uso de parênteses.
- [ ] Atualizar variáveis com operadores de atribuição combinada.
- [ ] Comparar valores e interpretar `True` e `False`.
- [ ] Combinar condições com `and`, `or` e `not`.
- [ ] Diferenciar igualdade de valores e identidade de objetos.
- [ ] Verificar a presença de elementos com `in` e `not in`.
- [ ] Reconhecer erros comuns envolvendo operadores.