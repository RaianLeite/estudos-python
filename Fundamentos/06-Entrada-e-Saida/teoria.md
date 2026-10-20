# 06 — Entrada e Saída de Dados em Python

## 1. O que são entrada e saída de dados?

Em um programa, entrada e saída são formas de comunicação entre o usuário e o computador.

- **Entrada:** informações fornecidas ao programa.
- **Processamento:** operações realizadas com essas informações.
- **Saída:** resultados apresentados pelo programa.

Exemplo de um programa que calcula a soma de dois números:

1. O usuário informa dois números.
2. O Python soma os valores.
3. O programa exibe o resultado.

Esse fluxo é a base de muitos programas, como calculadoras, sistemas de cadastro e ferramentas de automação.

## 2. Exibindo informações com `print()`

Você já conhece a função `print()`. Ela é utilizada para exibir informações no terminal.

```python
print("Bem-vindo ao Python!")
print("Vamos aprender a programar.")
print(10 + 5)
```

Saída:

```text
Bem-vindo ao Python!
Vamos aprender a programar.
15
```

Também podemos exibir variáveis:

```python
nome = "Raian"
print(nome)
```

Saída:

```text
Raian
```

## 3. Recebendo informações com `input()`

A função `input()` permite receber informações digitadas pelo usuário.

Exemplo:

```python
nome = input("Digite seu nome: ")

print(f"Olá, {nome}!")
```

Quando você executar esse código, o terminal exibirá:

```text
Digite seu nome:
```

Digite seu nome e pressione Enter. Se você digitar `Raian`, a saída será:

```text
Olá, Raian!
```

Entenda cada parte:

- `input()` solicita uma informação.
- `"Digite seu nome: "` é a mensagem apresentada ao usuário.
- `nome =` armazena o texto digitado na variável `nome`.
- `print()` exibe a mensagem de boas-vindas.

**Importante:** `input()` sempre retorna uma string (`str`), mesmo quando o usuário digita números.

## 4. O problema de realizar cálculos com `input()`

Imagine o seguinte programa:

```python
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

print(numero1 + numero2)
```

Se o usuário digitar `10` e depois `5`, o resultado será:

```text
105
```

Por quê?

Porque `input()` retorna textos. Nesse caso, o Python concatena `"10"` com `"5"`, em vez de realizar uma soma numérica.

Para realizar cálculos, precisamos converter os valores para um tipo numérico.

## 5. Convertendo entradas com `int()` e `float()`

### Recebendo números inteiros

Utilize `int()` quando quiser receber um número inteiro.

```python
idade = int(input("Digite sua idade: "))

print(f"Você tem {idade} anos.")
```

Se o usuário digitar `23`, a variável `idade` armazenará o inteiro `23`.

Podemos confirmar com:

```python
print(type(idade))
```

Saída:

```text
<class 'int'>
```

### Recebendo números decimais

Utilize `float()` quando quiser receber um número decimal.

```python
altura = float(input("Digite sua altura: "))

print(f"Sua altura é {altura:.2f} metros.")
```

Se o usuário digitar `1.83`, a saída será:

```text
Sua altura é 1.83 metros.
```

**Atenção:** por padrão, o Python utiliza ponto como separador decimal. Para esse exemplo, digite `1.83`, e não `1,83`.

### Calculando a soma de dois números

```python
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = numero1 + numero2

print(f"A soma é: {resultado}")
```

Exemplo de execução:

```text
Digite o primeiro número: 10
Digite o segundo número: 5
A soma é: 15
```

Agora o programa realiza uma soma numérica de verdade.

## 6. Recebendo diferentes tipos de dados

Podemos combinar entradas de texto, números inteiros e números decimais.

```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura:.2f} metros")
```

Nesse programa:

- `nome` é `str`.
- `idade` é `int`.
- `altura` é `float`.

Escolher o tipo correto permite utilizar os valores nas operações apropriadas.

## 7. Criando uma calculadora simples

Vamos criar um programa que recebe dois números e exibe os resultados das principais operações matemáticas.

```python
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

print(f"Soma: {soma:.2f}")
print(f"Subtração: {subtracao:.2f}")
print(f"Multiplicação: {multiplicacao:.2f}")

if numero2 != 0:
    divisao = numero1 / numero2
    print(f"Divisão: {divisao:.2f}")
else:
    print("Não é possível dividir por zero.")
```

O programa utiliza `float()` para aceitar números decimais e calcula quatro operações.

A condição `if numero2 != 0` verifica se o divisor é diferente de zero. O objetivo é evitar uma tentativa de divisão por zero.

Estudaremos as estruturas condicionais com mais detalhes em um tópico posterior.

## 8. Erros comuns com `input()`

### Erro 1 — Esquecer a conversão numérica

Código:

```python
idade = input("Digite sua idade: ")
print(idade + 1)
```

Esse código gera um `TypeError`, porque tenta somar uma string com um inteiro.

Correção:

```python
idade = int(input("Digite sua idade: "))
print(idade + 1)
```

### Erro 2 — Digitar um valor incompatível

Código:

```python
idade = int(input("Digite sua idade: "))
```

Se o usuário digitar `vinte`, o Python não conseguirá converter esse texto diretamente para inteiro e lançará um `ValueError`.

Para os primeiros exercícios, digite números válidos. Mais adiante, aprenderemos a tratar entradas incorretas com `try` e `except`.

### Erro 3 — Utilizar vírgula como separador decimal

Para este código:

```python
altura = float(input("Digite sua altura: "))
```

Digite `1.83`, e não `1,83`. A vírgula não é aceita nesse formato padrão de conversão.

## 9. Boas práticas

- Apresente mensagens claras para orientar o usuário.
- Utilize nomes de variáveis que indiquem o conteúdo armazenado.
- Converta a entrada para o tipo adequado antes de realizar cálculos.
- Utilize f-strings para exibir valores de forma organizada.
- Considere situações inválidas, como divisão por zero.
- Teste o programa com diferentes valores.
- Leia as mensagens de erro para identificar o que precisa ser corrigido.

## 10. Exercícios de fixação

### Exercício 1 — Saudação personalizada

Crie um programa que solicite o nome do usuário e exiba:

`Olá, [nome]! Seja bem-vindo ao Python.`

Utilize `input()` e `print()`.

### Exercício 2 — Soma de dois números

Solicite dois números inteiros ao usuário, converta-os com `int()` e exiba a soma.

Teste com os valores `10` e `5`. O resultado esperado é `15`.

### Exercício 3 — Calculando a idade

Solicite o ano de nascimento do usuário e o ano atual. Calcule a diferença entre os dois valores e exiba a idade aproximada.

Observação: esse cálculo não considera se a pessoa já fez aniversário no ano atual.

### Exercício 4 — Calculando o preço final

Solicite o nome de um produto, seu preço e o valor do desconto. Calcule o preço final e exiba os valores com duas casas decimais.

Utilize `input()`, `float()` e f-strings.

### Exercício 5 — Conversão de medidas

Solicite uma altura em metros e exiba o valor convertido para centímetros.

Dica: multiplique a altura por `100`.

Exemplo: `1.75` metro corresponde a `175.00` centímetros.

### Exercício 6 — Calculadora de média

Solicite três notas ao usuário, calcule a média aritmética e exiba o resultado com duas casas decimais.

Fórmula:

```text
média = (nota1 + nota2 + nota3) / 3
```

## 11. Revisão

Ao concluir este tópico, você deverá saber:

- [ ] Exibir informações com `print()`.
- [ ] Receber dados com `input()`.
- [ ] Entender por que `input()` retorna `str`.
- [ ] Converter entradas com `int()` e `float()`.
- [ ] Utilizar dados fornecidos pelo usuário em cálculos.
- [ ] Exibir resultados usando f-strings.
- [ ] Reconhecer erros comuns de entrada e conversão.

**Próximo tópico:** Operadores em Python.