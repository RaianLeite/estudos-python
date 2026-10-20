# 02 — Instalação e Ambiente de Desenvolvimento

## 1. O que é um ambiente de desenvolvimento?

Um ambiente de desenvolvimento é o conjunto de ferramentas utilizadas para escrever, executar, testar e depurar programas.

Para desenvolver em Python, os principais componentes são:

- **Python:** linguagem e ambiente de execução.
- **Interpretador:** executa o código Python.
- **Editor de código:** permite escrever e editar programas.
- **Terminal:** permite executar comandos e programas.
- **Extensões:** adicionam recursos ao editor, como execução e depuração de código.

## 2. Instalando o Python

No Windows, o Python pode ser obtido no site oficial:

https://www.python.org/downloads/

Baixe uma versão estável compatível com seus projetos.

Durante a instalação, confira se a opção de adicionar o Python ao PATH está disponível e habilite-a quando apropriado.

### O que é o PATH?

O PATH é uma variável de ambiente do sistema operacional que contém diretórios nos quais o terminal procura programas executáveis.

Quando o Python está corretamente configurado no PATH, é possível executá-lo pelo terminal sem informar o caminho completo do executável.

## 3. Verificando a instalação

Abra o terminal do Windows ou o terminal integrado do VS Code e execute:

```powershell
python --version
```

Se esse comando não funcionar, tente:

```powershell
py --version
```

Os comandos devem exibir a versão instalada, por exemplo:

```text
Python 3.x.x
```

Para descobrir qual executável está sendo utilizado no Windows, use:

```powershell
where.exe python
```

Para verificar o inicializador do Python:

```powershell
where.exe py
```

## 4. Instalando o Visual Studio Code

O Visual Studio Code (VS Code) é um editor de código que oferece recursos para desenvolver em várias linguagens.

Site oficial:

https://code.visualstudio.com/

Após instalar o editor, abra a seção Extensions e procure a extensão oficial **Python**, publicada pela Microsoft.

A extensão oferece recursos como:

- Realce de sintaxe.
- Autocompletar código.
- Depuração.
- Seleção de interpretador.
- Integração com ambientes virtuais.

Importante: a extensão Python do VS Code não substitui a instalação do interpretador Python.

## 5. Criando o primeiro projeto

Crie uma pasta para o projeto e abra-a no VS Code.

Exemplo de estrutura:

```text
meu-primeiro-projeto/
├── main.py
└── README.md
```

O arquivo `main.py` será o ponto de entrada do programa.

Conteúdo:

```python
print("Olá, mundo!")
```

Salve o arquivo antes de executá-lo.

## 6. Executando um programa

Abra o terminal integrado do VS Code pelo menu Terminal > New Terminal.

Navegue até a pasta do projeto, caso ainda não esteja nela, e execute:

```powershell
python main.py
```

Saída esperada:

```text
Olá, mundo!
```

Se o comando `python` não funcionar, tente `py main.py`.

## 7. O que é o terminal?

O terminal é uma interface de texto usada para executar comandos e interagir com o sistema operacional.

Comandos úteis no PowerShell:

```powershell
# Exibir a pasta atual
Get-Location

# Listar arquivos e pastas
Get-ChildItem

# Entrar em uma pasta
Set-Location nome-da-pasta

# Voltar para a pasta anterior
Set-Location ..
```

O terminal também é utilizado para executar programas, instalar bibliotecas e gerenciar ambientes virtuais.

## 8. O que é um ambiente virtual?

Um ambiente virtual permite manter as bibliotecas e dependências de um projeto separadas das de outros projetos.

Isso evita conflitos entre versões de pacotes.

Para criar um ambiente virtual dentro do projeto:

```powershell
python -m venv .venv
```

Para ativá-lo no PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Quando estiver ativo, o terminal normalmente exibirá `(.venv)` no início da linha.

Para sair do ambiente virtual:

```powershell
deactivate
```

O ambiente virtual será estudado com mais profundidade em um tópico posterior, quando você começar a trabalhar com bibliotecas e dependências.

## 9. Problemas comuns

### O comando python não é reconhecido

Possíveis causas:
- Python não está instalado.
- O Python não está configurado no PATH.
- O terminal foi aberto antes da alteração das variáveis de ambiente.

Verifique a instalação e tente `py --version`.

### O VS Code não encontra o interpretador

Abra a paleta de comandos com `Ctrl + Shift + P`, procure por `Python: Select Interpreter` e selecione o interpretador correto.

### O arquivo não é executado

Confira:
- Se o arquivo foi salvo com a extensão `.py`.
- Se o terminal está na pasta correta.
- Se o nome do arquivo está correto.
- Se há mensagens de erro no terminal.

## 10. Resumo

Para desenvolver em Python, é necessário ter um interpretador instalado e um editor de código configurado. O VS Code facilita a escrita, a execução e a depuração dos programas.

O terminal permite executar scripts e comandos, enquanto os ambientes virtuais ajudam a isolar as dependências de cada projeto.

## 11. Exercícios de fixação

1. Instale ou verifique a instalação do Python.
2. Confira a versão instalada pelo terminal.
3. Instale o VS Code e a extensão Python.
4. Crie um arquivo chamado `main.py`.
5. Escreva um programa que exiba uma mensagem.
6. Execute o programa pelo terminal.
7. Explique, com suas próprias palavras, a diferença entre Python, VS Code e terminal.
8. Explique para que serve um ambiente virtual.

## 12. Instalando o PyCharm

O PyCharm é um ambiente de desenvolvimento integrado (IDE) criado pela JetBrains, voltado principalmente para programação em Python.

Diferentemente de um editor mais genérico, ele oferece diversas ferramentas integradas para desenvolvimento, execução, depuração e organização de projetos.

### Principais recursos

- Autocompletar código.
- Identificação de erros durante a escrita.
- Depuração de programas.
- Gerenciamento de projetos.
- Integração com Git.
- Suporte a ambientes virtuais.
- Ferramentas para testes automatizados.

### Download

Acesse o site oficial:

https://www.jetbrains.com/pycharm/download/

Baixe a versão para Windows e siga as instruções do instalador.

O PyCharm possui uma versão gratuita com recursos para desenvolvimento em Python. Alguns recursos avançados podem depender de uma assinatura.

## 13. Configurando o Python no PyCharm

Após instalar o PyCharm:

1. Abra o programa.
2. Selecione a opção para criar um novo projeto.
3. Escolha o diretório em que o projeto será armazenado.
4. Configure o interpretador Python.
5. Se necessário, selecione a instalação existente do Python ou crie um ambiente virtual.
6. Finalize a criação do projeto.

### Criando o primeiro arquivo

Dentro do projeto:

1. Clique com o botão direito na pasta do projeto.
2. Selecione New > Python File.
3. Informe o nome `main`.
4. Escreva o código abaixo:

```python
print("Olá, mundo!")
```

5. Clique com o botão direito no arquivo e selecione Run 'main'.

A saída esperada será:

```text
Olá, mundo!
```

## 14. VS Code ou PyCharm?

Os dois ambientes permitem desenvolver aplicações Python, mas apresentam diferenças.

| Característica | VS Code | PyCharm |
|---|---|---|
| Tipo | Editor extensível | IDE especializada |
| Configuração inicial | Pode exigir extensões e ajustes | Integra mais ferramentas |
| Python | Suporte por extensão | Suporte integrado |
| Depuração | Disponível | Disponível |
| Git | Integração por extensões e recursos internos | Integração integrada |
| Ambientes virtuais | Suportados | Gerenciados pela IDE |
| Melhor utilização | Projetos variados e múltiplas linguagens | Desenvolvimento focado em Python |

## 15. Qual devo escolher?

Não é obrigatório instalar ou utilizar os dois ambientes.

- **VS Code:** boa opção para quem quer trabalhar com Python, SQL, scripts e outras linguagens no mesmo editor.
- **PyCharm:** boa opção para quem deseja um ambiente mais especializado em Python, com ferramentas de desenvolvimento integradas.

Ambos podem ser utilizados para aprender Python e desenvolver projetos profissionais.