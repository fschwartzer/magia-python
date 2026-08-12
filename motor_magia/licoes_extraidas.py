"""Licoes extraidas automaticamente dos notebooks.
Nao editar manualmente. Rode scripts/extrair_licoes.py.
Gerado em: 2026-08-12 16:17:49
"""

LESSONS_DATA = [{'lesson_id': 'aula-1',
  'order': 1,
  'title': '🌟 Aula 1: Primeiros Passos',
  'notebook_file': 'minha_primeira_aula.ipynb',
  'total_cells': 13,
  'code_cells': 5,
  'markdown_cells': 8,
  'cells': [{'cell_id': 'aula-1::cell-1',
             'index': 1,
             'cell_type': 'markdown',
             'source': '# 🪄 A Escola de Magia do Python 🐍\n'
                       '\n'
                       'Olá! Hoje você não é apenas uma aluna, você é uma **Feiticeira da '
                       'Programação**! 🧙\u200d♀️✨\n'
                       '\n'
                       'O computador é como um robô que obedece a tudo o que a gente manda, mas '
                       'precisamos falar a língua dele. Essa língua se chama **Python**.\n'
                       '\n'
                       'Vamos aprender 3 feitiços hoje:\n'
                       '1. Fazer o computador **Falar**.\n'
                       '2. Fazer o computador **Guardar Segredos** (Memória).\n'
                       '3. Fazer o computador **Escutar** você.\n'
                       '\n'
                       '**Dica Importante:** Para fazer a mágica acontecer, clique em **Executar '
                       'magia**, abaixo da caixa de código.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-1::cell-2',
             'index': 2,
             'cell_type': 'markdown',
             'source': '## 🗣️ Feitiço 1: O Computador Tagarela (`print`)\n'
                       '\n'
                       'O comando `print` serve para mostrar coisas na tela. É como se o '
                       'computador estivesse falando com você.\n'
                       '\n'
                       '**Missão:** Observe o código abaixo e clique em **Executar magia** para '
                       'ver o que acontece.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-1::cell-3',
             'index': 3,
             'cell_type': 'code',
             'source': 'print("Olá! Eu sou o seu computador!")\n'
                       'print("Eu adoro aprender coisas novas.")',
             'requires_input': False,
             'default_code': 'print("Olá! Eu sou o seu computador!")\n'
                             'print("Eu adoro aprender coisas novas.")'},
            {'cell_id': 'aula-1::cell-4',
             'index': 4,
             'cell_type': 'markdown',
             'source': '### ⚡ Desafio Relâmpago!\n'
                       'No código abaixo, apague o texto que está dentro das aspas `" "` e escreva '
                       'o seu nome. Depois, clique em **Executar magia**.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-1::cell-5',
             'index': 5,
             'cell_type': 'code',
             'source': 'print("escreva aqui seu nome")',
             'requires_input': False,
             'default_code': 'print("escreva aqui seu nome")'},
            {'cell_id': 'aula-1::cell-6',
             'index': 6,
             'cell_type': 'markdown',
             'source': '## 📦 Feitiço 2: As Caixinhas Mágicas (Variáveis)\n'
                       '\n'
                       'O computador tem uma memória muito boa, mas ele precisa de ajuda. Nós '
                       'usamos **Caixinhas** (que os adultos chamam de *Variáveis*) para guardar '
                       'informações.\n'
                       '\n'
                       'Vamos criar uma caixinha chamada `comida_favorita` e guardar uma coisa '
                       'deliciosa dentro dela.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-1::cell-7',
             'index': 7,
             'cell_type': 'code',
             'source': '# Criando a caixinha\n'
                       'comida_favorita = "escreva aqui sua comida favorita"\n'
                       '\n'
                       '# Mandando o computador mostrar o que tem dentro da caixinha\n'
                       'print(comida_favorita)',
             'requires_input': False,
             'default_code': '# Criando a caixinha\n'
                             'comida_favorita = "escreva aqui sua comida favorita"\n'
                             '\n'
                             '# Mandando o computador mostrar o que tem dentro da caixinha\n'
                             'print(comida_favorita)'},
            {'cell_id': 'aula-1::cell-8',
             'index': 8,
             'cell_type': 'markdown',
             'source': 'Viu? Você não precisou escrever "Sorvete" dentro do print. Você usou o '
                       'nome da caixinha!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-1::cell-9',
             'index': 9,
             'cell_type': 'markdown',
             'source': '## 👂 Feitiço 3: O Computador Curioso (`input`)\n'
                       '\n'
                       'E se a gente quiser que o computador faça uma pergunta para você?\n'
                       'Usamos o comando `input`. Clique em **Executar magia**, preencha a '
                       'resposta no pop-up e confirme a execução!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-1::cell-10',
             'index': 10,
             'cell_type': 'code',
             'source': 'nome = input("Qual é o seu nome? ")\n'
                       'print("Nossa! Que nome lindo!")\n'
                       'print("Prazer em te conhecer, " + nome)',
             'requires_input': True,
             'default_code': 'nome = input("Qual é o seu nome? ")\n'
                             'print("Nossa! Que nome lindo!")\n'
                             'print("Prazer em te conhecer, " + nome)'},
            {'cell_id': 'aula-1::cell-11',
             'index': 11,
             'cell_type': 'markdown',
             'source': '## 🏰 O Grande Projeto: O Gerador de Histórias Malucas 🤪\n'
                       '\n'
                       'Agora vamos juntar tudo o que aprendemos!\n'
                       '\n'
                       'Vamos criar um programa que escreve uma história engraçada baseada no que '
                       'você responder.\n'
                       '\n'
                       '**Instruções:**\n'
                       '1. Clique em **Executar magia** abaixo do código.\n'
                       '2. Preencha as caixas de resposta no pop-up.\n'
                       '3. Clique em **Executar magia** no pop-up e veja a história mágica no '
                       'final!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-1::cell-12',
             'index': 12,
             'cell_type': 'code',
             'source': '# O Computador vai fazer perguntas e guardar nas caixinhas\n'
                       'animal = input("Digite o nome de um animal (ex: gato, dragão): ")\n'
                       'cor = input("Digite uma cor bem diferente: ")\n'
                       'comida = input("Digite uma comida estranha: ")\n'
                       'lugar = input("Digite um lugar (ex: castelo, escola, lua): ")\n'
                       '\n'
                       'print("--------------------------------------------------")\n'
                       'print("📖 AQUI ESTÁ A SUA HISTÓRIA MALUCA:")\n'
                       'print("")\n'
                       'print("Era uma vez um " + animal + " muito especial.")\n'
                       'print("Ele era diferente de todos, pois a sua cor era " + cor + "!")\n'
                       'print("Um dia, ele estava no(a) " + lugar + " sentindo muita fome.")\n'
                       'print("Então, ele resolveu cozinhar o prato favorito dele: " + comida + '
                       '".")\n'
                       'print("E todos viveram felizes e com a barriga cheia!")\n'
                       'print("")\n'
                       'print("FIM! 🎉")',
             'requires_input': True,
             'default_code': '# O Computador vai fazer perguntas e guardar nas caixinhas\n'
                             'animal = input("Digite o nome de um animal (ex: gato, dragão): ")\n'
                             'cor = input("Digite uma cor bem diferente: ")\n'
                             'comida = input("Digite uma comida estranha: ")\n'
                             'lugar = input("Digite um lugar (ex: castelo, escola, lua): ")\n'
                             '\n'
                             'print("--------------------------------------------------")\n'
                             'print("📖 AQUI ESTÁ A SUA HISTÓRIA MALUCA:")\n'
                             'print("")\n'
                             'print("Era uma vez um " + animal + " muito especial.")\n'
                             'print("Ele era diferente de todos, pois a sua cor era " + cor + '
                             '"!")\n'
                             'print("Um dia, ele estava no(a) " + lugar + " sentindo muita '
                             'fome.")\n'
                             'print("Então, ele resolveu cozinhar o prato favorito dele: " + '
                             'comida + ".")\n'
                             'print("E todos viveram felizes e com a barriga cheia!")\n'
                             'print("")\n'
                             'print("FIM! 🎉")'},
            {'cell_id': 'aula-1::cell-13',
             'index': 13,
             'cell_type': 'markdown',
             'source': '## Parabéns! 🏆\n'
                       '\n'
                       'Você escreveu seu primeiro programa de computador. Você é incrível!\n'
                       'Clique em **Executar magia**, preencha o pop-up com novas respostas e '
                       'confirme para inventar coisas ainda mais malucas.',
             'requires_input': False,
             'default_code': None}]},
 {'lesson_id': 'aula-2',
  'order': 2,
  'title': '🕵️ Aula 2: O Computador Detetive',
  'notebook_file': 'minha_segunda_aula.ipynb',
  'total_cells': 10,
  'code_cells': 3,
  'markdown_cells': 7,
  'cells': [{'cell_id': 'aula-2::cell-1',
             'index': 1,
             'cell_type': 'markdown',
             'source': '# 🕵️\u200d♀️ Aula 2: O Computador Detetive\n'
                       '\n'
                       'Bem-vinda de volta, Feiticeira da Programação! 🧙\u200d♀️\n'
                       '\n'
                       'Na última aula, você ensinou o computador a falar e a guardar nomes. Hoje, '
                       'vamos ensinar o computador a **PENSAR** e **TOMAR DECISÕES**!\n'
                       '\n'
                       'Vamos aprender:\n'
                       '1. Como comparar coisas.\n'
                       '2. O feitiço do **"SE"** (`if`).\n'
                       '3. O feitiço do **"SENÃO"** (`else`).\n'
                       '\n'
                       'Prepare sua varinha (o teclado) e vamos lá! ✨',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-2::cell-2',
             'index': 2,
             'cell_type': 'markdown',
             'source': '## 🔍 Parte 1: O Detetive Compara Coisas (`==`)\n'
                       '\n'
                       'Para o computador tomar decisões, ele precisa saber se duas coisas são '
                       'iguais.\n'
                       'Na matemática, usamos um sinal de igual `=`. No Python, para perguntar '
                       '"Isso é igual àquilo?", nós usamos **DOIS** sinais de igual: `==`.\n'
                       '\n'
                       'Tente adivinhar o que vai acontecer abaixo e clique em **Executar magia**.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-2::cell-3',
             'index': 3,
             'cell_type': 'code',
             'source': 'print(5 == 5)   # Cinco é igual a cinco?\n'
                       'print(5 == 10)  # Cinco é igual a dez?\n'
                       'print("Banana" == "Banana") # A palavra é igual?',
             'requires_input': False,
             'default_code': 'print(5 == 5)   # Cinco é igual a cinco?\n'
                             'print(5 == 10)  # Cinco é igual a dez?\n'
                             'print("Banana" == "Banana") # A palavra é igual?'},
            {'cell_id': 'aula-2::cell-4',
             'index': 4,
             'cell_type': 'markdown',
             'source': 'O computador respondeu `True` (Verdadeiro) ou `False` (Falso). Ele é muito '
                       'esperto!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-2::cell-5',
             'index': 5,
             'cell_type': 'markdown',
             'source': '## 🚪 Parte 2: A Senha Secreta (`if` e `else`)\n'
                       '\n'
                       'Agora vamos criar um porteiro digital. Ele só vai deixar entrar quem '
                       'souber a senha.\n'
                       '\n'
                       'Usamos o comando `if`, que significa **"SE"** em inglês.\n'
                       'E usamos o `else`, que significa **"SENÃO"** (ou "caso contrário").\n'
                       '\n'
                       '**⚠️ ATENÇÃO MÁGICA:**\n'
                       'Note que algumas linhas têm um espaço vazio no começo (um recuo). Isso '
                       'mostra que aquela linha pertence ao `if`. Sem esse espacinho, a mágica não '
                       'funciona!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-2::cell-6',
             'index': 6,
             'cell_type': 'code',
             'source': 'senha = input("Digite a senha secreta para entrar no clube: ")\n'
                       '\n'
                       'if senha == "chocolate":\n'
                       '    print("✅ ACESSO PERMITIDO! Bem-vinda ao clube!")\n'
                       'else:\n'
                       '    print("❌ SENHA INCORRETA! Tente de novo.")',
             'requires_input': True,
             'default_code': 'senha = input("Digite a senha secreta para entrar no clube: ")\n'
                             '\n'
                             'if senha == "chocolate":\n'
                             '    print("✅ ACESSO PERMITIDO! Bem-vinda ao clube!")\n'
                             'else:\n'
                             '    print("❌ SENHA INCORRETA! Tente de novo.")'},
            {'cell_id': 'aula-2::cell-7',
             'index': 7,
             'cell_type': 'markdown',
             'source': '**Desafio:** Execute o código duas vezes usando o botão **Executar '
                       'magia**.\n'
                       '1. Na primeira execução, preencha o pop-up com `chocolate` (tudo '
                       'minúsculo) e confirme.\n'
                       '2. Na segunda, preencha o pop-up com `abacaxi` e confirme novamente.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-2::cell-8',
             'index': 8,
             'cell_type': 'markdown',
             'source': '## 🏆 O Grande Jogo: O Quiz dos Animais 🦁\n'
                       '\n'
                       'Agora vamos construir um jogo de verdade! Vamos fazer perguntas e contar '
                       'os pontos.\n'
                       '\n'
                       'Nós vamos usar uma variável chamada `pontos` que começa com **zero**. Cada '
                       'vez que você acertar, vamos somar +1 ponto.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-2::cell-9',
             'index': 9,
             'cell_type': 'code',
             'source': 'print("Bem-vinda ao Quiz!")\n'
                       'pontos = 0\n'
                       '\n'
                       '# Pergunta 1\n'
                       'resposta = input("Qual animal faz \'Miau\'? ")\n'
                       'if resposta == "gato":\n'
                       '    print("🎉 Acertou!")\n'
                       '    pontos = pontos + 1\n'
                       'else:\n'
                       '    print("😱 Errou! A resposta era gato.")\n'
                       '\n'
                       '# Pergunta 2\n'
                       'resposta = input("O pato tem quantas patas? ")\n'
                       'if resposta == "2":\n'
                       '    print("🎉 Acertou de novo!")\n'
                       '    pontos = pontos + 1\n'
                       'else:\n'
                       '    print("😱 Errou! Ele tem 2 patas.")\n'
                       '\n'
                       '# Pergunta 3\n'
                       'resposta = input("Quanto é 2 + 3? ")\n'
                       'if resposta == "5":\n'
                       '    print("🎉 Acertou de novo!")\n'
                       '    pontos = pontos + 1\n'
                       'else:\n'
                       '    print("😱 Errou! É 5.")\n'
                       '\n'
                       '# Pergunta 4\n'
                       'resposta = input("22+20?")\n'
                       'if resposta == "42":\n'
                       '    print("🎉 Acertou de novo!")\n'
                       '    pontos = pontos + 1\n'
                       'else:\n'
                       '    print("😱 Errou! É 42.")\n'
                       '\n'
                       '# Resultado Final\n'
                       'print("------------------------")\n'
                       'print("Fim de jogo!")\n'
                       'print("Você fez " + str(pontos) + " pontos!")',
             'requires_input': True,
             'default_code': 'print("Bem-vinda ao Quiz!")\n'
                             'pontos = 0\n'
                             '\n'
                             '# Pergunta 1\n'
                             'resposta = input("Qual animal faz \'Miau\'? ")\n'
                             'if resposta == "gato":\n'
                             '    print("🎉 Acertou!")\n'
                             '    pontos = pontos + 1\n'
                             'else:\n'
                             '    print("😱 Errou! A resposta era gato.")\n'
                             '\n'
                             '# Pergunta 2\n'
                             'resposta = input("O pato tem quantas patas? ")\n'
                             'if resposta == "2":\n'
                             '    print("🎉 Acertou de novo!")\n'
                             '    pontos = pontos + 1\n'
                             'else:\n'
                             '    print("😱 Errou! Ele tem 2 patas.")\n'
                             '\n'
                             '# Pergunta 3\n'
                             'resposta = input("Quanto é 2 + 3? ")\n'
                             'if resposta == "5":\n'
                             '    print("🎉 Acertou de novo!")\n'
                             '    pontos = pontos + 1\n'
                             'else:\n'
                             '    print("😱 Errou! É 5.")\n'
                             '\n'
                             '# Pergunta 4\n'
                             'resposta = input("22+20?")\n'
                             'if resposta == "42":\n'
                             '    print("🎉 Acertou de novo!")\n'
                             '    pontos = pontos + 1\n'
                             'else:\n'
                             '    print("😱 Errou! É 42.")\n'
                             '\n'
                             '# Resultado Final\n'
                             'print("------------------------")\n'
                             'print("Fim de jogo!")\n'
                             'print("Você fez " + str(pontos) + " pontos!")'},
            {'cell_id': 'aula-2::cell-10',
             'index': 10,
             'cell_type': 'markdown',
             'source': '### 🌟 Missão de Casa\n'
                       '\n'
                       'Você consegue adicionar uma **Pergunta 5** no código acima?\n'
                       '\n'
                       '**Dica:** Copie e cole o bloco da pergunta do cachorro e mude as palavras. '
                       'Não esqueça de somar os pontos se acertar!',
             'requires_input': False,
             'default_code': None}]},
 {'lesson_id': 'aula-3',
  'order': 3,
  'title': '🔁 Aula 3: Repetições Mágicas',
  'notebook_file': 'minha_terceira_aula.ipynb',
  'total_cells': 9,
  'code_cells': 3,
  'markdown_cells': 6,
  'cells': [{'cell_id': 'aula-3::cell-1',
             'index': 1,
             'cell_type': 'markdown',
             'source': '# ⏳ Aula 3: O Mago do Tempo e da Sorte\n'
                       '\n'
                       'Olá, Grande Programadora! 🧙\u200d♀️✨\n'
                       '\n'
                       'Nas últimas aulas, você aprendeu a falar com o computador e a fazer ele '
                       'tomar decisões.\n'
                       'Hoje, vamos dar a ele dois novos poderes:\n'
                       '\n'
                       '1. **O Poder da Sorte:** O computador vai escolher números surpresa!\n'
                       '2. **O Poder da Repetição:** O computador vai fazer coisas várias vezes '
                       'sem se cansar.\n'
                       '\n'
                       'Vamos abrir nossa mochila de ferramentas!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-3::cell-2',
             'index': 2,
             'cell_type': 'markdown',
             'source': '## 🎒 Parte 1: A Mochila de Ferramentas (`import`)\n'
                       '\n'
                       'O Python tem muitas ferramentas guardadas numa mochila. Para usar, '
                       'precisamos pedir para ele pegar.\n'
                       '\n'
                       'Vamos pegar a ferramenta `random` (que significa **Aleatório** ou '
                       '**Sorte**).\n'
                       'Clique em **Executar magia** várias vezes e veja o número mudar!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-3::cell-3',
             'index': 3,
             'cell_type': 'code',
             'source': 'import random\n'
                       '\n'
                       '# O computador vai escolher um número entre 1 e 10\n'
                       'numero_surpresa = random.randint(1, 100)\n'
                       '\n'
                       'print("O número sorteado foi:")\n'
                       'print(numero_surpresa)',
             'requires_input': False,
             'default_code': 'import random\n'
                             '\n'
                             '# O computador vai escolher um número entre 1 e 10\n'
                             'numero_surpresa = random.randint(1, 100)\n'
                             '\n'
                             'print("O número sorteado foi:")\n'
                             'print(numero_surpresa)'},
            {'cell_id': 'aula-3::cell-4',
             'index': 4,
             'cell_type': 'markdown',
             'source': '## 🔄 Parte 2: A Roda Gigante (`while`)\n'
                       '\n'
                       'Imagine que você quer contar até 5. Você não precisa escrever 5 prints. '
                       'Você pode usar o `while` (que significa **ENQUANTO**).\n'
                       '\n'
                       'O código abaixo diz: *"Enquanto o número for maior que zero, continue '
                       'contando!"*',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-3::cell-5',
             'index': 5,
             'cell_type': 'code',
             'source': 'import time # Vamos pegar a ferramenta do Tempo\n'
                       '\n'
                       'contador = 5\n'
                       '\n'
                       'print("🚀 Preparar para decolagem...")\n'
                       '\n'
                       'while contador > 0:\n'
                       '    print(contador)\n'
                       '    contador = contador - 1\n'
                       '    time.sleep(1) # Espera 1 segundo (dorme um pouquinho)\n'
                       '\n'
                       'print("🔥 DECOLAR!")',
             'requires_input': False,
             'default_code': 'import time # Vamos pegar a ferramenta do Tempo\n'
                             '\n'
                             'contador = 5\n'
                             '\n'
                             'print("🚀 Preparar para decolagem...")\n'
                             '\n'
                             'while contador > 0:\n'
                             '    print(contador)\n'
                             '    contador = contador - 1\n'
                             '    time.sleep(1) # Espera 1 segundo (dorme um pouquinho)\n'
                             '\n'
                             'print("🔥 DECOLAR!")'},
            {'cell_id': 'aula-3::cell-6',
             'index': 6,
             'cell_type': 'markdown',
             'source': '## 🔢 Parte 3: O Transformador de Números (`int`)\n'
                       '\n'
                       'Aqui tem um segredinho. Quando você usa o `input` para digitar algo, o '
                       'computador acha que é um **Texto** (uma palavra).\n'
                       '\n'
                       'Mas para matemática, precisamos transformar esse texto em **Número**.\n'
                       'Usamos o feitiço `int()` para isso.\n'
                       '\n'
                       'Exemplo: `chute = int(input("Digite um número"))`',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-3::cell-7',
             'index': 7,
             'cell_type': 'markdown',
             'source': '## 🔮 O Grande Projeto: Jogo da Adivinhação\n'
                       '\n'
                       'Agora o desafio final!\n'
                       '1. O Computador vai pensar num número de 1 a 10.\n'
                       '2. Você vai tentar adivinhar.\n'
                       '3. O jogo **NÃO VAI PARAR** (loop) até você acertar!\n'
                       '\n'
                       'Preparada? Clique em **Executar magia**, preencha a resposta no pop-up e '
                       'confirme!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-3::cell-8',
             'index': 8,
             'cell_type': 'code',
             'source': 'import random\n'
                       '\n'
                       'print("🤖: Estou pensando em um número de 1 a 10...")\n'
                       'numero_secreto = random.randint(1, 10)\n'
                       '\n'
                       'chute = 0  # Começamos com zero para o jogo não acabar antes de começar\n'
                       '\n'
                       '# Enquanto o seu chute for diferente (!=) do segredo, continue '
                       'perguntando\n'
                       'while chute != numero_secreto:\n'
                       '\n'
                       '    # O int() transforma sua resposta em número de verdade\n'
                       '    chute = int(input("Qual é o seu chute? "))\n'
                       '\n'
                       '    if chute == numero_secreto:\n'
                       '        print("🎉 PARABÉNS! Você leu minha mente!")\n'
                       '    else:\n'
                       '        if chute > numero_secreto:\n'
                       '            print("👇 Menos... Tente um número menor.")\n'
                       '        else:\n'
                       '            print("👆 Mais... Tente um número maior.")\n'
                       '\n'
                       'print("Fim de jogo!")',
             'requires_input': True,
             'default_code': 'import random\n'
                             '\n'
                             'print("🤖: Estou pensando em um número de 1 a 10...")\n'
                             'numero_secreto = random.randint(1, 10)\n'
                             '\n'
                             'chute = 0  # Começamos com zero para o jogo não acabar antes de '
                             'começar\n'
                             '\n'
                             '# Enquanto o seu chute for diferente (!=) do segredo, continue '
                             'perguntando\n'
                             'while chute != numero_secreto:\n'
                             '\n'
                             '    # O int() transforma sua resposta em número de verdade\n'
                             '    chute = int(input("Qual é o seu chute? "))\n'
                             '\n'
                             '    if chute == numero_secreto:\n'
                             '        print("🎉 PARABÉNS! Você leu minha mente!")\n'
                             '    else:\n'
                             '        if chute > numero_secreto:\n'
                             '            print("👇 Menos... Tente um número menor.")\n'
                             '        else:\n'
                             '            print("👆 Mais... Tente um número maior.")\n'
                             '\n'
                             'print("Fim de jogo!")'},
            {'cell_id': 'aula-3::cell-9',
             'index': 9,
             'cell_type': 'markdown',
             'source': '### 🏆 Desafio Extra\n'
                       '\n'
                       'Achou fácil? Tente mudar o código acima para o computador pensar em um '
                       'número de **1 até 100**!\n'
                       'Procure onde está escrito `(1, 10)` e mude para `(1, 100)`.',
             'requires_input': False,
             'default_code': None}]},
 {'lesson_id': 'aula-4',
  'order': 4,
  'title': '📦 Aula 4: Listas Encantadas',
  'notebook_file': 'minha_quarta_aula.ipynb',
  'total_cells': 11,
  'code_cells': 5,
  'markdown_cells': 6,
  'cells': [{'cell_id': 'aula-4::cell-1',
             'index': 1,
             'cell_type': 'markdown',
             'source': '# 🎒 Aula 4: A Mochila Mágica (Listas)\n'
                       '\n'
                       'Parabéns por chegar até aqui! 🚀\n'
                       '\n'
                       'Você já sabe guardar **uma** coisa em uma variável. Mas imagine se você '
                       'fosse viajar. Você não levaria uma mala para a escova de dentes, outra '
                       'mala para o pijama e outra para o brinquedo, certo?\n'
                       '\n'
                       'Você usa uma **MALA** para guardar tudo junto!\n'
                       '\n'
                       'No Python, chamamos isso de **LISTA**. Vamos aprender a criar listas hoje.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-4::cell-2',
             'index': 2,
             'cell_type': 'markdown',
             'source': '## 📝 Parte 1: Criando uma Lista\n'
                       '\n'
                       'Para fazer uma lista, usamos os colchetes `[ ]` e separamos as coisas com '
                       'vírgulas.\n'
                       '\n'
                       'Veja a lista de compras abaixo e clique em **Executar magia**.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-4::cell-3',
             'index': 3,
             'cell_type': 'code',
             'source': '# Aqui está nossa lista de compras\n'
                       'compras = ["Banana", "Chocolate", "Leite", "Biscoito"]\n'
                       '\n'
                       'print("Minha lista de compras:")\n'
                       'print(compras)',
             'requires_input': False,
             'default_code': '# Aqui está nossa lista de compras\n'
                             'compras = ["Banana", "Chocolate", "Leite", "Biscoito"]\n'
                             '\n'
                             'print("Minha lista de compras:")\n'
                             'print(compras)'},
            {'cell_id': 'aula-4::cell-4',
             'index': 4,
             'cell_type': 'markdown',
             'source': '## 🔢 Parte 2: A Regra do Zero (Muito Importante!)\n'
                       '\n'
                       'Agora, preste muita atenção. Os computadores são um pouco estranhos.\n'
                       '\n'
                       'Quando a gente conta, começamos do 1. Mas o computador começa a contar do '
                       '**ZERO**.\n'
                       '\n'
                       'Se quisermos pegar o **primeiro** item da lista, pedimos o número **0**.\n'
                       'Se quisermos o **segundo**, pedimos o número **1**.\n'
                       '\n'
                       'Isso se chama **Índice**.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-4::cell-5',
             'index': 5,
             'cell_type': 'code',
             'source': 'frutas = ["Morango", "Uva", "Abacaxi"]\n'
                       '\n'
                       '# Vamos tentar pegar as frutas pelo número da posição\n'
                       'print("A fruta número 0 é:")\n'
                       'print(frutas[0])\n'
                       '\n'
                       'print("A fruta número 1 é:")\n'
                       'print(frutas[1])\n'
                       '\n'
                       'print("A fruta número 2 é:")\n'
                       'print(frutas[2])',
             'requires_input': False,
             'default_code': 'frutas = ["Morango", "Uva", "Abacaxi"]\n'
                             '\n'
                             '# Vamos tentar pegar as frutas pelo número da posição\n'
                             'print("A fruta número 0 é:")\n'
                             'print(frutas[0])\n'
                             '\n'
                             'print("A fruta número 1 é:")\n'
                             'print(frutas[1])\n'
                             '\n'
                             'print("A fruta número 2 é:")\n'
                             'print(frutas[2])'},
            {'cell_id': 'aula-4::cell-7',
             'index': 7,
             'cell_type': 'markdown',
             'source': '## ➕ Parte 3: Colocando coisas na Mochila (`append`)\n'
                       '\n'
                       'E se a gente esqueceu de algo? Podemos adicionar itens novos na lista '
                       'usando o comando mágico `.append()` (que significa "anexar" ou '
                       '"adicionar").',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-4::cell-8',
             'index': 8,
             'cell_type': 'code',
             'source': 'mochila = ["Lanterna", "Mapa"]\n'
                       '\n'
                       'print("Minha mochila tem:")\n'
                       'print(mochila)\n'
                       '\n'
                       'print("Ah! Esqueci a garrafa de água! Adicionando...")\n'
                       'mochila.append("Água")\n'
                       '\n'
                       'print("Agora minha mochila tem:")\n'
                       'print(mochila)\n'
                       '\n'
                       'print("Ah! Preciso fazer fogo! Adicionando o fósforo...")\n'
                       'mochila.append("Fósforo")\n'
                       '\n'
                       'print("Agora minha mochila tem:")\n'
                       'print(mochila)',
             'requires_input': False,
             'default_code': 'mochila = ["Lanterna", "Mapa"]\n'
                             '\n'
                             'print("Minha mochila tem:")\n'
                             'print(mochila)\n'
                             '\n'
                             'print("Ah! Esqueci a garrafa de água! Adicionando...")\n'
                             'mochila.append("Água")\n'
                             '\n'
                             'print("Agora minha mochila tem:")\n'
                             'print(mochila)\n'
                             '\n'
                             'print("Ah! Preciso fazer fogo! Adicionando o fósforo...")\n'
                             'mochila.append("Fósforo")\n'
                             '\n'
                             'print("Agora minha mochila tem:")\n'
                             'print(mochila)'},
            {'cell_id': 'aula-4::cell-9',
             'index': 9,
             'cell_type': 'markdown',
             'source': '## 🎲 O Grande Projeto: O Sorteador do Fim de Semana\n'
                       '\n'
                       'Vamos usar a biblioteca `random` de novo, mas agora com um poder novo: o '
                       '`choice` (escolha).\n'
                       '\n'
                       'O computador vai pegar sua lista de brincadeiras e escolher **uma** para '
                       'você fazer!\n'
                       '\n'
                       '**Sua Missão:**\n'
                       '1. No código abaixo, mude os nomes das brincadeiras para as que você mais '
                       'gosta.\n'
                       '2. Pode adicionar mais brincadeiras se quiser!\n'
                       '3. Clique em **Executar magia** para ver o que o destino escolheu.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-4::cell-10',
             'index': 10,
             'cell_type': 'code',
             'source': 'import random\n'
                       '\n'
                       '# 1. Crie sua lista de brincadeiras aqui\n'
                       'brincadeiras = ["vôlei", "boneca", "nadar", "fazer pulseiras", '
                       '"esconde-esconde", "andar de balanço", "jogar jogos"]\n'
                       '\n'
                       '# 2. O computador vai escolher uma aleatoriamente\n'
                       'escolha = random.choice(brincadeiras)\n'
                       '\n'
                       'print("🤔 O computador está pensando no que vamos fazer...")\n'
                       'print("✨ DECIDIDO! Hoje nós vamos: " + escolha + "!")',
             'requires_input': False,
             'default_code': 'import random\n'
                             '\n'
                             '# 1. Crie sua lista de brincadeiras aqui\n'
                             'brincadeiras = ["vôlei", "boneca", "nadar", "fazer pulseiras", '
                             '"esconde-esconde", "andar de balanço", "jogar jogos"]\n'
                             '\n'
                             '# 2. O computador vai escolher uma aleatoriamente\n'
                             'escolha = random.choice(brincadeiras)\n'
                             '\n'
                             'print("🤔 O computador está pensando no que vamos fazer...")\n'
                             'print("✨ DECIDIDO! Hoje nós vamos: " + escolha + "!")'},
            {'cell_id': 'aula-4::cell-11',
             'index': 11,
             'cell_type': 'markdown',
             'source': '### 🏆 Missão de Casa: O Sorteador de Ajudantes\n'
                       '\n'
                       'Que tal criar um código novo que tem uma lista com o nome de todas as '
                       'pessoas da sua casa?\n'
                       'Aí você pede para o computador sortear: **"Quem vai lavar a louça hoje?"** '
                       '🧼🍽️\n'
                       '\n'
                       'Divirta-se criando listas!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-4::cell-12',
             'index': 12,
             'cell_type': 'code',
             'source': 'import random\n'
                       '\n'
                       'pessoas = ["Maria", "José", "João"]\n'
                       'escolha = random.choice(pessoas)\n'
                       'print("O computador está sorteando...")\n'
                       'print("O escolhido é: " + escolha)',
             'requires_input': False,
             'default_code': 'import random\n'
                             '\n'
                             'pessoas = ["Maria", "José", "João"]\n'
                             'escolha = random.choice(pessoas)\n'
                             'print("O computador está sorteando...")\n'
                             'print("O escolhido é: " + escolha)'}]},
 {'lesson_id': 'aula-5',
  'order': 5,
  'title': '🧪 Aula 5: Funções e Poções',
  'notebook_file': 'minha_quinta_aula.ipynb',
  'total_cells': 11,
  'code_cells': 4,
  'markdown_cells': 7,
  'cells': [{'cell_id': 'aula-5::cell-1',
             'index': 1,
             'cell_type': 'markdown',
             'source': '# 🏭 Aula 5: A Fábrica Automática (`for`)\n'
                       '\n'
                       'Olá, Mestra dos Códigos! 👩\u200d💻\n'
                       '\n'
                       'Na aula passada, criamos listas (mochilas). Mas imagine que você tem uma '
                       'lista com 50 amigos e quer mandar "Oi" para todos.\n'
                       '\n'
                       'Você escreveria 50 vezes o comando `print`? Nããão! Isso dá muito '
                       'trabalho.\n'
                       '\n'
                       'Hoje vamos criar um **Robô Trabalhador** que faz isso para você. O nome '
                       'dele é `for` (que significa **"PARA CADA"**).',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-5::cell-2',
             'index': 2,
             'cell_type': 'markdown',
             'source': '## 🤖 Parte 1: O Robô que Lê Listas\n'
                       '\n'
                       'O comando `for` funciona assim: ele olha para a sua lista, pega o primeiro '
                       'item, faz o que você mandou, depois pega o segundo, e assim por diante.\n'
                       '\n'
                       'Veja a mágica acontecer abaixo:',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-5::cell-3',
             'index': 3,
             'cell_type': 'code',
             'source': 'frutas = ["Maçã", "Banana", "Laranja", "Melancia"]\n'
                       '\n'
                       "# O Robô vai chamar cada fruta de 'f' (apelido carinhoso)\n"
                       'for f in frutas:\n'
                       '    print("Eu adoro comer " + f)',
             'requires_input': False,
             'default_code': 'frutas = ["Maçã", "Banana", "Laranja", "Melancia"]\n'
                             '\n'
                             "# O Robô vai chamar cada fruta de 'f' (apelido carinhoso)\n"
                             'for f in frutas:\n'
                             '    print("Eu adoro comer " + f)'},
            {'cell_id': 'aula-5::cell-4',
             'index': 4,
             'cell_type': 'markdown',
             'source': 'Percebeu? Você escreveu o `print` só uma vez, mas ele apareceu 4 vezes! O '
                       '`f` mudava de nome a cada volta.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-5::cell-5',
             'index': 5,
             'cell_type': 'markdown',
             'source': '## 🔢 Parte 2: O Robô Matemático (`range`)\n'
                       '\n'
                       'E se você quiser repetir uma coisa 10 vezes, mas não tem uma lista?\n'
                       'Nós usamos o `range` (que significa **ALCANCE** ou **INTERVALO**).\n'
                       '\n'
                       'É ótimo para fazer desenhos!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-5::cell-6',
             'index': 6,
             'cell_type': 'code',
             'source': 'print("Vou imprimir 5 Geraldos para você:")\n'
                       '\n'
                       '# Repita 5 vezes\n'
                       'for numero in range(5):\n'
                       '    print("🦸\u200d♀️ Geraldo!")',
             'requires_input': False,
             'default_code': 'print("Vou imprimir 5 Geraldos para você:")\n'
                             '\n'
                             '# Repita 5 vezes\n'
                             'for numero in range(5):\n'
                             '    print("🦸\u200d♀️ Geraldo!")'},
            {'cell_id': 'aula-5::cell-7',
             'index': 7,
             'cell_type': 'markdown',
             'source': '### ⚡ Desafio de Arte\n'
                       'No código acima, tente mudar o número `5` para `20` e a frase para outra '
                       'coisa. Veja como o computador trabalha rápido!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-5::cell-8',
             'index': 8,
             'cell_type': 'markdown',
             'source': '## 🦸\u200d♀️ O Grande Projeto: Fábrica de Super-Heróis\n'
                       '\n'
                       'Vamos pegar uma lista de pessoas normais e transformá-las em '
                       'Super-Heróis!\n'
                       '\n'
                       '**Sua Missão:**\n'
                       '1. Coloque os nomes da sua família ou amigos na lista.\n'
                       '2. O Robô `for` vai adicionar um título heroico para cada um.\n'
                       '3. Clique em **Executar magia**!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-5::cell-9',
             'index': 9,
             'cell_type': 'code',
             'source': '# Lista de pessoas comuns\n'
                       'amigos = ["Maria", "Sofia", "Cecilia", "Pedro", "Papai", "Mamãe"]\n'
                       '\n'
                       'print("⚡ ATIVANDO A MÁQUINA DE HEROIS... ⚡")\n'
                       'print("--------------------------------------")\n'
                       '\n'
                       'for pessoa in amigos:\n'
                       '    # Aqui a mágica acontece!\n'
                       '    nome_de_heroi = "Super " + pessoa + " 🚀"\n'
                       '    print(nome_de_heroi)\n'
                       '\n'
                       'print("--------------------------------------")\n'
                       'print("Todos salvos pelo poder do Python!")',
             'requires_input': False,
             'default_code': '# Lista de pessoas comuns\n'
                             'amigos = ["Maria", "Sofia", "Cecilia", "Pedro", "Papai", "Mamãe"]\n'
                             '\n'
                             'print("⚡ ATIVANDO A MÁQUINA DE HEROIS... ⚡")\n'
                             'print("--------------------------------------")\n'
                             '\n'
                             'for pessoa in amigos:\n'
                             '    # Aqui a mágica acontece!\n'
                             '    nome_de_heroi = "Super " + pessoa + " 🚀"\n'
                             '    print(nome_de_heroi)\n'
                             '\n'
                             'print("--------------------------------------")\n'
                             'print("Todos salvos pelo poder do Python!")'},
            {'cell_id': 'aula-5::cell-10',
             'index': 10,
             'cell_type': 'markdown',
             'source': '### 🏆 Desafio Extra: O Tabuada Automática\n'
                       '\n'
                       'Esse é para quem é boa em matemática!\n'
                       'O código abaixo faz a tabuada do 2 automaticamente.\n'
                       '\n'
                       'Tente mudar para fazer a tabuada do 5 ou do 9!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-5::cell-11',
             'index': 11,
             'cell_type': 'code',
             'source': 'numero_tabuada = 2\n'
                       '\n'
                       'print("Tabuada do " + str(numero_tabuada))\n'
                       '\n'
                       '# Vai contar do 1 até o 10 (o range para um número antes do final, por '
                       'isso 11)\n'
                       'for contador in range(1, 11):\n'
                       '    resultado = numero_tabuada * contador\n'
                       '    print(str(numero_tabuada) + " vezes " + str(contador) + " é igual a: " '
                       '+ str(resultado))',
             'requires_input': False,
             'default_code': 'numero_tabuada = 2\n'
                             '\n'
                             'print("Tabuada do " + str(numero_tabuada))\n'
                             '\n'
                             '# Vai contar do 1 até o 10 (o range para um número antes do final, '
                             'por isso 11)\n'
                             'for contador in range(1, 11):\n'
                             '    resultado = numero_tabuada * contador\n'
                             '    print(str(numero_tabuada) + " vezes " + str(contador) + " é '
                             'igual a: " + str(resultado))'}]},
 {'lesson_id': 'aula-6',
  'order': 6,
  'title': '🛠️ Aula 6: Mini Projetos',
  'notebook_file': 'minha_sexta_aula.ipynb',
  'total_cells': 11,
  'code_cells': 4,
  'markdown_cells': 7,
  'cells': [{'cell_id': 'aula-6::cell-1',
             'index': 1,
             'cell_type': 'markdown',
             'source': '# 📜 Aula 6: O Livro de Feitiços Secretos (Funções)\n'
                       '\n'
                       'Olá, Suprema Feiticeira! 🧙\u200d♀️✨\n'
                       '\n'
                       'Você já percebeu que às vezes a gente escreve a mesma coisa várias vezes? '
                       'Isso cansa, né?\n'
                       '\n'
                       'Hoje você vai ganhar o poder de **CRIAR SEUS PRÓPRIOS COMANDOS**!\n'
                       '\n'
                       'Isso se chama **Função**. É como escrever uma receita nova no seu livro de '
                       'mágica. Depois que você escreve a receita, basta dizer o nome dela para a '
                       'mágica acontecer.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-6::cell-2',
             'index': 2,
             'cell_type': 'markdown',
             'source': '## 🍳 Parte 1: Criando a Receita (`def`)\n'
                       '\n'
                       'Para criar um comando novo, usamos a palavra `def` (de **DEF**inir).\n'
                       '\n'
                       'Vamos ensinar o computador a dar uma risada longa. O nome do comando será '
                       '`risada_maluca`.\n'
                       '\n'
                       '**Atenção:** O código abaixo só **ensina** o computador. Ele não vai fazer '
                       'nada até você chamar o nome dele no final!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-6::cell-3',
             'index': 3,
             'cell_type': 'code',
             'source': '# 1. AQUI NÓS ENSINAMOS A RECEITA\n'
                       'def risada_maluca():\n'
                       '    print("MUAHAHAHA! 🧛")\n'
                       '    print("HOHOHOHO! 🎅")\n'
                       '    print("HIHIHIHI! 🤡")\n'
                       '\n'
                       '# 2. AGORA NÓS USAMOS O COMANDO NOVO\n'
                       'print("Vou contar uma piada...")\n'
                       'risada_maluca()  # Chamando a função!\n'
                       '\n'
                       'print("Mais uma vez!")\n'
                       'risada_maluca()  # Olha como é rápido!',
             'requires_input': False,
             'default_code': '# 1. AQUI NÓS ENSINAMOS A RECEITA\n'
                             'def risada_maluca():\n'
                             '    print("MUAHAHAHA! 🧛")\n'
                             '    print("HOHOHOHO! 🎅")\n'
                             '    print("HIHIHIHI! 🤡")\n'
                             '\n'
                             '# 2. AGORA NÓS USAMOS O COMANDO NOVO\n'
                             'print("Vou contar uma piada...")\n'
                             'risada_maluca()  # Chamando a função!\n'
                             '\n'
                             'print("Mais uma vez!")\n'
                             'risada_maluca()  # Olha como é rápido!'},
            {'cell_id': 'aula-6::cell-4',
             'index': 4,
             'cell_type': 'markdown',
             'source': 'Viu? Você escreveu os 3 prints só uma vez lá em cima. Depois, só precisou '
                       'escrever `risada_maluca()` para tudo aparecer.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-6::cell-5',
             'index': 5,
             'cell_type': 'markdown',
             'source': '## 🧪 Parte 2: O Caldeirão com Ingredientes (Parâmetros)\n'
                       '\n'
                       'Uma receita pode mudar dependendo do ingrediente. Um bolo pode ser de '
                       'chocolate ou de cenoura.\n'
                       '\n'
                       'Nossas funções também aceitam ingredientes! Nós colocamos eles dentro dos '
                       'parênteses `( )`.\n'
                       '\n'
                       'Vamos criar um comando chamado `dar_oi_especial`.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-6::cell-6',
             'index': 6,
             'cell_type': 'code',
             'source': 'def dar_oi_especial(nome):\n'
                       '    print("✨ Olá, " + nome + "! Seja bem-vinda! ✨")\n'
                       '\n'
                       '# Agora vamos usar com ingredientes diferentes\n'
                       'dar_oi_especial("Mamãe")\n'
                       'dar_oi_especial("Papai")\n'
                       'dar_oi_especial("Vovó")',
             'requires_input': False,
             'default_code': 'def dar_oi_especial(nome):\n'
                             '    print("✨ Olá, " + nome + "! Seja bem-vinda! ✨")\n'
                             '\n'
                             '# Agora vamos usar com ingredientes diferentes\n'
                             'dar_oi_especial("Mamãe")\n'
                             'dar_oi_especial("Papai")\n'
                             'dar_oi_especial("Vovó")'},
            {'cell_id': 'aula-6::cell-9',
             'index': 9,
             'cell_type': 'markdown',
             'source': '### ⚡ Desafio Mágico\n'
                       'No código acima, tente chamar o comando `dar_oi_especial` colocando o '
                       '**seu nome** dentro dos parênteses!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-6::cell-10',
             'index': 10,
             'cell_type': 'markdown',
             'source': '## 🎨 O Grande Projeto: O Robô Decorador\n'
                       '\n'
                       'Vamos criar um comando que deixa qualquer frase bonita.\n'
                       'Você vai criar a função `enfeitar`.\n'
                       '\n'
                       'Sempre que você usar o `enfeitar`, o texto vai aparecer cercado de '
                       'estrelas!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-6::cell-11',
             'index': 11,
             'cell_type': 'code',
             'source': '# Criando a função (A Receita)\n'
                       'def enfeitar(frase):\n'
                       '    print("★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")\n'
                       '    print("★ " + frase + " ★")\n'
                       '    print("★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")\n'
                       '\n'
                       '# Usando a função (Cozinhando)\n'
                       'enfeitar("EU AMO PYTHON")\n'
                       '\n'
                       'enfeitar("MINHA FAMÍLIA É LEGAL")\n'
                       '\n'
                       '# Podemos até usar input junto!\n'
                       'sua_frase = input()\n'
                       'enfeitar(sua_frase)',
             'requires_input': True,
             'default_code': '# Criando a função (A Receita)\n'
                             'def enfeitar(frase):\n'
                             '    print("★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")\n'
                             '    print("★ " + frase + " ★")\n'
                             '    print("★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")\n'
                             '\n'
                             '# Usando a função (Cozinhando)\n'
                             'enfeitar("EU AMO PYTHON")\n'
                             '\n'
                             'enfeitar("MINHA FAMÍLIA É LEGAL")\n'
                             '\n'
                             '# Podemos até usar input junto!\n'
                             'sua_frase = input()\n'
                             'enfeitar(sua_frase)'},
            {'cell_id': 'aula-6::cell-12',
             'index': 12,
             'cell_type': 'markdown',
             'source': '### 🏆 Missão de Casa: A Calculadora da Idade de Cachorro 🐶\n'
                       '\n'
                       'Dizem que 1 ano de humano vale 7 anos de cachorro.\n'
                       'Tente criar uma função chamada `idade_canina(numero)` que faz essa conta '
                       'para você!\n'
                       '\n'
                       '*(Dica: Dentro da função, você faz `print(numero * 7)`)*',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-6::cell-13',
             'index': 13,
             'cell_type': 'code',
             'source': 'def idade_canina(numero):\n'
                       '    # Um ano humano vale sete anos de cachorro.\n'
                       '    print(numero * 7)\n'
                       '\n'
                       'idade_canina(2)',
             'requires_input': False,
             'default_code': 'def idade_canina(numero):\n'
                             '    # Um ano humano vale sete anos de cachorro.\n'
                             '    print(numero * 7)\n'
                             '\n'
                             'idade_canina(2)'}]},
 {'lesson_id': 'aula-7',
  'order': 7,
  'title': '🏆 Aula 7: Desafios Finais',
  'notebook_file': 'minha_setima_aula.ipynb',
  'total_cells': 8,
  'code_cells': 3,
  'markdown_cells': 5,
  'cells': [{'cell_id': 'aula-7::cell-1',
             'index': 1,
             'cell_type': 'markdown',
             'source': '# 📘 Aula 7: O Guardião dos Segredos (Dicionários)\n'
                       '\n'
                       'Bem-vinda, Mestra dos Dados! 👩\u200d💻✨\n'
                       '\n'
                       'Lembra das Listas? Elas são ótimas, mas às vezes é difícil lembrar se o '
                       'nome do herói está na posição 0 ou 1.\n'
                       '\n'
                       'Hoje vamos aprender a usar **Dicionários**.\n'
                       'Imagine uma gaveta cheia de etiquetas. Você puxa a etiqueta "Nome" e vê o '
                       'nome. Puxa a etiqueta "Cor" e vê a cor.\n'
                       '\n'
                       'Isso é perfeito para criar personagens de jogos!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-7::cell-2',
             'index': 2,
             'cell_type': 'markdown',
             'source': '## 🏷️ Parte 1: Criando o Personagem (`{}`)\n'
                       '\n'
                       'Para criar um dicionário, usamos as chaves `{ }`.\n'
                       'Dentro dele, colocamos pares de **Etiqueta : Valor**.\n'
                       '\n'
                       'Vamos criar um monstrinho:',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-7::cell-3',
             'index': 3,
             'cell_type': 'code',
             'source': '# Criando nosso monstrinho\n'
                       'monstro = {\n'
                       '    "nome": "Bolota",\n'
                       '    "cor": "Roxo",\n'
                       '    "fome": 5,      # De 0 a 10\n'
                       '    "alegria": 5    # De 0 a 10\n'
                       '}\n'
                       '\n'
                       'print("Nasceu um monstro!")\n'
                       'print(monstro)',
             'requires_input': False,
             'default_code': '# Criando nosso monstrinho\n'
                             'monstro = {\n'
                             '    "nome": "Bolota",\n'
                             '    "cor": "Roxo",\n'
                             '    "fome": 5,      # De 0 a 10\n'
                             '    "alegria": 5    # De 0 a 10\n'
                             '}\n'
                             '\n'
                             'print("Nasceu um monstro!")\n'
                             'print(monstro)'},
            {'cell_id': 'aula-7::cell-4',
             'index': 4,
             'cell_type': 'markdown',
             'source': '## 🔍 Parte 2: Lendo as Etiquetas\n'
                       '\n'
                       'Para saber o nome do monstro, não usamos `[0]`. Nós usamos a etiqueta '
                       '`["nome"]`.\n'
                       'É muito mais fácil de ler!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-7::cell-5',
             'index': 5,
             'cell_type': 'code',
             'source': 'print("O nome do monstro é: " + monstro["nome"])\n'
                       'print("A cor dele é: " + monstro["cor"])\n'
                       '\n'
                       '# Podemos ver os números também\n'
                       'print("Fome atual: " + str(monstro["fome"]))\n'
                       '\n'
                       '# E se a gente mudar o nome dele?\n'
                       'monstro["nome"] = "Fofinho"\n'
                       'print("Agora o nome dele é: " + monstro["nome"])',
             'requires_input': False,
             'default_code': 'print("O nome do monstro é: " + monstro["nome"])\n'
                             'print("A cor dele é: " + monstro["cor"])\n'
                             '\n'
                             '# Podemos ver os números também\n'
                             'print("Fome atual: " + str(monstro["fome"]))\n'
                             '\n'
                             '# E se a gente mudar o nome dele?\n'
                             'monstro["nome"] = "Fofinho"\n'
                             'print("Agora o nome dele é: " + monstro["nome"])'},
            {'cell_id': 'aula-7::cell-6',
             'index': 6,
             'cell_type': 'markdown',
             'source': '## 🎮 O Grande Projeto: Seu Bichinho Virtual (Tamagotchi) 👾\n'
                       '\n'
                       'Agora vamos juntar TUDO o que você aprendeu em 7 aulas!\n'
                       '1. Variáveis (O Bicho)\n'
                       '2. Funções (Ações de comer e brincar)\n'
                       '3. While (O jogo rodando para sempre)\n'
                       '4. Input (Você escolhendo o que fazer)\n'
                       '\n'
                       '**Regras:**\n'
                       '- Se comer: Fome diminui, mas Alegria aumenta um pouco.\n'
                       '- Se brincar: Alegria aumenta muito, mas Fome também aumenta!\n'
                       '\n'
                       'Clique em **Executar magia**, preencha as respostas no pop-up e cuide do '
                       'seu bichinho!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-7::cell-7',
             'index': 7,
             'cell_type': 'code',
             'source': 'import time\n'
                       '\n'
                       '# 1. Criando o Bicho\n'
                       'bicho = {\n'
                       '    "nome": input("Que nome você quer dar ao seu bichinho? "),\n'
                       '    "fome": 5,\n'
                       '    "alegria": 5\n'
                       '}\n'
                       '\n'
                       '# 2. Funções de Ação\n'
                       'def mostrar_status():\n'
                       '    print("----------------------------")\n'
                       '    print(bicho["nome"] + " está assim:")\n'
                       '    print("🍖 Fome: " + str(bicho["fome"]))\n'
                       '    print("😊 Alegria: " + str(bicho["alegria"]))\n'
                       '    print("----------------------------")\n'
                       '\n'
                       'def alimentar():\n'
                       '    print("Dando comida... Nhac nhac! 🍎")\n'
                       '    bicho["fome"] = bicho["fome"] - 2\n'
                       '    bicho["alegria"] = bicho["alegria"] + 1\n'
                       '\n'
                       'def brincar():\n'
                       '    print("Jogando bola! Boing boing! ⚽")\n'
                       '    bicho["alegria"] = bicho["alegria"] + 3\n'
                       '    bicho["fome"] = bicho["fome"] + 1\n'
                       '\n'
                       '# 3. O Jogo Começa (Loop Infinito)\n'
                       'while True:\n'
                       '    mostrar_status()\n'
                       '\n'
                       '    acao = input("O que você quer fazer? (1-Comer, 2-Brincar, 3-Sair): ")\n'
                       '\n'
                       '    if acao == "1":\n'
                       '        alimentar()\n'
                       '    elif acao == "2":\n'
                       '        brincar()\n'
                       '    elif acao == "3":\n'
                       '        print("Tchau! O " + bicho["nome"] + " vai dormir.")\n'
                       '        break # O break quebra o loop e encerra o jogo\n'
                       '    else:\n'
                       '        print("Não entendi... tente 1, 2 ou 3.")\n'
                       '\n'
                       '    time.sleep(1)',
             'requires_input': True,
             'default_code': 'import time\n'
                             '\n'
                             '# 1. Criando o Bicho\n'
                             'bicho = {\n'
                             '    "nome": input("Que nome você quer dar ao seu bichinho? "),\n'
                             '    "fome": 5,\n'
                             '    "alegria": 5\n'
                             '}\n'
                             '\n'
                             '# 2. Funções de Ação\n'
                             'def mostrar_status():\n'
                             '    print("----------------------------")\n'
                             '    print(bicho["nome"] + " está assim:")\n'
                             '    print("🍖 Fome: " + str(bicho["fome"]))\n'
                             '    print("😊 Alegria: " + str(bicho["alegria"]))\n'
                             '    print("----------------------------")\n'
                             '\n'
                             'def alimentar():\n'
                             '    print("Dando comida... Nhac nhac! 🍎")\n'
                             '    bicho["fome"] = bicho["fome"] - 2\n'
                             '    bicho["alegria"] = bicho["alegria"] + 1\n'
                             '\n'
                             'def brincar():\n'
                             '    print("Jogando bola! Boing boing! ⚽")\n'
                             '    bicho["alegria"] = bicho["alegria"] + 3\n'
                             '    bicho["fome"] = bicho["fome"] + 1\n'
                             '\n'
                             '# 3. O Jogo Começa (Loop Infinito)\n'
                             'while True:\n'
                             '    mostrar_status()\n'
                             '\n'
                             '    acao = input("O que você quer fazer? (1-Comer, 2-Brincar, '
                             '3-Sair): ")\n'
                             '\n'
                             '    if acao == "1":\n'
                             '        alimentar()\n'
                             '    elif acao == "2":\n'
                             '        brincar()\n'
                             '    elif acao == "3":\n'
                             '        print("Tchau! O " + bicho["nome"] + " vai dormir.")\n'
                             '        break # O break quebra o loop e encerra o jogo\n'
                             '    else:\n'
                             '        print("Não entendi... tente 1, 2 ou 3.")\n'
                             '\n'
                             '    time.sleep(1)'},
            {'cell_id': 'aula-7::cell-8',
             'index': 8,
             'cell_type': 'markdown',
             'source': '### 🏆 Desafio Mestre\n'
                       '\n'
                       'Se a fome chegar em 10, o bichinho desmaia!\n'
                       'Tente adicionar um `if` dentro do loop para avisar:\n'
                       '**"CUIDADO! SEU BICHINHO ESTÁ MORRENDO DE FOME!"**',
             'requires_input': False,
             'default_code': None}]},
 {'lesson_id': 'aula-8',
  'order': 8,
  'title': '📊 Aula 8: A Grande Mestra',
  'notebook_file': 'minha_oitava_aula.ipynb',
  'total_cells': 9,
  'code_cells': 4,
  'markdown_cells': 5,
  'cells': [{'cell_id': 'aula-8::cell-1',
             'index': 1,
             'cell_type': 'markdown',
             'source': '# 📊 Aula 8: A Artista de Dados (Desenhando Gráficos)\n'
                       '\n'
                       'Olá, Grande Criadora! 🎨\n'
                       '\n'
                       'Você já sabe programar textos, contas e jogos. Mas sabia que o Python '
                       'também sabe desenhar?\n'
                       '\n'
                       'Hoje vamos transformar **LISTAS** (aquelas do Aula 4) em **GRÁFICOS** '
                       'coloridos.\n'
                       'Isso se chama "Ciência de Dados". É como pegar números chatos e '
                       'transformar em uma pintura!\n'
                       '\n'
                       'Vamos abrir nossa caixa de lápis de cor digital, chamada `matplotlib`.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-8::cell-2',
             'index': 2,
             'cell_type': 'markdown',
             'source': '## 📈 Parte 1: Ligando os Pontos (`plot`)\n'
                       '\n'
                       'Lembra da brincadeira de ligar os pontos? O computador faz isso muito '
                       'rápido.\n'
                       '\n'
                       'Vamos imaginar que estamos plantando um **Feijão Mágico** 🌱.\n'
                       'Vamos anotar o tamanho dele a cada dia.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-8::cell-3',
             'index': 3,
             'cell_type': 'code',
             'source': 'import matplotlib.pyplot as plt\n'
                       '\n'
                       '# Dia 1, Dia 2, Dia 3, Dia 4, Dia 5\n'
                       'dias = [1, 2, 3, 4, 5]\n'
                       '\n'
                       '# Tamanho da planta em centímetros\n'
                       'tamanho = [2, 4, 8, 16, 32]\n'
                       '\n'
                       'print("Desenhando o crescimento da planta... 🖌️")\n'
                       '\n'
                       '# O comando plot desenha a linha\n'
                       'plt.plot(dias, tamanho)\n'
                       '\n'
                       '# Colocando título no desenho\n'
                       'plt.title("O Crescimento do Feijão Mágico 🌱")\n'
                       'plt.xlabel("Dias")\n'
                       'plt.ylabel("Centímetros")\n'
                       '\n'
                       '# Mostre o desenho!\n'
                       'plt.show()',
             'requires_input': False,
             'default_code': 'import matplotlib.pyplot as plt\n'
                             '\n'
                             '# Dia 1, Dia 2, Dia 3, Dia 4, Dia 5\n'
                             'dias = [1, 2, 3, 4, 5]\n'
                             '\n'
                             '# Tamanho da planta em centímetros\n'
                             'tamanho = [2, 4, 8, 16, 32]\n'
                             '\n'
                             'print("Desenhando o crescimento da planta... 🖌️")\n'
                             '\n'
                             '# O comando plot desenha a linha\n'
                             'plt.plot(dias, tamanho)\n'
                             '\n'
                             '# Colocando título no desenho\n'
                             'plt.title("O Crescimento do Feijão Mágico 🌱")\n'
                             'plt.xlabel("Dias")\n'
                             'plt.ylabel("Centímetros")\n'
                             '\n'
                             '# Mostre o desenho!\n'
                             'plt.show()'},
            {'cell_id': 'aula-8::cell-4',
             'index': 4,
             'cell_type': 'markdown',
             'source': 'Uau! Você viu como a linha subiu rápido?\n'
                       '\n'
                       '## 🎨 Parte 2: Mudando as Cores\n'
                       '\n'
                       'O gráfico azul é bonito, mas podemos mudar a cor e colocar bolinhas nos '
                       'pontos.\n'
                       '\n'
                       '- `color="red"` (vermelho), `"green"` (verde), `"purple"` (roxo)\n'
                       '- `marker="o"` (faz uma bolinha em cada dia)\n'
                       '\n'
                       'Tente mudar a cor no código abaixo:',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-8::cell-5',
             'index': 5,
             'cell_type': 'code',
             'source': 'import matplotlib.pyplot as plt\n'
                       '\n'
                       'dias = ["Seg", "Ter", "Qua", "Qui", "Sex"]\n'
                       'temperatura = [25, 28, 22, 30, 31]\n'
                       '\n'
                       '# Tente mudar "orange" para "pink" ou "green"\n'
                       'plt.plot(dias, temperatura, color="orange", marker="o")\n'
                       '\n'
                       'plt.title("Temperatura da Semana ☀️")\n'
                       'plt.show()',
             'requires_input': False,
             'default_code': 'import matplotlib.pyplot as plt\n'
                             '\n'
                             'dias = ["Seg", "Ter", "Qua", "Qui", "Sex"]\n'
                             'temperatura = [25, 28, 22, 30, 31]\n'
                             '\n'
                             '# Tente mudar "orange" para "pink" ou "green"\n'
                             'plt.plot(dias, temperatura, color="orange", marker="o")\n'
                             '\n'
                             'plt.title("Temperatura da Semana ☀️")\n'
                             'plt.show()'},
            {'cell_id': 'aula-8::cell-6',
             'index': 6,
             'cell_type': 'markdown',
             'source': '## 📊 O Grande Projeto: Votação das Frutas (Gráfico de Barras)\n'
                       '\n'
                       'Para comparar coisas (quem tem mais?), o melhor é o **Gráfico de '
                       'Barras**.\n'
                       '\n'
                       'Imagine que você fez uma pesquisa na escola: "Qual é sua fruta favorita?"\n'
                       '\n'
                       'Em vez de `plt.plot`, vamos usar `plt.bar`.',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-8::cell-7',
             'index': 7,
             'cell_type': 'code',
             'source': 'import matplotlib.pyplot as plt\n'
                       '\n'
                       '# Nomes das frutas\n'
                       'frutas = ["Maçã 🍎", "Banana 🍌", "Uva 🍇", "Laranja 🍊"]\n'
                       '\n'
                       '# Quantos votos cada uma teve\n'
                       'votos = [5, 10, 3, 8]\n'
                       '\n'
                       '# Criando o gráfico de barras\n'
                       '# Podemos escolher uma cor para cada barra!\n'
                       'cores = ["red", "yellow", "purple", "orange"]\n'
                       '\n'
                       'plt.bar(frutas, votos, color=cores)\n'
                       '\n'
                       'plt.title("Campeonato das Frutas 🏆")\n'
                       'plt.show()',
             'requires_input': False,
             'default_code': 'import matplotlib.pyplot as plt\n'
                             '\n'
                             '# Nomes das frutas\n'
                             'frutas = ["Maçã 🍎", "Banana 🍌", "Uva 🍇", "Laranja 🍊"]\n'
                             '\n'
                             '# Quantos votos cada uma teve\n'
                             'votos = [5, 10, 3, 8]\n'
                             '\n'
                             '# Criando o gráfico de barras\n'
                             '# Podemos escolher uma cor para cada barra!\n'
                             'cores = ["red", "yellow", "purple", "orange"]\n'
                             '\n'
                             'plt.bar(frutas, votos, color=cores)\n'
                             '\n'
                             'plt.title("Campeonato das Frutas 🏆")\n'
                             'plt.show()'},
            {'cell_id': 'aula-8::cell-8',
             'index': 8,
             'cell_type': 'markdown',
             'source': '### 🏆 Desafio da Cientista\n'
                       '\n'
                       'Crie um gráfico sobre a sua família ou amigos!\n'
                       '\n'
                       'Ideias:\n'
                       '1. **Idade das pessoas:** Crie uma lista com nomes e outra com idades.\n'
                       '2. **Pontuação de Videogame:** Quem fez mais pontos?\n'
                       '\n'
                       'Use o **Laboratório de código abaixo**. Os comentários mostram onde trocar '
                       'os nomes, os números, as cores e o título. Depois, clique em **Executar '
                       'magia** para ver o resultado!',
             'requires_input': False,
             'default_code': None},
            {'cell_id': 'aula-8::cell-9',
             'index': 9,
             'cell_type': 'code',
             'source': 'import matplotlib.pyplot as plt\n'
                       '\n'
                       '# 1. Troque os nomes entre aspas pelos nomes da sua família ou dos seus '
                       'amigos.\n'
                       'nomes = ["Maria", "José", "João"]\n'
                       '\n'
                       '# 2. Troque os números pelas idades ou pontuações de cada pessoa.\n'
                       'numeros = [10, 35, 62]\n'
                       '\n'
                       '# 3. Você também pode trocar as cores das barras.\n'
                       'cores = ["purple", "orange", "green"]\n'
                       '\n'
                       '# 4. Troque o título para explicar o que o seu gráfico mostra.\n'
                       'titulo = "Idade da minha família"\n'
                       '\n'
                       '# O computador usa suas listas para desenhar o gráfico.\n'
                       'plt.bar(nomes, numeros, color=cores)\n'
                       'plt.title(titulo)\n'
                       'plt.xlabel("Pessoas")\n'
                       'plt.ylabel("Idade ou pontuação")\n'
                       'plt.show()',
             'requires_input': False,
             'default_code': 'import matplotlib.pyplot as plt\n'
                             '\n'
                             '# 1. Troque os nomes entre aspas pelos nomes da sua família ou dos '
                             'seus amigos.\n'
                             'nomes = ["Maria", "José", "João"]\n'
                             '\n'
                             '# 2. Troque os números pelas idades ou pontuações de cada pessoa.\n'
                             'numeros = [10, 35, 62]\n'
                             '\n'
                             '# 3. Você também pode trocar as cores das barras.\n'
                             'cores = ["purple", "orange", "green"]\n'
                             '\n'
                             '# 4. Troque o título para explicar o que o seu gráfico mostra.\n'
                             'titulo = "Idade da minha família"\n'
                             '\n'
                             '# O computador usa suas listas para desenhar o gráfico.\n'
                             'plt.bar(nomes, numeros, color=cores)\n'
                             'plt.title(titulo)\n'
                             'plt.xlabel("Pessoas")\n'
                             'plt.ylabel("Idade ou pontuação")\n'
                             'plt.show()'}]}]
