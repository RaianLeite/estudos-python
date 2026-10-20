# 03 — Primeiro Programa em Python

## 1. O que é um programa?

Um programa é um conjunto de instruções que o computador executa para realizar uma tarefa.

Em Python, escrevemos essas instruções em arquivos com a extensão `.py`.

Exemplos de tarefas que podem ser realizadas com Python:
- Exibir mensagens na tela.
- Realizar cálculos.
- Processar informações.
- Automatizar tarefas repetitivas.
- Consultar e manipular dados.

## 2. Criando o primeiro programa

No VS Code, abra a pasta do seu projeto `Python-Dev`.

Crie o arquivo `main.py` dentro da pasta `03-Primeiro-Programa`.

Digite o seguinte código:

```python
print("Olá, mundo!")
```

Salve o arquivo e execute-o pelo botão **Run Python File** do VS Code ou pelo terminal integrado:

```powershell
python main.py
```

Resultado esperado:

```text
Olá, mundo!
```

## 3. Entendendo a função `print()`

A função `print()` é utilizada para exibir informações no terminal.

Exemplo:

```python
print("Estou aprendendo Python")
print("Este é meu primeiro programa")
print(10)
print(5 + 3)
```

Saída:

```text
Estou aprendendo Python
Este é meu primeiro programa
10
8
```

Observe que o Python consegue exibir textos, números e resultados de cálculos.

## 4. Textos e números

Em Python, textos são chamados de *strings* e geralmente são escritos entre aspas simples ou duplas.

```python
print("Python")
print('Estou estudando programação')
print(25)
print(10 + 5)
```

Os textos ficam entre aspas. Os números podem ser escritos diretamente, sem aspas.

Compare:

```python
print(10 + 5)
print("10 + 5")
```

Resultado:

```text
15
10 + 5
```

No primeiro caso, o Python realiza uma soma. No segundo, exibe o conteúdo como texto.

## 5. Exibindo várias informações

É possível passar várias informações para a mesma função `print()`, separando-as por vírgulas.

```python
print("Nome:", "Carlos")
print("Idade:", 25)
print("Resultado:", 10 + 5)
```

Saída:

```text
Nome: Carlos
Idade: 25
Resultado: 15
```

Por padrão, a função `print()` separa os argumentos com um espaço.

## 6. Comentários no código

Comentários são trechos escritos para explicar o código. Eles não são executados pelo Python.

Utilizamos o caractere `#` para criar um comentário de uma linha.

```python
# Este é meu primeiro programa
print("Olá, mundo!")

# Exibindo um cálculo
print(10 + 5)
```

Comentários podem ajudar a documentar regras de negócio, explicar cálculos e facilitar a manutenção do código.

Evite comentários desnecessários que apenas repetem o que a instrução já deixa claro.

## 7. Quebras de linha

Cada chamada de `print()` normalmente exibe o resultado em uma nova linha.

```python
print("Primeira linha")
print("Segunda linha")
print("Terceira linha")
```

Saída:

```text
Primeira linha
Segunda linha
Terceira linha
```

Também podemos utilizar `\n` dentro de uma string para inserir uma quebra de linha.

```python
print("Primeira linha\nSegunda linha")
```

Saída:

```text
Primeira linha
Segunda linha
```

## 8. Erros comuns

### Esquecer as aspas

Código incorreto:

```python
print(Olá, mundo!)
```

O Python não interpreta esse texto como uma string válida.

Código correto:

```python
print("Olá, mundo!")
```

### Esquecer um parêntese

Código incorreto:

```python
print("Olá, mundo!"
```

Código correto:

```python
print("Olá, mundo!")
```

### Executar o arquivo errado

Confira se o terminal está na pasta correta e se o comando corresponde ao nome do arquivo.

```powershell
python main.py
```

### Salvar o arquivo antes de executar

Se você alterar o código, salve o arquivo para garantir que está executando a versão atualizada.

## 9. Boas práticas

- Utilize nomes de arquivos claros, como `main.py`.
- Organize seus estudos em pastas por assunto.
- Use comentários quando ajudarem a explicar o código.
- Mantenha a indentação consistente.
- Leia as mensagens de erro com atenção.
- Execute o código frequentemente para verificar seu funcionamento.
- Pratique escrevendo os exemplos, em vez de apenas copiá-los.

## 10. Exercícios de fixação

### Exercício 1 — Apresentação

Crie um programa que exiba seu nome, sua área de estudo e o motivo pelo qual deseja aprender Python.

### Exercício 2 — Mensagens

Exiba três mensagens diferentes, cada uma em uma linha.

### Exercício 3 — Cálculos

Utilize `print()` para exibir o resultado das seguintes operações:

- 15 + 7
- 20 - 8
- 6 * 4
- 20 / 5

### Exercício 4 — Comentários

Adicione comentários ao código explicando o objetivo de cada operação.

### Exercício 5 — Texto versus cálculo

Escreva um programa que exiba:

- O resultado de `8 + 2` como cálculo.
- A expressão `"8 + 2"` como texto.

Observe a diferença entre os resultados.

## 11. Revisão

Ao concluir este tópico, você deverá saber:

- [ ] Criar um arquivo `.py`.
- [ ] Executar um programa pelo VS Code.
- [ ] Utilizar a função `print()`.
- [ ] Diferenciar textos de números.
- [ ] Exibir cálculos na tela.
- [ ] Escrever comentários com `#`.
- [ ] Reconhecer e corrigir erros simples.

**Próximo tópico:** Variáveis e Constantes.