# 04 — Variáveis e Constantes em Python

## 1. O que são variáveis?

Uma variável é um nome utilizado para armazenar e acessar um valor durante a execução de um programa.

Imagine que você queira guardar seu nome, sua idade e seu salário. Em vez de escrever essas informações repetidamente, você pode armazená-las em variáveis.

Exemplo:

```python
nome = "Raian Leite"
idade = 23
altura = 1.83
```

Nesse exemplo, criamos três variáveis:

- `nome`: armazena um texto.
- `idade`: armazena um número inteiro.
- `altura`: armazena um número decimal.

O operador `=` é utilizado para atribuir um valor a uma variável.

**Importante:** em Python, o sinal `=` significa atribuição, não uma comparação de igualdade matemática.

## 2. Criando e utilizando variáveis

Veja um exemplo completo:

```python
nome = "Raian Leite"
idade = 23

print(nome)
print(idade)
```

Saída:

```text
Raian Leite
23
```

Você também pode utilizar as variáveis dentro de mensagens:

```python
nome = "Raian Leite"
idade = 23

print("Nome:", nome)
print("Idade:", idade)
```

Saída:

```text
Nome: Raian Leite
Idade: 23
```

Observe que podemos reutilizar o mesmo valor em diferentes partes do programa sem precisar digitá-lo novamente.

## 3. Alterando o valor de uma variável

Em Python, podemos atribuir um novo valor à mesma variável.

```python
idade = 23

print(idade)

idade = 24

print(idade)
```

Saída:

```text
23
24
```

Depois da segunda atribuição, a variável `idade` passa a armazenar o valor `24`.

Também podemos utilizar o valor anterior para calcular um novo valor:

```python
saldo = 100

saldo = saldo + 50

print(saldo)
```

Saída:

```text
150
```

A expressão `saldo = saldo + 50` significa: pegue o valor atual de `saldo`, some 50 e armazene o resultado novamente em `saldo`.

Uma forma abreviada de escrever essa operação é:

```python
saldo = 100
saldo += 50

print(saldo)
```

O resultado também será `150`.

## 4. Regras para nomear variáveis

Os nomes das variáveis precisam seguir algumas regras.

### Regras obrigatórias

- Podem conter letras, números e o caractere `_`.
- Não podem começar com um número.
- Não podem conter espaços.
- Não podem utilizar palavras reservadas do Python como nomes.
- Diferenciam letras maiúsculas de minúsculas.

Exemplos:

```python
nome_completo = "Raian Leite"
idade = 23
numero1 = 10
valor_total = 250.50
```

Exemplos de nomes inválidos:

```python
# nome completo = "Raian Leite"  # Contém espaço
# 1numero = 10                   # Começa com número
# class = "Python"               # Palavra reservada
```

Os exemplos inválidos estão comentados para que o arquivo continue executável.

### Convenção recomendada: snake_case

Em Python, recomenda-se utilizar `snake_case` para nomes de variáveis: palavras minúsculas separadas por sublinhados.

Prefira:

```python
nome_completo = "Raian Leite"
valor_produto = 49.90
quantidade_estoque = 15
```

Evite:

```python
nomeCompleto = "Raian Leite"
ValorProduto = 49.90
quantidadeestoque = 15
```

Os últimos exemplos podem funcionar, mas não seguem a convenção usual para variáveis em Python.

## 5. Tipos de valores nas variáveis

As variáveis podem armazenar valores de diferentes tipos.

```python
nome = "Raian"
idade = 23
altura = 1.83
estudando = True
```

| Tipo | Significado | Exemplo |
|---|---|---|
| `str` | Texto | `"Python"` |
| `int` | Número inteiro | `23` |
| `float` | Número decimal | `1.83` |
| `bool` | Verdadeiro ou falso | `True` |

Podemos descobrir o tipo de um valor utilizando `type()`:

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

Vamos estudar cada tipo com mais detalhes no próximo tópico sobre tipos de dados.

## 6. O que são constantes?

Uma constante representa um valor que, por convenção, não deve ser alterado durante a execução do programa.

Em Python, não existe uma palavra-chave que torne uma variável uma constante de forma nativa. Utilizamos uma convenção de escrita: nomes de constantes são escritos em letras maiúsculas, com palavras separadas por `_`.

Exemplo:

```python
TAXA_JUROS = 0.05
LIMITE_TENTATIVAS = 3
NOME_SISTEMA = "Controle de Estoque"
```

Por convenção, esses valores devem permanecer inalterados.

Diferentemente de algumas linguagens, Python não impede que você atribua outro valor a esses nomes:

```python
TAXA_JUROS = 0.05
TAXA_JUROS = 0.10
```

Esse código funciona, mas alterar uma constante contraria a convenção adotada.

### Quando utilizar constantes?

Utilize constantes para valores fixos que aparecem em diferentes partes do programa, como:

- Limites definidos por regras de negócio.
- Taxas e percentuais fixos.
- Configurações que não devem mudar durante a execução.
- Nomes ou códigos utilizados repetidamente.

**Atenção:** não confunda uma constante com um valor que pode mudar ao longo do programa. O saldo de uma conta, por exemplo, normalmente é uma variável.

## 7. Utilizando f-strings com variáveis

As f-strings permitem inserir variáveis diretamente em textos.

Exemplo:

```python
nome = "Raian"
idade = 23

print(f"Meu nome é {nome} e tenho {idade} anos.")
```

Saída:

```text
Meu nome é Raian e tenho 23 anos.
```

Também podemos realizar cálculos dentro das chaves:

```python
preco = 100
desconto = 15

print(f"Preço original: R$ {preco}")
print(f"Preço com desconto: R$ {preco - desconto}")
```

Saída:

```text
Preço original: R$ 100
Preço com desconto: R$ 85
```

As f-strings são muito úteis para montar mensagens, relatórios e resultados de cálculos.

## 8. Exemplo prático

Vamos criar um pequeno programa para calcular o preço de um produto após um desconto.

```python
nome_produto = "Teclado"
preco = 150.00
desconto = 20.00

preco_final = preco - desconto

print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
```

Saída:

```text
Produto: Teclado
Preço original: R$ 150.00
Desconto: R$ 20.00
Preço final: R$ 130.00
```

O trecho `:.2f` faz com que o número seja exibido com duas casas decimais.

Nesse exemplo, utilizamos variáveis para armazenar os dados, uma operação matemática para calcular o preço final e f-strings para exibir os resultados.

## 9. Boas práticas

- Escolha nomes que indiquem claramente o que a variável armazena.
- Utilize `snake_case` para variáveis.
- Utilize letras maiúsculas para constantes por convenção.
- Evite nomes genéricos como `x`, `a` ou `valor1` quando um nome mais descritivo for possível.
- Evite alterar uma variável sem necessidade.
- Não utilize nomes de palavras reservadas do Python.
- Prefira código simples, legível e organizado.

## 10. Exercícios de fixação

### Exercício 1 — Dados pessoais

Crie variáveis para armazenar:

- Seu nome.
- Sua idade.
- Sua altura.
- Se você está estudando Python (`True` ou `False`).

Depois, exiba todas as informações utilizando `print()`.

### Exercício 2 — Alterando variáveis

Crie uma variável chamada `saldo` com o valor `100`.

Em seguida:

1. Exiba o saldo.
2. Adicione `50` ao saldo.
3. Exiba o novo saldo.
4. Subtraia `30` do saldo.
5. Exiba o saldo final.

### Exercício 3 — Cálculo de produto

Crie as seguintes variáveis:

- `nome_produto`: `"Mouse"`.
- `preco`: `80.00`.
- `desconto`: `10.00`.

Calcule o preço final e exiba o nome do produto, o preço original, o desconto e o preço final.

Utilize f-strings para montar as mensagens.

### Exercício 4 — Constantes

Crie duas constantes:

- `TAXA_IMPOSTO = 0.10`
- `PRECO_PRODUTO = 200.00`

Calcule o valor do imposto e exiba o resultado.

Dica: multiplique o preço pela taxa de imposto.

### Exercício 5 — Previsão de resultados

Sem executar o código, escreva qual será a saída:

```python
numero = 10
numero = numero + 5

print(numero)

numero += 2

print(numero)
```

### Exercício 6 — Identificando nomes válidos

Indique quais nomes são válidos para variáveis em Python:

- `nome_completo`
- `2valor`
- `idade`
- `valor-total`
- `NOME_SISTEMA`
- `class`

Explique brevemente por que os nomes inválidos não podem ser utilizados.

## 11. Revisão

Ao concluir este tópico, você deverá saber:

- [ ] Criar e utilizar variáveis.
- [ ] Alterar valores armazenados.
- [ ] Utilizar operadores de atribuição, como `+=`.
- [ ] Escolher nomes válidos e legíveis.
- [ ] Identificar os tipos básicos de valores.
- [ ] Entender a convenção de constantes em Python.
- [ ] Utilizar f-strings com variáveis.
- [ ] Realizar cálculos com valores armazenados.

**Próximo tópico:** Tipos de Dados.