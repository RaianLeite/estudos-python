# 09 — Strings em Python (`str`)

## 1. O que são Strings?

Strings são sequências de caracteres utilizadas para representar textos em Python.

Podem conter:

- Letras.
- Números.
- Espaços.
- Símbolos.
- Caracteres especiais.

Em Python, o tipo utilizado para representar textos é `str`.

### Exemplo

```python
nome = "Raian"
cidade = "Santa Luzia"
mensagem = "Estou estudando Python!"

print(nome)
print(cidade)
print(mensagem)

print(type(nome))
```

**Saída:**

```text
Raian
Santa Luzia
Estou estudando Python!
<class 'str'>
```

---

## 2. Declaração de Strings

Em Python, podemos declarar strings utilizando aspas simples ou aspas duplas.

### Aspas simples

```python
nome = 'Python'
print(nome)
```

### Aspas duplas

```python
nome = "Python"
print(nome)
```

As duas formas funcionam da mesma maneira.

### Quando utilizar cada uma?

Podemos escolher a forma que facilita a escrita do texto.

```python
mensagem = "Estou estudando Python."
frase = 'O professor disse: "Estude todos os dias."'
```

Se precisarmos utilizar aspas simples dentro de uma string delimitada por aspas simples, podemos utilizar uma barra invertida (`\`) para escapar o caractere.

```python
frase = 'Estou estudando \'Python\'.'

print(frase)
```

**Saída:**

```text
Estou estudando 'Python'.
```

---

## 3. Concatenação de Strings

A concatenação consiste em unir duas ou mais strings utilizando o operador `+`.

### Exemplo

```python
nome = "Raian"
sobrenome = "Leite"

nome_completo = nome + " " + sobrenome

print(nome_completo)
```

**Saída:**

```text
Raian Leite
```

### Concatenação com variáveis

```python
produto = "Notebook"
marca = "Dell"

descricao = "Produto: " + produto + " | Marca: " + marca

print(descricao)
```

**Saída:**

```text
Produto: Notebook | Marca: Dell
```

### Atenção

Não podemos concatenar diretamente uma string com um número de outro tipo.

```python
idade = 23

mensagem = "Minha idade é " + idade
```

Esse código gera um `TypeError`.

Para corrigir, podemos converter o número utilizando `str()`:

```python
idade = 23

mensagem = "Minha idade é " + str(idade)

print(mensagem)
```

Outra alternativa é utilizar f-strings, que veremos mais adiante.

---

## 4. Repetição de Strings

O operador `*` permite repetir uma string determinada quantidade de vezes.

### Exemplo

```python
texto = "Python "

resultado = texto * 3

print(resultado)
```

**Saída:**

```text
Python Python Python
```

### Outro exemplo

```python
linha = "-" * 30

print(linha)
print("MENU PRINCIPAL")
print(linha)
```

**Saída:**

```text
------------------------------
MENU PRINCIPAL
------------------------------
```

---

## 5. Índices de Strings

Cada caractere de uma string possui uma posição, chamada de índice.

Em Python, os índices começam em zero.

### Exemplo

```python
linguagem = "PYTHON"
```

| Caractere | P | Y | T | H | O | N |
|---|---|---|---|---|---|---|
| Índice | 0 | 1 | 2 | 3 | 4 | 5 |

### Acessando caracteres

Podemos acessar um caractere específico utilizando colchetes `[]`.

```python
linguagem = "PYTHON"

print(linguagem[0])
print(linguagem[1])
print(linguagem[5])
```

**Saída:**

```text
P
Y
N
```

### Índices negativos

Também podemos acessar os caracteres utilizando índices negativos.

Nesse caso, a contagem começa pelo último caractere.

| Caractere | P | Y | T | H | O | N |
|---|---|---|---|---|---|---|
| Índice positivo | 0 | 1 | 2 | 3 | 4 | 5 |
| Índice negativo | -6 | -5 | -4 | -3 | -2 | -1 |

### Exemplo

```python
linguagem = "PYTHON"

print(linguagem[-1])
print(linguagem[-2])
```

**Saída:**

```text
N
O
```

### Atenção

Tentar acessar um índice inexistente gera um `IndexError`.

```python
linguagem = "PYTHON"

print(linguagem[10])
```

---

## 6. Fatiamento de Strings (Slicing)

O fatiamento permite extrair partes de uma string.

A estrutura básica é:

```python
texto[inicio:fim:passo]
```

- `inicio`: posição onde começa o fatiamento.
- `fim`: posição onde termina, sem incluir o caractere dessa posição.
- `passo`: intervalo entre os caracteres selecionados.

### Exemplo 1 — Extraindo parte do texto

```python
linguagem = "PYTHON"

print(linguagem[0:3])
```

**Saída:**

```text
PYT
```

O índice 3 não é incluído.

### Exemplo 2 — Omitindo o início

```python
linguagem = "PYTHON"

print(linguagem[:3])
```

**Saída:**

```text
PYT
```

Quando o início é omitido, o Python começa pelo primeiro caractere.

### Exemplo 3 — Omitindo o final

```python
linguagem = "PYTHON"

print(linguagem[3:])
```

**Saída:**

```text
HON
```

Quando o final é omitido, o Python percorre até o último caractere.

### Exemplo 4 — Utilizando índices negativos

```python
linguagem = "PYTHON"

print(linguagem[-3:])
```

**Saída:**

```text
HON
```

### Exemplo 5 — Utilizando passo

```python
numero = "123456789"

print(numero[::2])
```

**Saída:**

```text
13579
```

O passo `2` faz com que o Python selecione um caractere e pule o próximo.

### Exemplo 6 — Invertendo uma String

```python
linguagem = "PYTHON"

print(linguagem[::-1])
```

**Saída:**

```text
NOHTYP
```

O passo `-1` percorre a string de trás para frente.

---

## 7. Tamanho de uma String — `len()`

A função `len()` retorna a quantidade de caracteres de uma string.

Os espaços também são contabilizados.

### Exemplo

```python
nome = "Python"

print(len(nome))
```

**Saída:**

```text
6
```

### Exemplo com espaços

```python
mensagem = "Olá Mundo"

print(len(mensagem))
```

**Saída:**

```text
9
```

A contagem inclui o espaço entre as palavras.

---

## 8. Métodos de Strings

Python possui diversos métodos que permitem modificar a apresentação ou verificar o conteúdo de uma string.

Um método é uma funcionalidade que podemos utilizar a partir de um objeto.

### 8.1 — `upper()`

Converte todos os caracteres alfabéticos para letras maiúsculas.

```python
nome = "raian leite"

print(nome.upper())
```

**Saída:**

```text
RAIAN LEITE
```

### 8.2 — `lower()`

Converte todos os caracteres alfabéticos para letras minúsculas.

```python
nome = "RAIAN LEITE"

print(nome.lower())
```

**Saída:**

```text
raian leite
```

### 8.3 — `capitalize()`

Converte a primeira letra da string para maiúscula e as demais para minúsculas.

```python
nome = "rAIAN LEITE"

print(nome.capitalize())
```

**Saída:**

```text
Raian leite
```

### 8.4 — `title()`

Converte a primeira letra de cada palavra para maiúscula.

```python
nome = "raian leite"

print(nome.title())
```

**Saída:**

```text
Raian Leite
```

### 8.5 — `strip()`

Remove espaços em branco do início e do final da string.

```python
nome = "   Raian Leite   "

print(nome.strip())
```

**Saída:**

```text
Raian Leite
```

Também existem:

- `lstrip()`: remove espaços do início.
- `rstrip()`: remove espaços do final.

### 8.6 — `replace()`

Substitui uma parte da string por outra.

Estrutura:

```python
texto.replace("texto_antigo", "texto_novo")
```

Exemplo:

```python
frase = "Eu gosto de Java"

nova_frase = frase.replace("Java", "Python")

print(nova_frase)
```

**Saída:**

```text
Eu gosto de Python
```

O método `replace()` retorna uma nova string, não altera a string original.

### 8.7 — `find()`

Procura uma sequência de caracteres e retorna a posição da primeira ocorrência.

```python
frase = "Estou estudando Python"

print(frase.find("Python"))
```

**Saída:**

```text
17
```

Se o texto não for encontrado, retorna `-1`.

```python
frase = "Estou estudando Python"

print(frase.find("Java"))
```

**Saída:**

```text
-1
```

### 8.8 — `count()`

Conta quantas vezes uma sequência aparece na string.

```python
frase = "Python é muito bom. Python é interessante."

print(frase.count("Python"))
```

**Saída:**

```text
2
```

### 8.9 — `startswith()`

Verifica se a string começa com determinado conteúdo.

Retorna `True` ou `False`.

```python
linguagem = "Python"

print(linguagem.startswith("Py"))
print(linguagem.startswith("Ja"))
```

**Saída:**

```text
True
False
```

### 8.10 — `endswith()`

Verifica se a string termina com determinado conteúdo.

```python
arquivo = "documento.pdf"

print(arquivo.endswith(".pdf"))
print(arquivo.endswith(".txt"))
```

**Saída:**

```text
True
False
```

---

## 9. Verificação de conteúdo em Strings

Podemos verificar se determinado conteúdo existe dentro de uma string utilizando o operador `in`.

### Exemplo

```python
frase = "Estou estudando Python"

print("Python" in frase)
print("Java" in frase)
```

**Saída:**

```text
True
False
```

Também podemos utilizar `not in` para verificar se um conteúdo não existe.

```python
frase = "Estou estudando Python"

print("Java" not in frase)
```

**Saída:**

```text
True
```

A comparação diferencia letras maiúsculas de minúsculas.

```python
frase = "Python"

print("python" in frase)
```

**Saída:**

```text
False
```

---

## 10. Formatação de Strings com f-strings

As f-strings permitem inserir variáveis e expressões diretamente dentro de textos.

Para utilizá-las, colocamos a letra `f` antes das aspas e inserimos as variáveis entre chaves `{}`.

### Exemplo

```python
nome = "Raian"
idade = 23

print(f"Meu nome é {nome} e tenho {idade} anos.")
```

**Saída:**

```text
Meu nome é Raian e tenho 23 anos.
```

### Exemplo com operações matemáticas

```python
numero1 = 10
numero2 = 5

print(f"A soma é {numero1 + numero2}")
```

**Saída:**

```text
A soma é 15
```

### Formatação de casas decimais

Podemos definir quantas casas decimais queremos exibir.

```python
preco = 19.9

print(f"Preço: R$ {preco:.2f}")
```

**Saída:**

```text
Preço: R$ 19.90
```

### Alinhamento de texto

Também podemos utilizar f-strings para alinhar informações.

```python
nome = "Python"

print(f"|{nome:<15}|")
print(f"|{nome:>15}|")
print(f"|{nome:^15}|")
```

**Saída:**

```text
|Python         |
|         Python|
|     Python    |
```

- `<`: alinha à esquerda.
- `>`: alinha à direita.
- `^`: centraliza.

---

## 11. Imutabilidade das Strings

Strings em Python são imutáveis.

Isso significa que não podemos alterar diretamente um caractere de uma string depois que ela foi criada.

### Exemplo incorreto

```python
linguagem = "Python"

linguagem[0] = "J"
```

Esse código gera um `TypeError`.

### Como fazer corretamente?

Podemos criar uma nova string com o conteúdo desejado.

```python
linguagem = "Python"

nova_linguagem = "J" + linguagem[1:]

print(nova_linguagem)
```

**Saída:**

```text
Jython
```

A variável original continua armazenando `"Python"`.

---

## 12. Resumo das principais funcionalidades

| Função ou método | Finalidade |
|---|---|
| `str()` | Converte um valor para texto |
| `len()` | Retorna a quantidade de caracteres |
| `upper()` | Converte para maiúsculas |
| `lower()` | Converte para minúsculas |
| `capitalize()` | Coloca a primeira letra em maiúscula |
| `title()` | Coloca a primeira letra de cada palavra em maiúscula |
| `strip()` | Remove espaços das extremidades |
| `lstrip()` | Remove espaços do início |
| `rstrip()` | Remove espaços do final |
| `replace()` | Substitui partes de uma string |
| `find()` | Localiza a posição de um conteúdo |
| `count()` | Conta ocorrências |
| `startswith()` | Verifica o início da string |
| `endswith()` | Verifica o final da string |
| `in` | Verifica se um conteúdo existe |
| `not in` | Verifica se um conteúdo não existe |
| `f-string` | Formata textos com variáveis e expressões |

---

## 13. Observações importantes

1. Strings podem ser declaradas com aspas simples ou duplas.
2. Os índices começam em zero.
3. Índices negativos começam pelo último caractere.
4. No slicing, o índice final não é incluído.
5. A função `len()` também conta espaços.
6. Métodos como `upper()`, `lower()` e `replace()` não modificam a string original.
7. Strings são imutáveis.
8. Python diferencia letras maiúsculas de minúsculas.
9. `input()` retorna uma string.
10. F-strings facilitam a apresentação de informações.

---

## 14. Checklist de aprendizado

- [ ] Entendo o que são Strings.
- [ ] Sei declarar strings com aspas simples e duplas.
- [ ] Consigo concatenar strings.
- [ ] Sei repetir strings utilizando `*`.
- [ ] Entendo índices positivos e negativos.
- [ ] Consigo utilizar slicing.
- [ ] Sei utilizar `len()`.
- [ ] Conheço os métodos `upper()`, `lower()`, `capitalize()` e `title()`.
- [ ] Sei utilizar `strip()` e `replace()`.
- [ ] Entendo a utilização de `find()` e `count()`.
- [ ] Consigo verificar conteúdos com `in` e `not in`.
- [ ] Sei formatar textos utilizando f-strings.
- [ ] Entendo que Strings são imutáveis.

**Critério para avançar:** conseguir utilizar os principais métodos e operações de Strings sem consultar constantemente a teoria.

---

# 15 — Exercícios Práticos de Strings

Resolva os exercícios no arquivo `main.py`, sem copiar diretamente os exemplos da teoria.

## Exercício 1 — Declaração de Strings

Crie três variáveis:

- `nome`
- `cidade`
- `linguagem`

Armazene um texto em cada uma e exiba os valores e seus respectivos tipos utilizando `type()`.

## Exercício 2 — Concatenação

Solicite ao usuário seu nome e sobrenome.

Concatene os dois valores e exiba o nome completo.

Exemplo de saída:

```text
Digite seu nome: Raian
Digite seu sobrenome: Leite

Nome completo: Raian Leite
```

## Exercício 3 — Repetição de Strings

Solicite ao usuário uma palavra e exiba essa palavra cinco vezes utilizando o operador `*`.

## Exercício 4 — Índices

Considere a seguinte variável:

```python
linguagem = "PYTHON"
```

Exiba separadamente:

1. O primeiro caractere.
2. O terceiro caractere.
3. O último caractere.
4. O penúltimo caractere.

Utilize índices positivos e negativos.

## Exercício 5 — Fatiamento (Slicing)

Considere:

```python
frase = "ESTOU ESTUDANDO PYTHON"
```

Exiba:

1. Os cinco primeiros caracteres.
2. Os caracteres a partir da posição 6.
3. Apenas a palavra `PYTHON`.
4. A frase invertida.

## Exercício 6 — Tamanho de uma String

Solicite ao usuário uma frase e exiba:

- A frase digitada.
- A quantidade total de caracteres utilizando `len()`.

Lembre-se de que os espaços também são contabilizados.

## Exercício 7 — Maiúsculas e Minúsculas

Solicite ao usuário seu nome completo.

Exiba o nome nas seguintes formas:

1. Todas as letras maiúsculas.
2. Todas as letras minúsculas.
3. Primeira letra maiúscula.
4. Primeira letra de cada palavra maiúscula.

Utilize `upper()`, `lower()`, `capitalize()` e `title()`.

## Exercício 8 — Removendo Espaços

Solicite ao usuário que digite seu nome com espaços antes e depois.

Exiba:

1. O nome original.
2. O nome utilizando `strip()`.
3. O nome utilizando `lstrip()`.
4. O nome utilizando `rstrip()`.

## Exercício 9 — Substituição de Texto

Considere:

```python
frase = "Estou estudando Java"
```

Utilize `replace()` para substituir `Java` por `Python`.

Exiba a frase original e a nova frase.

## Exercício 10 — Busca de Texto

Considere:

```python
frase = "Python é uma linguagem poderosa. Python é muito utilizado."
```

Utilize `find()` para encontrar a posição da primeira ocorrência da palavra `Python`.

Depois, utilize `count()` para descobrir quantas vezes a palavra aparece.

## Exercício 11 — Verificação de Conteúdo

Solicite ao usuário uma frase.

Verifique se a palavra `Python` está presente utilizando o operador `in`.

Exiba o resultado.

**Desafio adicional:** faça a verificação funcionar mesmo que o usuário digite `python`, `PYTHON` ou `Python`.

Dica: utilize `lower()`.

## Exercício 12 — Verificando Extensões

Solicite ao usuário o nome de um arquivo.

Utilize `endswith()` para verificar se o arquivo termina com `.pdf`.

Exiba `True` ou `False`.

## Exercício 13 — Formatação com f-strings

Solicite ao usuário:

- Nome.
- Idade.
- Altura.

Exiba uma mensagem utilizando f-string, formatando a altura com duas casas decimais.

Exemplo:

```text
Meu nome é Raian, tenho 23 anos e minha altura é 1.83 metros.
```

## Exercício 14 — Desafio: Analisador de Texto

Crie um programa que solicite uma frase ao usuário.

O programa deverá exibir:

1. A frase original.
2. A frase em letras maiúsculas.
3. A frase em letras minúsculas.
4. A quantidade de caracteres.
5. A quantidade de espaços.
6. A quantidade de vezes que a letra `a` aparece.
7. A frase invertida.

Utilize os métodos e funções estudados nesta aula.

---