# 05 — Tipos de Dados em Python

## 1. O que são tipos de dados?

Tipos de dados definem a natureza de um valor que utilizamos em um programa.

Por exemplo, um nome é um texto, uma idade normalmente é um número inteiro e uma altura pode ser representada por um número decimal.

Veja:

```python
nome = "Raian"
idade = 23
altura = 1.83
estudando = True
```

Cada variável armazena um valor de um tipo diferente.

Os quatro tipos básicos que estudaremos inicialmente são:

- `str`: textos.
- `int`: números inteiros.
- `float`: números de ponto flutuante, usados para representar valores decimais.
- `bool`: valores lógicos, `True` ou `False`.

## 2. Tipo `str` — Strings

O tipo `str` representa textos, também chamados de *strings*.

Strings são delimitadas por aspas simples ou duplas.

```python
nome = "Raian Leite"
linguagem = 'Python'
mensagem = "Estou aprendendo programação"

print(nome)
print(linguagem)
print(mensagem)
```

Saída:

```text
Raian Leite
Python
Estou aprendendo programação
```

### Texto não é a mesma coisa que número

Observe:

```python
numero = 10
texto = "10"

print(numero)
print(texto)
```

Visualmente, ambos exibem `10`. Entretanto, o primeiro é um número inteiro e o segundo é um texto.

Essa diferença afeta as operações que podemos realizar com eles.

```python
print(10 + 5)
print("10" + "5")
```

Saída:

```text
15
105
```

No primeiro caso, o Python soma os números. No segundo, junta os textos. Essa operação é chamada de *concatenação*.

## 3. Tipo `int` — Números inteiros

O tipo `int` representa números inteiros, positivos, negativos ou zero, sem parte decimal.

Exemplos:

```python
idade = 23
quantidade = 10
temperatura = -5
saldo = 0

print(idade)
print(quantidade)
print(temperatura)
print(saldo)
```

Podemos utilizar números inteiros em operações matemáticas:

```python
quantidade = 10
quantidade += 5

print(quantidade)
```

Saída:

```text
15
```

Atenção: escrever `23` e escrever `"23"` são coisas diferentes. O primeiro é `int`; o segundo é `str`.

## 4. Tipo `float` — Números decimais

O tipo `float` representa números de ponto flutuante.

Em Python, utilizamos o ponto como separador decimal, e não a vírgula.

Correto:

```python
preco = 49.90
altura = 1.83
taxa = 0.10
```

Incorreto para representar um único número decimal:

```python
# preco = 49,90
```

A vírgula não funciona como separador decimal em Python; nesse exemplo, ela separa dois valores.

Também podemos fazer cálculos com `float`:

```python
preco = 49.90
desconto = 10.00

preco_final = preco - desconto

print(preco_final)
```

Saída esperada:

```text
39.9
```

Observe que o Python pode exibir `39.9` em vez de `39.90`. Isso não significa que o cálculo esteja errado.

Para exibir duas casas decimais:

```python
print(f"Preço final: R$ {preco_final:.2f}")
```

Saída:

```text
Preço final: R$ 39.90
```

**Observação:** números `float` podem apresentar pequenas imprecisões em determinados cálculos. Para aplicações financeiras que exigem precisão decimal, existe também o tipo `Decimal`, que estudaremos em outro momento.

## 5. Tipo `bool` — Valores lógicos

O tipo `bool` representa apenas dois valores:

- `True`: verdadeiro.
- `False`: falso.

Exemplo:

```python
estudando_python = True
tem_cadastro = False

print(estudando_python)
print(tem_cadastro)
```

Saída:

```text
True
False
```

Esses valores são úteis para representar condições e estados de um programa.

Por exemplo:

```python
idade = 23

maior_de_idade = idade >= 18

print(maior_de_idade)
```

Saída:

```text
True
```

A expressão `idade >= 18` verifica se a idade é maior ou igual a 18. O resultado é um valor booleano.

**Importante:** em Python, `True` e `False` começam com letra maiúscula.

## 6. Descobrindo o tipo com `type()`

A função `type()` informa o tipo de um valor ou de uma variável.

Exemplo:

```python
nome = "Raian"
idade = 23
altura = 1.83
estudando = True

print(type(nome))
print(type(idade))
print(type(altura))
print(type(estudando))
```

Saída:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

O resultado mostra o tipo correspondente a cada variável.

Podemos também verificar valores diretamente:

```python
print(type("Python"))
print(type(100))
print(type(9.5))
print(type(False))
```

## 7. Conversão de tipos

Em algumas situações, precisamos converter um valor de um tipo para outro.

As funções mais utilizadas inicialmente são:

| Função | Objetivo |
|---|---|
| `str()` | Converter para texto, quando possível |
| `int()` | Converter para inteiro, quando possível |
| `float()` | Converter para número decimal, quando possível |
| `bool()` | Converter para valor lógico |

### Convertendo para inteiro com `int()`

```python
numero = int("10")

print(numero)
print(type(numero))
```

Saída:

```text
10
<class 'int'>
```

Também podemos converter um `float` para `int`:

```python
numero = int(9.8)

print(numero)
```

Saída:

```text
9
```

Atenção: nesse caso, a parte decimal é descartada. `int(9.8)` não arredonda para 10.

### Convertendo para decimal com `float()`

```python
preco = float("49.90")

print(preco)
print(type(preco))
```

Saída:

```text
49.9
<class 'float'>
```

### Convertendo para texto com `str()`

```python
idade = 23

mensagem = "Minha idade é " + str(idade)

print(mensagem)
```

Saída:

```text
Minha idade é 23
```

A função `str()` transforma o número em texto, permitindo concatená-lo com outra string.

Outra possibilidade é utilizar uma f-string:

```python
idade = 23

print(f"Minha idade é {idade}")
```

### Convertendo para booleano com `bool()`

```python
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))
```

Saída:

```text
True
False
False
True
```

Em Python, zero e strings vazias são considerados falsos. Números diferentes de zero e strings não vazias são considerados verdadeiros.

Isso é útil em condições, mas lembre-se: `bool("False")` resulta em `True`, porque `"False"` é um texto não vazio.

## 8. Erros comuns em conversões

Nem todo valor pode ser convertido para qualquer tipo.

Por exemplo:

```python
numero = int("Python")
```

Esse código gera um `ValueError`, porque `"Python"` não representa um número inteiro válido.

Da mesma forma:

```python
numero = float("abc")
```

Também gera um `ValueError`.

Ao trabalhar com informações digitadas por usuários, é importante validar os dados e tratar possíveis erros. Estudaremos isso mais adiante.

## 9. Resumo dos quatro tipos básicos

| Tipo | Exemplo | Uso comum |
|---|---|---|
| `str` | `"Raian"` | Nomes e mensagens |
| `int` | `23` | Idades e quantidades |
| `float` | `1.83` | Alturas, medidas e valores decimais |
| `bool` | `True` | Estados e condições |

Um mesmo programa pode utilizar os quatro tipos simultaneamente:

```python
nome = "Raian"
idade = 23
altura = 1.83
estudando_python = True

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura:.2f}")
print(f"Estudando Python: {estudando_python}")
```

## 10. Boas práticas

- Escolha o tipo de dado adequado para cada informação.
- Lembre-se de que texto numérico, como `"10"`, não é o mesmo que o número `10`.
- Utilize `type()` para investigar o tipo de uma variável.
- Converta valores explicitamente quando necessário.
- Não presuma que qualquer texto pode ser convertido em número.
- Utilize `:.2f` para apresentar valores com duas casas decimais quando apropriado.
- Em cálculos financeiros que exigem precisão decimal, considere `Decimal` em vez de depender diretamente de `float`.

## 11. Exercícios de fixação

### Exercício 1 — Identificando tipos

Crie as variáveis abaixo e utilize `type()` para descobrir seus tipos:

```python
nome = "Python"
quantidade = 15
preco = 29.90
disponivel = True
```

Exiba o tipo de cada variável.

### Exercício 2 — Texto ou número?

Observe o código:

```python
a = 10
b = "10"

print(a + a)
print(b + b)
```

Antes de executar, escreva qual será a saída e explique por que os resultados são diferentes.

### Exercício 3 — Conversões

Converta os seguintes valores e exiba seus resultados e tipos:

- A string `"25"` para `int`.
- A string `"19.90"` para `float`.
- O número `100` para `str`.
- O número `0` para `bool`.

### Exercício 4 — Calculando o preço final

Crie as variáveis:

```python
preco = 150.00
desconto = 25.00
```

Calcule o preço final e exiba uma mensagem utilizando f-string com duas casas decimais.

### Exercício 5 — Verdadeiro ou falso?

Sem executar o código, preveja os resultados:

```python
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool("False"))
```

### Exercício 6 — Corrigindo uma conversão

O código abaixo gera um erro:

```python
idade = int("vinte e três")
print(idade)
```

Explique por que ocorre o erro e apresente uma maneira de corrigir o programa para armazenar a idade como número inteiro.

## 12. Revisão

Ao concluir este tópico, você deverá saber:

- [ ] Diferenciar `str`, `int`, `float` e `bool`.
- [ ] Identificar tipos usando `type()`.
- [ ] Entender a diferença entre texto e número.
- [ ] Realizar conversões com `str()`, `int()`, `float()` e `bool()`.
- [ ] Reconhecer erros comuns de conversão.
- [ ] Formatar números com f-strings.

**Próximo tópico:** Entrada e Saída de Dados.